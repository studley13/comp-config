Name:		curtis-host-blue
Version:	1.0
Release:	1%{?dist}
Summary:	Meta-package for installing software for host 'blue'

Group:		Applications/System
License:	ISC
BuildArch:	noarch

Requires:	rpmfusion-free-release
Requires:	rpmfusion-nonfree-release
Requires:	curtis-desk
Requires:	curtis-tools

%description
Package dependancies for Blue Thinkpad x100e

%prep

%build

%clean

%install

%files

%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Created initial package
