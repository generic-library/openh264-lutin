#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools


def get_type():
	return "LIBRARY"

def get_desc():
	return "Open H264 library"

def get_licence():
	return "BSD-2"

def get_maintainer():
	return ["HaiboZhu <haibozhu@cisco.com>"]

def get_version():
	return [1,6,0]

def configure(target, my_module):
	my_module.add_depend([
	    'openh264-encoder',
	    'openh264-decoder',
	    'openh264-processing'
	    ])
	return True


