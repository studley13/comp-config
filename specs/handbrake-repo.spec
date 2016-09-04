Name:		handbrake-repo
Version:	1.0
Release:	1.multi
Summary:	Package to install the handbrake-repo
BuildArch:	noarch

Group:		Applications/Multimedia
License:	ISC
URL:		http://handbrake.fr/

#Requires:	epel-release

%description
Package to install the repository of handbrake.


%prep


%build


%install
mkdir -p %{buildroot}/etc/yum.repos.d/
cat > %{buildroot}/etc/yum.repos.d/handbrake.repo << __endRepo
[fedora-HandBrake]
name=negativo17 - Open source multiplatform video transcoder
baseurl=http://negativo17.org/repos/HandBrake/fedora-$releasever/$basearch/
enabled=1
skip_if_unavailable=1
gpgkey=http://negativo17.org/repos/RPM-GPG-KEY-slaanesh
gpgcheck=1

[fedora-HandBrake-source]
name=negativo17 - Open source multiplatform video transcoder - Source
baseurl=http://negativo17.org/repos/HandBrake/fedora-$releasever/SRPMS
enabled=0
skip_if_unavailable=1
gpgkey=http://negativo17.org/repos/RPM-GPG-KEY-slaanesh
gpgcheck=1
__endRepo


%files
/etc/yum.repos.d/handbrake.repo


%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Created package
