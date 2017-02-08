Name:		curtis-desk-full
Version:	1.3.2
Release:	1.multi
Summary:	Meta-package for installing desktop and GUI software

Group:		Applications/System
License:	ISC
BuildArch:	noarch

Requires:	curtis-repos
Requires:	curtis-desk
Requires:	chrome-remote-desktop
Requires:	google-chrome-stable
Requires:	skypeforlinux
Requires:	vivaldi-stable
Requires:	google-android-emoji-fonts google-noto-sans-fonts google-noto-emoji-fonts
Requires:	anki
Requires:	VirtualBox kmod-VirtualBox

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
