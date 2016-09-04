Name:		i3blocks
Version:	1.4
Release:	1.multi
Summary:	A block based provider for i3bar

Group:		System Environment/Shells
License:	GPLv3
URL:		http://github.com/vivien/i3blocks

BuildRequires:	git make pandoc
Requires:	i3

%global _prefix /usr/local

%description
Blocky json interface to i3bar


%prep
rm -rf %{name}
git clone http://github.com/vivien/i3blocks %{name}
git clone http://github.com/vivien/i3blocks-contrib %{name}/i3-contrib


%build
pushd %{name} > /dev/null
make clean all
popd > /dev/null


%install
pushd %{name} > /dev/null
%make_install
cp i3-contrib/mediaplayer/mediaplayer %{buildroot}%{_prefix}/libexec/i3blocks/
popd > /dev/null


%files
%doc
%{_prefix}/bin/*
%{_prefix}%{_sysconfdir}/*
%{_libexecdir}/*




%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Made the initial repo
