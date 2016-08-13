Name:		curtis-server
Version:	1.0
Release:	1%{?dist}
Summary:	Meta-package for installing server software

Group:		Applications/System
License:	ISC
BuildArch:	noarch

#Requires:	rpmfusion-free-release
#Requires:	rpmfusion-nonfree-release
#Requires:	plexmediaserver
Requires:	opensmtpd
Requires:	transmisssion transmission-daemon transmission-common
Requires:	httpd php fcgi mod_fcgi mod_h264_streaming
Requires:	openssh-server
Requires:	dhcp-server
Requires:	bind
Requires:	nfs-utils
Requires:	docker
Requires:	java-1.8.0-openjdk
#Requires:	ntopng
Requires:	redis hiredis
Requires:	ntp ntpdate
Requires:	rsync

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
