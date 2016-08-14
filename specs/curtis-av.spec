Name:		curtis-av
Version:	1.0
Release:	1.multi
Summary:	Meta-package for installing AV software

Group:		Applications/Multimedia
License:	ISC
BuildArch:	noarch

Requires:	curtis-repos
Requires:	audacity 
Requires:	blender 
Requires:	dcraw 
Requires:	gimp 
Requires:	inkscape 
Requires:	lmms 
Requires:	picard 
Requires:	mypaint 
Requires:	rawtherapee
#Requires:	obs-studio
Requires:	libwacom xorg-x11-drv-wacom

%description
A collection of multimedia software inclding audio tools, 3D modelling
tools, image editing software

%prep

%build

%clean

%install

%files

%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Created initial package
- added Audacity
- added Blender
- added DCRaw
- added The GIMP
- added Inkscape
- added LMMS
- added MusicBrainz Picard
- added MyPaint
- added Rawtherapee
