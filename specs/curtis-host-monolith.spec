Name:		curtis-host-monolith
Version:	1.3.0
Release:	1.multi
Summary:	Meta-package for installing software for host 'monolith'

Group:		Applications/System
License:	ISC
BuildArch:	noarch

Requires:	curtis-repos
Requires:	curtis-desk-full
Requires:	curtis-tools
Requires:	curtis-media
Requires:	curtis-av
Requires:	curtis-games
#Requires:	xorg-x11-drv-nvidia kmod-nvidia
Requires:	gstreamer1-plugins-bad-nvenc
Requires:	dkms-nvidia nvidia-driver nvidia-driver-cuda nvidia-driver-libs.i686 kernel-devel
Requires:	vulkan.i686 cuda nvidia-driver-cuda-libs.i686

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
