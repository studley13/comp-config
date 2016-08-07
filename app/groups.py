#!/usr/bin/env python

from types import *

class Prereq:

    def __init__(self, config):
        self.__config = config
        self.__format = None
        pass

    def __getConfig(self):
        return self.__config

    def __setArguments(self, argumentFormat):
        self.__format = argumentFormat

    def isMet(self):
        """Return if current machine meets prerequisite"""
        pass

    def fromObject(self, data):
        """Load a prerequisite from a python object"""
        pass

    def asObject(self):
        """Return the prequisite as a python object"""

    def fromArguments(self, data):
        """Set the prerequisite as based on an array of strings"""

    def argumentFormat(self):
        """
        Return an array describing the arguments used to set the
        prerequisite.

        [("name", "description")[
        """
        return self.__format

    # Some type checking
    def expect(self, data, dataType, obj, objFn, argName):
        if type(data) != dataType:
            raise RuntimeError("<{}.{}> expects argument `{}` of type `{}`. Got {}.".format(
                obj.__class__.__name__, objFn.__name__, argName, dataType,
                repr(data)))
        return data

    def expectLength(self, data, dataLength, obj, objFn, argName):
        if len(data) != dataLength:
            raise RuntimeError("<{}.{}> expects argument `{}` of length `{}`. Got {}.".format(
                obj.__class__.__name__, objFn.__name__, argName, dataLength,
                repr(data)))
        return data

class HostnamePrereq(Prereq):

    def __init__(self, config):
        Prereq.__init__(self, config)
        Prereq.__setArguments(self, [
            ("hostname", "name of host to match")
        ])
        self.__host = None

    def isMet(self):
        # Determine exact hostname match
        pass

    def fromObject(self, data):
        # Uses a string to determine
        hostname = Prereq.expect(data, StringType, self, self.fromObject, "data")
        self.__host = self._Prereq__config.getNameHost(hostname)

    def asObject(self):
        # return the string of the hostname
        return self.__host.name()

    def fromArguments(self, data):
        # Accepts a single string
        self.fromObject(Prereq.expect(
            data, 1, self, self.fromArguments, "data")[0])

class HostnamePcrePrereq(Prereq):

    def __init__(self, config):
        Prereq.__init__(self, config)
        Prereq.__setArguments(self, [
            ("pcre_regex_pattern", "PCRE pattern to check for match with hostname")
        ])
        self.__pcre = None

    def isMet(self):
        # Determine in hostname matches syntax
        pass

    def fromObject(self, data):
        # uses a string to determine
        self.__pcre = Prereq.expect(data, StringType, self, self.fromObject, "data")

    def asObject(self):
        return self.__pcre

    def fromArguments(self, data)
        # Accepts a single string
        self.fromObject(Prereq.expect(
            data, 1, self, self.fromArguments, "data")[0])

class MachinePrereq(Prereq):

    def __init__(self, config):
        Prereq.__init__(self, config)
        Prereq.__setArguments(self, [
            ("machine", "machine type as reported by `uname -m`")
        ])
        self.__machine = None

    def isMet(self):
        # Determine if machine type is a match
        pass

    def fromObject(self, data):
        # just uses a string
        self.__machine = Prereq.expect(data, StringType, self, self.fromObject, "data")

    def asObject(self):
        return self.__machine

    def fromArguments(self, data)
        # Accepts a single string
        self.fromObject(Prereq.expect(
            data, 1, self, self.fromArguments, "data")[0])

class SystemPrereq(Prereq):

    def __init__(self, config):
        Prereq.__init__(self, config)
        Prereq.__setArguments(self, [
            ("system", "operating system identifier")
        ])
        self.__system = None

    def isMet(self):
        # Determine if any IPs match
        pass

    def fromObject(self, data):
        # Just uses a string
        self.__system = Prereq.expect(data, StringType, self, self.fromObject, "data")

    def asObject(self):
        return self.__system

    def fromArguments(self, data)
        # Accepts a single string
        self.fromObject(Prereq.expect(
            data, 1, self, self.fromArguments, "data")[0])

class IpPrereq(Prereq):

    def __init__(self, config):
        Prereq.__init__(self, config)
        Prereq.__setArguments(self, [
            ("ip/subnet", "ip as x.x.x.x or subnet as x.x.x.x/n")
        ])
        self.__address = None
        self.__size = None

    def isMet(self):
        # Determine if any matching IPs are on the system
        pass

    def fromObject(self, data):
        # Expects dict with "address" in 4 parts and "size"
        if "address" in data and len(data["address"]) == 4:
            self.__address = [int(octet) % 256 for octet in data["address"]]
            if "size" in data:
                self.__size = int(data["size"]) % 33
        else:
            raise RuntimeError("""<{}.{} expects object of format
{\"address\" : [int, int, int, int]} or
{\"address\" : [int, int, int, int], "size" : int}.
Got {}.""".format(self.__class__.__name__, self.fromObject.__name__, repr(data)))

    def asObject(self):
        data = {}
        data["address"] = self.__address
        if self.__size != None:
            data["size"] = self.__size
        return data

    def fromArguments(self, data):
        data = Prereq.expect(
            data, 1, self, self.fromArguments, "data")[0])

        if "/" in data:
            ipData, sizeData = data.split("/")
        else:
            ipData = data
            sizeData = None

        ipData = ipData.split(".")
        if len(ipData) != 4:
            raise RuntimeError("IP address must be of format x.x.x.x. Got {}.".format(
                ".".join(ipData)))
        self.__address = [int(octet) % 256 for octet in ipData]

        if sizeData != None:
            self.__size = int(sizeData) % 33

class MacPrereq(Prereq):


    def __init__(self, config)
        Prereq.__init__(self, config)
        Prereq.__setArguments(self, [
            ("mac-address", "MAC address as XX:XX:XX or XX:XX:XX:XX:XX:XX")
        ])
        self.__address = None

        self.HEX_CHARS = ["{:x}".format(n) for n in xrange(16)]

    def isMet(self):
        # Determine if any MAC addresses on the system are matched
        pass

    def fromObject(self, data):
        # Expects array of 3 or 6 ints
        if len(data) == 3 or len(data) == 6:
            self.__address = [int(octet) % 256 for octet in data]
        else:
            raise RuntimeError("""<{}.{} expects object of format
[int, int, int] or [int, int, int, int, int, int]. Got {}.""".format(
                self.__class__.__name__, self.fromObject.__name__, repr(data)))

    def asObject(self):
        return self.__address

    def fromArguments(self, data):
        data = Prereq.expect(
            data, 1, self, self.fromArguments, "data")[0])

        data = data.lower()

        macData = ""

        for char in list(data):
            if char in self.HEX_CHARS:
                macData += char

        if len(macData) != 6 and len(macData) != 12:
            raise RuntimeError("MAC address must be of format xx:xx:xx or xx:xx:xx:xx:xx:xx Got {}.".format(".".join(ipData)))




class Group:

    def __init__(self, config):
        self.__config = config
        pass

    def fromObject(self, data):
        pass

    def asObject(self):
        pass
