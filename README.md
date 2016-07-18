# comp-config
Python based config and install tool to speed up installing new systems

# Plan

This tool will use a JSON file to record the payloads that it can unload
onto a machine.

Each payload will have a list of targets (empty for all or individual
hostnames) that the payload will unload onto.

The payload may consist of:
* PPAs to install w/ packages to install from ppa
* packages to install from apt
* scripts to run from scripts directory
* files to copy from static directy (backing up existing files)
* tars to unpack over root from static directory
* Files to use to download packages from websites
