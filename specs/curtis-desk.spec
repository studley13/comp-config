Name:		curtis-desk
Version:	1.5.2
Release:	1.multi
Summary:	Meta-package for installing desktop and GUI software

Group:		Applications/System
License:	ISC
BuildArch:	noarch

Requires:	curtis-repos
Requires:	acpi
Requires:	sysstat
Requires:	xorg-x11-xinit-session
Requires:	perl-Env
Requires:	anthy
Requires:	baobab
Requires:	Thunar
Requires:	cdparanoia
Requires:	chromium chromium-libs chromium-libs-media
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
Requires:	gparted
Requires:	i3 i3lock i3status
Requires:	i3blocks
Requires:	ibus ibus-gtk
Requires:	libimobiledevice libimobiledevice-utils
Requires:	intel-gpu-tools
Requires:	jack-audio-connection-kit alsa-plugins-jack pulseaudio-module-jack
Requires:	libreoffice
Requires:	lxappearance lxinput lxrandr lxterminal
Requires:	mesa-demos
Requires:	nitrogen
Requires:	numlockx
Requires:	pavucontrol
Requires:	playerctl
Requires:	powertop
Requires:	qjackctl
Requires:	redshift
Requires:	remmina
Requires:	seahorse
Requires:	simple-scan
Requires:	VirtualGL
#Requires:	wine
Requires:	dosbox
Requires:	wireshark wireshark-gtk
Requires:	xbacklight
Requires:	gnome-screensaver
Requires:	network-manager-applet
Requires:	font-awesome
Requires:	ubuntu-font-family
Requires:	gucharmap
Requires:	faience-icon-theme
Requires:	hicolor-icon-theme
Requires:   	texlive-scheme-full
Requires:	workrave-gtk2
Requires:	xcompmgr

%description
Standard desktop and GUI software

%prep

%build

%clean

%install

%files

%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Created initial package
