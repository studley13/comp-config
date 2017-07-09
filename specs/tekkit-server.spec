Name:		tekkit-server
Version:	1.2.9
Release:	1.multi
Summary:	Server for Tekkit modpack for Minecraft

Group:		Games
License:	GPLv3
URL:		https://www.technicpack.net/modpack/tekkitmain.552547

BuildRequires:  git make
Requires(pre):  shadow-utils
Requires(post): systemd
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

%pre
getent group tekkit >/dev/null || groupadd -r tekkit
getent passwd tekkit >/dev/null || \
    useradd -r -g tekkit -d "/var/${name}" -s /sbin/nologin \
    -c "Tekkit server" tekkit
exit 0

%install
# Copy Files
mkdir -p  "%{buildroot}/var/"
cp -rv %{name} "%{buildroot}/var/%{name}"
rm -rf %{buildroot}/var/%{name}/.{git,gitignore}

# Copy service and reload
mkdir -p "%{buildroot}/etc/systemd/system"
cp %{name}/tekkit.service "%{buildroot}/etc/systemd/system/tekkit.service"

%post
systemctl daemon-reload

%files
%defattr(0600, tekkit, tekkit)
%attr(0700, tekkit, tekkit) /var/%{name}/tekkit
/var/%{name}/
%attr(0644, root, root) /etc/systemd/system/tekkit.service

%changelog
* Sat Aug 13 2016 Curtis Millar <rpm@curtism.me> - 1.0
- Made the initial repo
