#!/usr/bin/python
import lutin.module as module
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


def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
	    'openh264/codec/console/enc/src/welsenc.cpp',
	    'openh264/codec/console/common/src/read_config.cpp',
	    ])
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "openh264", "codec", "console", "enc", "inc"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "openh264", "codec", "console", "common", "inc"))
	my_module.compile_version("c++", 2003)
	my_module.add_module_depend('openh264')
	return my_module