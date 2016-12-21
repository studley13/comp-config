Name:		curtis-host-black
Version:	1.10.1
Release:	1.multi
Summary:	Meta-package for installing software for host 'black'

Group:		Applications/System
License:	ISC
BuildArch:	noarch

Requires:	curtis-repos
Requires:	curtis-desk-full
Requires:	curtis-tools
Requires:	curtis-media
Requires:	curtis-av
Requires:	curtis-games
#Requires:	bbswitch-dkms
#Requires:	gstreamer1-plugins-bad-nvenc
#Requires:	bumblebee-nvidia dkms-nvidia nvidia-driver nvidia-driver-cuda
#Requires:	nvidia-driver-cuda-libs(x86-32) nvidia-driver-libs(x86-32) vulkan(x86-32)
Requires:	kernel-devel
Requires:	VirtualGL
%if %{__isa_bits} == 64
Requires: 	VirtualGL(%{__isa_name}-32)
%endif
Requires:	primus
%if %{__isa_bits} == 64
Requires: 	primus(%{__isa_name}-32)
%endif

%description
Package dependancies for Black and silver Asus S550-CM

%prep

%build

%clean

%install

%files

%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Created initial package
