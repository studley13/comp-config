Name:		curtis-tools
Version:	1.0
Release:	1.multi
Summary:	Meta-package for installing Custom tools

Group:		Applications/Multimedia
License:	ISC
BuildArch:	noarch

Requires:	curtis-repos
Requires:	android-tools
Requires:	httpd php fcgi mod_fcgid mod_h264_streaming
Requires:	aspell
Requires:	avahi
Requires:	bash zsh bash-completion tmux tree
Requires:	bind-utils
Requires:	bindfs fuse-sshfs ftp
Requires:	nfs-utils
Requires:	binwalk
Requires:	bzip2 gzip zip unzip unrar tar
Requires:	clang llvm
Requires:	rustc
Requires:	java-1.8.0-openjdk
Requires:	wget curl
Requires:	docker
Requires:	fsarchiver
Requires:	genisoimage
Requires:	haskell-platform
Requires:	dhex
Requires:	ghostscript
Requires:	git
Requires:	gnupg gnupg2
Requires:	gnuplot gnuplot-wx
Requires:	htop
Requires:	lm_sensors
Requires:	lua
Requires:	m4
Requires:	make
Requires:	vim nano
Requires:	mutt
Requires:	NetworkManager-ssh NetworkManager-openvpn NetworkManager-openconnect openconnect openvpn
Requires:	ntpdate
Requires:	openssh-server openssh-clients openssh
Requires:	partimage
Requires:	qphotorec
Requires:	protobuf protobuf-c protobuf-vim protobuf-java protobuf-python
Requires:	python-cryptominisat4
Requires:	python2-markdown2 python-beautifulsoup4
Requires:	redis hiredis
Requires:	rsync
Requires:	socat nc6 telnet
Requires:	tcpdump 
Requires:	traceroute whois
Requires:	vagrant
Requires:	VirtualBox
Requires:	xclip
Requires:	duplicity
Requires:	powerline ctags
Requires:	irssi bitlbee
Requires:	snownews

%description
Standard command line tools

%prep

%build

%clean

%install

%files

%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Created initial package
