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

# Config Utility

This is a python utility that you can use to add payloads to your
configuration file.

It allows you to create groups based on:
 * hostname
 * architecture
 * IPv4 address / subnet
 * MAC address

It allows you to create payloads by:
 * Selecting scripts from the scripts directory
 * Selecting tars to unpack from the static directory
 * Select files to replace from the static directory
 * Select packages to install from PPAs (based on distro config
   tool is being run on)
 * Select packages known by apt-cache (based on distro config is
   being run on)

It also allows you bundle the final python binday

Works as its own shell

# Config JSON File

This file records all of the payloads and groups that the setup tool
will work on.

The root element is an object with the form:

~~~ .lang-js
{
    "groups" : {
        "group-name" : Group()
    },
    "payloads: [
        Payload(),
    ]
}
~~~

## Groups

Each group will have a combination of different rules. Some rules act to
include a host in a group, in that _any_ matching member will be considered
part of the group. Other rules will act to restrict group membership, in
that _only_ matching hosts will be considered part of the group.

A group appears as an object with one or more of the following keys:

 * `"hostname"`
 * `"hostname-pcre"`
 * `"machine"`
 * `"system"`
 * `"ipv4"`
 * `"mac"`
 * `"group"`

### Matching Exact Hostnames

The `"hostname"` key will always refer to an array of string values. Each
string will be an exact hostname value. A machine with a short hostname
or fully qualified hostname matching that value will have any associated
payloads installed.

_Any_ matching hosts get group membership.

Example:

~~~ .lang-js
{
    "hostname" : [
        "example2",
        "example1.example.com"
    ]
}
~~~

This group would match both `example1.example.com` and `example2.example.com`
as well as `example2.local` but not `example3.example.com`.

### Matching Hostname Patterns with PCRE

The `"hostname-pcre"` key will always refer to an array of string values.
Each sting will be a PCRE pattern. Any hostname that matches the pattern
will have associated payloads installed.

_Any_ matching hosts get group membership.

### Matching Architectures

The `"machine"` key will always refer to an array of string values. Each will
be an architecture identifier as returned by the command `uname -m`.

A host _must_ match this rule to get group membership.

### Matching Operating Systems

The `"system"` key will always refer to an array of string values. Each
will be a system name as reported by `uname -s`.

A host _must_ match this rule to get group membership.

### Matching by IPv4 address

The `"ipv4"` key will always refer to an array of objects. Each object
will have a the key `"address"`, which will refer to an array of four
numbers (>= 0, < 256), identifying the four octets of either a specific 
IP address or of the identifying address of a particular subnet. Each
object may optionally have a `"size"` key which will refer to a single 
number (>= 0, <= 32), identfying the size of the subnet portion of the
address space.

Any address matching exactly the address specified, where no size is
specified, will consititue a match. Any address with the same bits
in the subnet portion of the address will also constitute a match.

_Any_ matching hosts get group membership.

### Matching by MAC Address

The `"mac"` key will always refer to an array of arrays. Each array
will either have three numbers referring to the first 3 octets of a 
mac address, or the vendor part, or will have 6 numbers, referring
to a specific address.

Any MAC address with the same octets in the vendor portion as an array
that only specifies vendor parts will constitute a match. An address
that exactly matches the octets present in an array with all 6 octets
present will also be considered a match.

_Any_ matching hosts get group membership.

### Matching by Group Membership

The `"group"` key will always refer to an array of strings. Each string
will refer to the name of another group. Any member of that group
will be considered a match.

_Any_ matching hosts get group membership.
