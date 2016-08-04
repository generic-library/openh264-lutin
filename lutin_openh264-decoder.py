#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools


def get_type():
	return "LIBRARY"

def get_desc():
	return "Open H264 decoder library"

def get_licence():
	return "BSD-2"

def get_maintainer():
	return ["HaiboZhu <haibozhu@cisco.com>"]

def get_version():
	return [1,6,0]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
	    'openh264/codec/decoder/core/src/decoder.cpp',
	    'openh264/codec/decoder/core/src/cabac_decoder.cpp',
	    'openh264/codec/decoder/core/src/parse_mb_syn_cabac.cpp',
	    'openh264/codec/decoder/core/src/pic_queue.cpp',
	    'openh264/codec/decoder/core/src/rec_mb.cpp',
	    'openh264/codec/decoder/core/src/manage_dec_ref.cpp',
	    'openh264/codec/decoder/core/src/decoder_core.cpp',
	    'openh264/codec/decoder/core/src/decode_mb_aux.cpp',
	    'openh264/codec/decoder/core/src/error_concealment.cpp',
	    'openh264/codec/decoder/core/src/mv_pred.cpp',
	    'openh264/codec/decoder/core/src/deblocking.cpp',
	    'openh264/codec/decoder/core/src/decoder_data_tables.cpp',
	    'openh264/codec/decoder/core/src/bit_stream.cpp',
	    'openh264/codec/decoder/core/src/parse_mb_syn_cavlc.cpp',
	    'openh264/codec/decoder/core/src/au_parser.cpp',
	    'openh264/codec/decoder/core/src/fmo.cpp',
	    'openh264/codec/decoder/core/src/memmgr_nal_unit.cpp',
	    'openh264/codec/decoder/core/src/decode_slice.cpp',
	    'openh264/codec/decoder/core/src/get_intra_predictor.cpp',
	    'openh264/codec/decoder/plus/src/welsDecoderExt.cpp',
		])
	if target.config["arch"] == "arm":
		if target.config["bus-size"] == "64":
			my_module.add_src_file([
			    'openh264/codec/decoder/core/arm64/intra_pred_aarch64_neon.S',
			    'openh264/codec/decoder/core/arm64/block_add_aarch64_neon.S',
			    ])
		else:
			my_module.add_src_file([
			    'openh264/codec/decoder/core/arm/intra_pred_neon.S',
			    'openh264/codec/decoder/core/arm/block_add_neon.S',
			    ])

	my_module.add_header_file([
	    'openh264/codec/decoder/core/inc/decoder.h',
	    'openh264/codec/decoder/core/inc/error_concealment.h',
	    'openh264/codec/decoder/core/inc/decode_slice.h',
	    'openh264/codec/decoder/core/inc/cabac_decoder.h',
	    'openh264/codec/decoder/core/inc/mb_cache.h',
	    'openh264/codec/decoder/core/inc/dec_golomb.h',
	    'openh264/codec/decoder/core/inc/get_intra_predictor.h',
	    'openh264/codec/decoder/core/inc/pic_queue.h',
	    'openh264/codec/decoder/core/inc/bit_stream.h',
	    'openh264/codec/decoder/core/inc/rec_mb.h',
	    'openh264/codec/decoder/core/inc/vlc_decoder.h',
	    'openh264/codec/decoder/core/inc/au_parser.h',
	    'openh264/codec/decoder/core/inc/deblocking.h',
	    'openh264/codec/decoder/core/inc/decoder_context.h',
	    'openh264/codec/decoder/core/inc/dec_frame.h',
	    'openh264/codec/decoder/core/inc/slice.h',
	    'openh264/codec/decoder/core/inc/fmo.h',
	    'openh264/codec/decoder/core/inc/manage_dec_ref.h',
	    'openh264/codec/decoder/core/inc/parse_mb_syn_cavlc.h',
	    'openh264/codec/decoder/core/inc/parameter_sets.h',
	    'openh264/codec/decoder/core/inc/error_code.h',
	    'openh264/codec/decoder/core/inc/mv_pred.h',
	    'openh264/codec/decoder/core/inc/wels_const.h',
	    'openh264/codec/decoder/core/inc/parse_mb_syn_cabac.h',
	    'openh264/codec/decoder/core/inc/nalu.h',
	    'openh264/codec/decoder/core/inc/decoder_core.h',
	    'openh264/codec/decoder/core/inc/memmgr_nal_unit.h',
	    'openh264/codec/decoder/core/inc/wels_common_basis.h',
	    'openh264/codec/decoder/core/inc/picture.h',
	    'openh264/codec/decoder/core/inc/decode_mb_aux.h',
	    'openh264/codec/decoder/core/inc/nal_prefix.h',
	    'openh264/codec/decoder/plus/inc/welsDecoderExt.h',

		],
		destination_path="")
	my_module.compile_version("C++", 2003)
	my_module.add_module_depend([
	    'openh264-common',
	    'openh264-processing'
	    ])
	return my_module
