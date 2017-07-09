Name:		tekkit-server
Version:	1.2.9
Release:	1.multi
Summary:	Server for Tekkit modpack for Minecraft

Group:		Games
License:	GPLv3
URL:		https://www.technicpack.net/modpack/tekkitmain.552547

BuildRequires: git make
Requires:	java-1.8.0-openjdk systemd

%global _prefix /usr/local

%description
We have Liftoff! Tekkit has launched into a new era, and with it new frontiers
to explore! Dimensions, pockets and planets, it’s all there for you and your
friends to exploit and conquer.

%prep
rm -rf %{name}
git clone http://github.com/studley13/tekkit-server %{name}

%build
cd %{name}
make all

%install
# Add user and group
groupadd -r tekkit
useradd -r -g tekkit -d "/var/%{name}" -s "/bin/sh" tekkit

# Copy Files
mkdir -p "/var/%{name}/"
cp -rv %{name}/* "/var/%{name}/"
chown -R tekkit:tekkit "/var/%{name}"

# Copy service and reload
mkdir -p /etc/systemd/system
cp %{name}/tekkit.service /etc/systemd/system
systemctl daemon-reload

%files
%doc
/var/%{name}/*
/etc/systemd/system/tekkit.service

%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Made the initial repo
