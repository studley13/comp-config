Name:		curtis-repos
Version:	1.0
Release:	1.multi
Summary:	Meta-package for installing repos

Group:		System Environment/Base
License:	ISC
BuildArch:	noarch

Requires:	rpmfusion-free-release
Requires:	rpmfusion-nonfree-release
Requires:	google-chrome-repo
Requires:	skype-repo
Requires:	vivaldi-repo
Requires:	ntop-repo
Requires:	handbrake-repo
Requires:	bumblebee-release bumblebee-nonfree-release

%description
Standard repositories

%prep

%build

%clean

%install

%files

%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Created initial package
