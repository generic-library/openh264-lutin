#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools


def get_type():
	return "LIBRARY"

def get_desc():
	return "Open H264 common library"

def get_licence():
	return "BSD-2"

def get_maintainer():
	return ["HaiboZhu <haibozhu@cisco.com>"]

def get_version():
	return [1,6,0]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
	    'openh264/codec/common/src/welsCodecTrace.cpp',
	    'openh264/codec/common/src/sad_common.cpp',
	    'openh264/codec/common/src/cpu.cpp',
	    'openh264/codec/common/src/intra_pred_common.cpp',
	    'openh264/codec/common/src/expand_pic.cpp',
	    'openh264/codec/common/src/deblocking_common.cpp',
	    'openh264/codec/common/src/WelsThreadLib.cpp',
	    'openh264/codec/common/src/WelsThreadPool.cpp',
	    'openh264/codec/common/src/common_tables.cpp',
	    'openh264/codec/common/src/memory_align.cpp',
	    'openh264/codec/common/src/utils.cpp',
	    'openh264/codec/common/src/copy_mb.cpp',
	    'openh264/codec/common/src/WelsThread.cpp',
	    'openh264/codec/common/src/WelsTaskThread.cpp',
	    'openh264/codec/common/src/mc.cpp',
	    'openh264/codec/common/src/crt_util_safe_x.cpp',
		])
	if target.config["arch"] == "arm":
		if target.config["bus-size"] == "64":
			my_module.add_src_file([
			    'openh264/codec/common/arm64/arm_arch64_common_macro.S',
			    'openh264/codec/common/arm64/expand_picture_aarch64_neon.S',
			    'openh264/codec/common/arm64/copy_mb_aarch64_neon.S',
			    'openh264/codec/common/arm64/mc_aarch64_neon.S',
			    'openh264/codec/common/arm64/deblocking_aarch64_neon.S',
			    'openh264/codec/common/arm64/intra_pred_common_aarch64_neon.S',
			    ])
		else:
			my_module.add_src_file([
			    'openh264/codec/common/arm/copy_mb_neon.S',
			    'openh264/codec/common/arm/intra_pred_common_neon.S',
			    'openh264/codec/common/arm/expand_picture_neon.S',
			    'openh264/codec/common/arm/arm_arch_common_macro.S',
			    'openh264/codec/common/arm/deblocking_neon.S',
			    'openh264/codec/common/arm/mc_neon.S',
			    ])

	my_module.add_header_file([
	    'openh264/codec/common/inc/welsCodecTrace.h',
	    'openh264/codec/common/inc/WelsList.h',
	    'openh264/codec/common/inc/WelsCircleQueue.h',
	    'openh264/codec/common/inc/WelsThread.h',
	    'openh264/codec/common/inc/macros.h',
	    'openh264/codec/common/inc/WelsTask.h',
	    'openh264/codec/common/inc/cpu_core.h',
	    'openh264/codec/common/inc/WelsThreadPool.h',
	    'openh264/codec/common/inc/crt_util_safe_x.h',
	    'openh264/codec/common/inc/wels_const_common.h',
	    'openh264/codec/common/inc/ls_defines.h',
	    'openh264/codec/common/inc/golomb_common.h',
	    'openh264/codec/common/inc/WelsTaskThread.h',
	    'openh264/codec/common/inc/wels_common_defs.h',
	    'openh264/codec/common/inc/measure_time.h',
	    'openh264/codec/common/inc/expand_pic.h',
	    'openh264/codec/common/inc/version.h',
	    'openh264/codec/common/inc/deblocking_common.h',
	    'openh264/codec/common/inc/copy_mb.h',
	    'openh264/codec/common/inc/memory_align.h',
	    'openh264/codec/common/inc/utils.h',
	    'openh264/codec/common/inc/WelsThreadLib.h',
	    'openh264/codec/common/inc/mc.h',
	    'openh264/codec/common/inc/intra_pred_common.h',
	    'openh264/codec/common/inc/sad_common.h',
	    'openh264/codec/common/inc/typedefs.h',
	    'openh264/codec/common/inc/WelsLock.h',
	    'openh264/codec/common/inc/cpu.h',
		],
		destination_path="")
		
	my_module.add_header_file([
	    'openh264/codec/api/svc/codec_app_def.h',
	    'openh264/codec/api/svc/codec_api.h',
	    'openh264/codec/api/svc/codec_def.h',
	    'openh264/codec/api/svc/codec_ver.h',
		],
		destination_path="")
	my_module.add_module_depend([
	    'cxx'
	    ])
	my_module.compile_version("C++", 2003)
	my_module.add_module_depend([
		    'cxx',
		    'pthread',
		    'm'
		    ])
	return my_module
