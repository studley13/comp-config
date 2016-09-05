Name:		binaryninja
Version:	1.0
Release:	1.multi
Summary:	Binary inspection

Group:		Development/Tools
License:	GPLv3
URL:		http://binary.ninja/

Source:		https://cdn.binary.ninja/installers/BinaryNinja-demo.zip

%global _prefix /opt
%global _missing_build_ids_terminate_build 0
%define debug_package %{nil}

%description
Automatically built installer for binaryninja


%prep
%autosetup -n binaryninja


%build


%install
mkdir -p %{buildroot}%{prefix}/binaryninja
cp -rv %{builddir}/* %{buildroot}%{prefix}/binaryninja
ln -s %{prefix}/binaryninja/binaryninja /usr/local/bin/binaryninja


%files
%doc
%{_prefix}/*
/usr/local/bin

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Made the initial repo
