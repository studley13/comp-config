Name:		playerctl
Version:	1.0
Release:	1.multi
Summary:	Control all the media players

Group:		System Environment/Shells
License:	GPLv3
URL:		http://github.com/acrisci/playerctl

BuildRequires:	git make gtk-doc autoconf automake glib2-devel libtool gobject-introspection-devel
Requires:	i3

%global _prefix /usr

%description
A command line control interface to multiple media players


%prep
rm -rf %{name}
git clone http://github.com/acrisci/playerctl %{name}


%build
pushd %{name} > /dev/null
./autogen.sh --prefix=%{_prefix}
make
popd > /dev/null


%install
pushd %{name} > /dev/null
%make_install
popd > /dev/null


%files
%doc
%{_prefix}/bin/*
%{_prefix}/include/*
%{_prefix}/lib/*
%{_prefix}/share/*

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Made the initial repo
