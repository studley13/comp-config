Name:		skype-repo
Version:	1.0
Release:	1.multi
Summary:	Package to install the Skype repo
BuildArch:	noarch

Group:		Applications/Internet
License:	ISC
URL:		http://www.skype.com/

BuildRequires:	curl

%description
Package to install the repository of Skype IM client.


%prep


%build


%install
mkdir -p %{buildroot}/etc/yum.repos.d/
curl -Ls https://repo.skype.com/data/skype-stable.repo > %{buildroot}/etc/yum.repos.d/skype-stable.repo


%files
/etc/yum.repos.d/*


%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Created package
