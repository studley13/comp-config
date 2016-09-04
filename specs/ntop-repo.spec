Name:		ntop-repo
Version:	1.0
Release:	1.multi
Summary:	Package to install the ntop-repo
BuildArch:	noarch

Group:		System Environment/Daemons
License:	ISC
URL:		http://www.ntop.org/

#Requires:	epel-release

%description
Package to install the repository of the ntopng service.


%prep


%build


%install
mkdir -p %{buildroot}/etc/yum.repos.d/
cat > %{buildroot}/etc/yum.repos.d/ntop.repo << __endRepo
[ntop]
name=ntop CentOS repository
baseurl=http://packages.ntop.org/centos/7/\$basearch/
enabled=1
gpgcheck=0
__endRepo


%files
/etc/yum.repos.d/ntop.repo


%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Created package
