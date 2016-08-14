Name:		google-chrome-repo
Version:	1.0
Release:	1.multi
Summary:	Package to install the google-chrome repo
BuildArch:	noarch

Group:		Applications/Internet
License:	ISC
URL:		http://www.google.com/chrome

%description
Package to install the repository of google-chrome.


%prep


%build


%install
mkdir -p %{buildroot}/etc/yum.repos.d/
cat > %{buildroot}/etc/yum.repos.d/google-chrome.repo << __endRepo
[google]
name=Google Chrome repository
baseurl=http://dl.google.com/linux/chrome/rpm/stable/\$basearch/
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
__endRepo


%files
/etc/yum.repos.d/google-chrome.repo


%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Created package
