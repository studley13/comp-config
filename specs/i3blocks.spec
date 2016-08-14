Name:		i3blocks
Version:	1.0
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


%build


%install
pushd %{name} > /dev/null
%make_install
popd > /dev/null


%files
%doc
%{_prefix}/bin/*
%{_prefix}%{_sysconfdir}/*
%{_libexecdir}/*




%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Made the initial repo
