Name:		curtis-tools
Version:	1.6.5
Release:	1.multi
Summary:	Meta-package for installing Custom tools

Group:		Applications/Multimedia
License:	ISC
BuildArch:	noarch

Requires:	curtis-repos
Requires:	android-tools
Requires:	nmap
Requires:	httpd php fcgi mod_fcgid mod_h264_streaming
Requires:	aspell aspell-en
Requires:	avahi
Requires:	bash zsh bash-completion tmux tree screen
Requires:	bind-utils
Requires:	bindfs fuse-sshfs ftp f3
Requires:	nfs-utils
Requires:	binwalk
Requires:	bzip2 gzip zip unzip unrar tar
Requires: 	python-devel python3-devel automake
Requires:	gcc gcc-c++ kernel-devel cmake
Requires:	clang llvm lldb python-lldb
Requires:	rust cargo
Requires:	java-1.8.0-openjdk
Requires:	wget curl
Requires:	docker
Requires:	fsarchiver
Requires:	genisoimage
Requires:	haskell-platform
Requires:	dhex
Requires:	ghostscript
Requires:	git tig hub
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
Requires:	python-pypng python2-rjsmin
Requires:	python2-jinja2 PyYAML
Requires:	redis hiredis
Requires:	rsync
Requires:	socat nc6 telnet
Requires:	tcpdump 
Requires:	traceroute whois
Requires:	vagrant libvirt vagrant-libvirt
Requires:	VirtualBox kmod-VirtualBox
Requires:	dkms kernel-devel kernel-headers
Requires:	xclip
Requires:	duplicity
Requires:	powerline ctags vim-powerline powerline-fonts tmux-powerline
Requires:	irssi bitlbee
Requires:	snownews
Requires:	mailx
Requires:	youtube-dl
Requires:	wkhtmltopdf
Requires:	pv
Requires:	exfat-utils fuse-exfat
Requires:	pdfgrep

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
