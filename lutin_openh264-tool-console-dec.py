#!/usr/bin/python
import realog.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "BINARY"

def get_sub_type():
	return "TEST"

def get_desc():
	return "Open H264 tool"

def get_licence():
	return "BSD-2"

def get_maintainer():
	return ["HaiboZhu <haibozhu@cisco.com>"]


def configure(target, my_module):
	my_module.add_src_file([
	    'openh264/codec/console/dec/src/h264dec.cpp',
	    'openh264/codec/console/dec/src/d3d9_utils.cpp',
	    'openh264/codec/console/common/src/read_config.cpp'
	    ])
	my_module.add_path("openh264/codec/console/dec/inc")
	my_module.add_path("openh264/codec/console/common/inc")
	my_module.compile_version("c++", 2003)
	my_module.add_depend('openh264')
	return True
