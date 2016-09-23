Name:		curtis-server
Version:	1.1
Release:	1.multi
Summary:	Meta-package for installing server software

Group:		Applications/System
License:	ISC
BuildArch:	noarch

Requires:	ntop-repo
Requires:	mariadb-common mariadb-libs
Requires:	plexmediaserver
Requires:	opensmtpd
Requires:	transmission transmission-daemon transmission-common
Requires:	httpd php fcgi mod_fcgid mod_h264_streaming
Requires:	openssh-server
Requires:	dhcp-server
Requires:	bind
Requires:	nfs-utils
Requires:	docker
Requires:	java-1.8.0-openjdk
Requires:	ntopng
Requires:	redis hiredis
Requires:	ntp ntpdate
Requires:	rsync
Requires:	wol
Requires:	easy-rsa

%description
Server software

%prep

%build

%clean

%install

%files

%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Created initial package
