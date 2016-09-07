Name:		curtis-host-core
Version:	1.1
Release:	1.multi
Summary:	Meta-package for installing software for host 'core'

Group:		Applications/System
License:	ISC
BuildArch:	noarch

Requires:	curtis-repos
Requires:	rpmfusion-free-release
Requires:	rpmfusion-nonfree-release
Requires:	curtis-tools
Requires:	curtis-media
Requires:	curtis-server
Requires:	libva-intel-driver

%description
Package dependancies for Intel NUC

%prep

%build

%clean

%install

%files

%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Created initial package
