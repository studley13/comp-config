
S=./scripts

RPM_HOME=/home/makerpm

META_SPECS=specs/curtis-av.spec specs/curtis-desk.spec specs/curtis-games.spec\
	specs/curtis-host-black.spec specs/curtis-host-blue.spec\
	specs/curtis-host-core.spec specs/curtis-host-monolith.spec\
	specs/curtis-host-silver.spec specs/curtis-media.spec\
	specs/curtis-repos.spec specs/curtis-server.spec\
	specs/curtis-tools.spec  

PRE_BINARY_SPECS=specs/rust.spec
PRE32_BINARY_SPECS=specs/rust-32.spec
BINARY_SPECS=specs/i3blocks.spec specs/playerctl.spec
BINARY64_SPECS=specs/ffmpeg.spec

REPO_SPECS=specs/handbrake-repo.spec specs/google-chrome-repo.spec\
	specs/ntop-repo.spec specs/skype-repo.spec specs/vivaldi-repo.spec

all:	update

initial: rpm-fusion repo-specs update binary-specs repodata

update:	ubuntu-font font-awesome plex meta-specs repodata

clean:
	rm -rf rpm

rpm-user:	$(RPM_HOME)

$(RPM_HOME):	$S/rpm-user
	$S/rpm-user

rpm-fusion:	$S/get-rpm-fusion
	$S/get-rpm-fusion

plex:		$S/get-plex
	$S/get-plex

ubuntu-font:	$S/build-ubuntu-font $(RPM_HOME)
	$S/build-ubuntu-font

font-awesome:	$S/build-font-awesome $(RPM_HOME)
	$S/build-font-awesome

meta-specs:	$S/spec-build $(META_SPECS) $(RPM_HOME)
	$S/spec-build $(META_SPECS)

repo-specs:	$S/spec-build $(REPO_SPECS) $(RPM_HOME)
	$S/spec-build $(REPO_SPECS)

noarch:	ubuntu-font font-awesome meta-specs

binary-specs:	$S/spec-build $(BINARY_SPECS) $(RPM_HOME)
	$S/spec-build -b $(BINARY_SPECS)
	$S/spec-build $(BINARY64_SPECS)
	$S/spec-build $(PRE_BINARY_SPECS)
	$S/spec-build -t i386 $(PRE32_BINARY_SPECS)

repodata:
	$S/createrepo
