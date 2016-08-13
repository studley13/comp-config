Name:		curtis-host-monolith
Version:	1.0
Release:	1%{?dist}
Summary:	Meta-package for installing software for host 'monolith'

Group:		Applications/System
License:	ISC
BuildArch:	noarch

Requires:	rpmfusion-free-release
Requires:	rpmfusion-nonfree-release
Requires:	curtis-desk
Requires:	curtis-tools
Requires:	curtis-media
Requires:	curtis-av
Requires:	curtis-games
Requires:	xorg-x11-drv-nvidia-340xx

%description
Package dependancies for tower

%prep

%build

%clean

%install

%files

%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Created initial package
