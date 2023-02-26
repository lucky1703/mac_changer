#!/usr/bin/env python
import subprocess
import optparse
import re


def call(interface, mac):
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)


def parse():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="mac", help="MAC address you want to change to")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please spacify an interface.--help for more info")
    elif not options.mac:
        parser.error("Please spacify a mac address.--help for more info")
    return options


# main
options = parse()
call(options.interface, options.mac)
ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
result_mac = re.findall(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
if result_mac[0] == options.mac:
    print("Mac Address changed sucessfully")
else:
    print("Could not read MAC address")
