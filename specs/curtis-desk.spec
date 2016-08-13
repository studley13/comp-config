Name:		curtis-desk
Version:	1.0
Release:	1%{?dist}
Summary:	Meta-package for installing desktop and GUI software

Group:		Applications/System
License:	ISC
BuildArch:	noarch

Requires:	rpmfusion-free-release
Requires:	rpmfusion-nonfree-release
Requires:	anthy
Requires:	baobab
Requires:	Thunar
Requires:	cdparanoia
Requires:	chromium
Requires:	chrome-remote-desktop
Requires:	dropbox
Requires:	eog
Requires:	evince
Requires:	filezilla
Requires:	firefox
Requires:	ghex
Requires:	beesu
Requires:	glmark2
Requires:	gnome-disk-utility
Requires:	gnome-font-viewer
Requires:	gnome-keyring
Requires:	gnome-power-manager
Requires:	gnome-screenshot
Requires:	gnome-system-monitor
Requires:	xfce4-terminal
#Requires:	google-chrome
Requires:	gparted
Requires:	i3 i3lock i3status
#Requires:	i3blocks
Requires:	ibus ibus-gtk im-config
Requires:	libimobiledevice libimobiledevice-utils
Requires:	intel-gpu-tools
#Requires:	intel-linux-graphics-installer
Requires:	jack-audio-connection-kit alsa-plugins-jack pulseaudio-module-jack
Requires:	libreoffice
Requires:	lxappearance lxinput lxrandr lxterminal
Requires:	mesa-demos
Requires:	nitrogen
Requires:	numlockx
Requires:	pavucontrol
#Requires:	playerctl
Requires:	powertop
Requires:	qjackctl
Requires:	redshift
Requires:	remmina
#Requires:	ripit
Requires:	seahorse
Requires:	simple-scan
#Requires:	skype
Requires:	VirtualGL
#Requires:	Vivaldi
Requires:	wine
Requires:	dosbox
Requires:	wireshark
Requires:	xbacklight
Requires:	gnome-screensaver
Requires:	network-manager-applet
Requires:	font-awesome
Requires:	ubuntu-font-family
Requires:	gucharmap

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
