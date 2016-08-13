
S=./scripts

all:	rpm-fusion ubuntu-font font-awesome

clean:
	rm -rf rpm

rpm-fusion:	$S/get-rpm-fusion
	$S/get-rpm-fusion

ubuntu-font:	$S/build-ubuntu-font
	$S/build-ubuntu-font

font-awesome:	$S/build-font-awesome
	$S/build-font-awesome
