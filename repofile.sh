#!/bin/bash
set -e

reponame=$SERVER_NAME

# Headers
cat << __endHeaders
Content-Type: text/plain; charset=utf-8
Content-Disposition: download; filename="${reponame}.repo"

__endHeaders

# Repofile
cat << __endRepo
[$reponame]
name=Curtis's Repository
gpgcheck=0
baseurl=http://${SERVER_NAME}/${CONTENT_PREFIX}/rpms/\$basearch/
enabled=1

[${reponame}-noarch]
name=Curtis's Repository - Noarch
gpgcheck=0
baseurl=http://${SERVER_NAME}/${CONTENT_PREFIX}/rpms/noarch/
enabled=1
__endRepo

#env
