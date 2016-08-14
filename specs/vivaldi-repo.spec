Name:		vivaldi-repo
Version:	1.0
Release:	1.multi
Summary:	Package to install the vivaldi repo
BuildArch:	noarch

Group:		Applications/Internet
License:	ISC
URL:		http://vivaldi.com/

%description
Package to install the repository of vivaldi.


%prep


%build


%install
mkdir -p %{buildroot}/etc/yum.repos.d/
cat > %{buildroot}/etc/yum.repos.d/vivaldi.repo << __endRepo
[vivaldi]
name=Vivaldi repository
baseurl=http://repo.vivaldi.com/stable/rpm/\$basearch/
enabled=1
gpgcheck=1
gpgkey=http://repo.vivaldi.com/stable/linux_signing_key.pub
__endRepo


%files
/etc/yum.repos.d/vivaldi.repo


%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Created package
