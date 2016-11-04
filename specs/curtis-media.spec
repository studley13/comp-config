Name:		curtis-media
Version:	1.2.1
Release:	1.multi
Summary:	Meta-package for installing media software and codecs

Group:		Applications/Multimedia
License:	ISC
BuildArch:	noarch

Requires:	curtis-repos

# Codecs
Requires:	gstreamer gstreamer-tools
Requires:	gstreamer-plugins-base
Requires:	gstreamer-plugins-good
Requires:	gstreamer-plugins-bad
Requires:	gstreamer-plugins-ugly
Requires:	gstreamer1-libav
Requires:	gstreamer1-vaapi
Requires:	libva-utils
Requires:	lame lame-libs
Requires:	libogg
Requires:	libvorbis libvpx opus
Requires:	libquicktime libquicktime-utils
Requires:	x264 x264-libs
Requires:	x265 x265-libs
Requires:	libtheora
Requires:	libaacs-utils libaacs
Requires:	faad2 faac
Requires:	flac flac-libs

# Tools
Requires:	ImageMagick
Requires:	vlc vlc-plugin-jack
Requires:	ffmpeg >= 3.1.2-1.fc24.custom, ffmpeg-libs >= 3.1.2-1.fc24.custom, libavdevice >= 3.1.2-1.fc24.custom
Requires:	easytag
Requires:	mpv

%description
Software and codecs for audio and video

%prep

%build

%clean

%install

%files

%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Created initial package
