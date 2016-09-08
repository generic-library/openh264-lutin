#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools


def get_type():
	return "LIBRARY"

def get_desc():
	return "Open H264 processing library"

def get_licence():
	return "BSD-2"

def get_maintainer():
	return ["HaiboZhu <haibozhu@cisco.com>"]

def get_version():
	return [1,6,0]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
	    'openh264/codec/processing/src/adaptivequantization/AdaptiveQuantization.cpp',
	    'openh264/codec/processing/src/vaacalc/vaacalcfuncs.cpp',
	    'openh264/codec/processing/src/vaacalc/vaacalculation.cpp',
	    'openh264/codec/processing/src/imagerotate/imagerotate.cpp',
	    'openh264/codec/processing/src/imagerotate/imagerotatefuncs.cpp',
	    'openh264/codec/processing/src/backgrounddetection/BackgroundDetection.cpp',
	    'openh264/codec/processing/src/denoise/denoise_filter.cpp',
	    'openh264/codec/processing/src/denoise/denoise.cpp',
	    'openh264/codec/processing/src/scenechangedetection/SceneChangeDetection.cpp',
	    'openh264/codec/processing/src/common/WelsFrameWork.cpp',
	    'openh264/codec/processing/src/common/WelsFrameWorkEx.cpp',
	    'openh264/codec/processing/src/common/memory.cpp',
	    'openh264/codec/processing/src/downsample/downsamplefuncs.cpp',
	    'openh264/codec/processing/src/downsample/downsample.cpp',
	    'openh264/codec/processing/src/scrolldetection/ScrollDetectionFuncs.cpp',
	    'openh264/codec/processing/src/scrolldetection/ScrollDetection.cpp',
	    'openh264/codec/processing/src/complexityanalysis/ComplexityAnalysis.cpp',
		])
	if target.config["arch"] == "arm":
		if target.config["bus-size"] == "64":
			my_module.add_src_file([
			    'openh264/codec/processing/src/arm64/pixel_sad_aarch64_neon.S',
			    'openh264/codec/processing/src/arm64/down_sample_aarch64_neon.S',
			    'openh264/codec/processing/src/arm64/vaa_calc_aarch64_neon.S',
			    'openh264/codec/processing/src/arm64/adaptive_quantization_aarch64_neon.S',
			    ])
		else:
			my_module.add_src_file([
			    'openh264/codec/processing/src/arm/pixel_sad_neon.S',
			    'openh264/codec/processing/src/arm/down_sample_neon.S',
			    'openh264/codec/processing/src/arm/adaptive_quantization.S',
			    'openh264/codec/processing/src/arm/vaa_calc_neon.S',
			    ])

	my_module.add_header_file([
	    'openh264/codec/processing/src/adaptivequantization/AdaptiveQuantization.h',
	    'openh264/codec/processing/src/vaacalc/vaacalculation.h',
	    'openh264/codec/processing/src/imagerotate/imagerotate.h',
	    'openh264/codec/processing/src/backgrounddetection/BackgroundDetection.h',
	    'openh264/codec/processing/src/denoise/denoise.h',
	    'openh264/codec/processing/src/scenechangedetection/SceneChangeDetection.h',
	    'openh264/codec/processing/src/common/WelsFrameWork.h',
	    'openh264/codec/processing/src/common/resource.h',
	    'openh264/codec/processing/src/common/common.h',
	    'openh264/codec/processing/src/common/util.h',
	    'openh264/codec/processing/src/common/typedef.h',
	    'openh264/codec/processing/src/common/memory.h',
	    'openh264/codec/processing/src/downsample/downsample.h',
	    'openh264/codec/processing/src/scrolldetection/ScrollDetectionFuncs.h',
	    'openh264/codec/processing/src/scrolldetection/ScrollDetection.h',
	    'openh264/codec/processing/src/complexityanalysis/ComplexityAnalysis.h',
	    'openh264/codec/processing/interface/IWelsVP.h',

		],
		destination_path="")
	my_module.compile_version("C++", 2003)
	my_module.add_depend([
	    'openh264-common'
	    ])
	return my_module
