Name:		rustc
Version:	1.10.0
Release:	1.multi
Summary:	A well typed low-level langauge

Group:		Development/Languages
License:	GPLv3
URL:		http://rust-lang.org/

BuildRequires:	git make cmake python curl
Requires:	llvm
AutoReqProv:	no

Source:		https://static.rust-lang.org/dist/%{name}-%{version}-i686-unknown-linux-gnu.tar.gz

%global _prefix /usr
%global _missing_build_ids_terminate_build 0
%define debug_package %{nil}

%description
Automatically built installer for rust


%prep
%autosetup -n %{name}-%{version}-i686-unknown-linux-gnu


%build


%install
./install.sh --destdir=%{buildroot} --prefix=%{_prefix} --libdir=%{buildroot}%{_libdir} --mandir=%{buildroot}%{_mandir}
rm %{buildroot}%{_libdir}/rustlib/uninstall.sh
rm %{buildroot}%{_libdir}/rustlib/install.log
rm %{buildroot}%{_libdir}/rustlib/manifest-rustc


%files
%doc
%{_prefix}/bin/*
%{_libdir}/*
%{_defaultdocdir}/*
%{_mandir}/man1/*

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Made the initial repo
