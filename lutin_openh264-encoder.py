#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools


def get_type():
	return "LIBRARY"

def get_desc():
	return "Open H264 encoder library"

def get_licence():
	return "BSD-2"

def get_maintainer():
	return ["HaiboZhu <haibozhu@cisco.com>"]

def get_version():
	return [1,6,0]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
	    'openh264/codec/encoder/core/src/svc_encode_slice.cpp',
	    'openh264/codec/encoder/core/src/svc_enc_slice_segment.cpp',
	    'openh264/codec/encoder/core/src/au_set.cpp',
	    'openh264/codec/encoder/core/src/paraset_strategy.cpp',
	    'openh264/codec/encoder/core/src/encoder_ext.cpp',
	    'openh264/codec/encoder/core/src/ratectl.cpp',
	    'openh264/codec/encoder/core/src/sample.cpp',
	    'openh264/codec/encoder/core/src/picture_handle.cpp',
	    'openh264/codec/encoder/core/src/nal_encap.cpp',
	    'openh264/codec/encoder/core/src/svc_encode_mb.cpp',
	    'openh264/codec/encoder/core/src/svc_set_mb_syn_cavlc.cpp',
	    'openh264/codec/encoder/core/src/wels_task_base.cpp',
	    'openh264/codec/encoder/core/src/svc_set_mb_syn_cabac.cpp',
	    'openh264/codec/encoder/core/src/ref_list_mgr_svc.cpp',
	    'openh264/codec/encoder/core/src/svc_mode_decision.cpp',
	    'openh264/codec/encoder/core/src/decode_mb_aux.cpp',
	    'openh264/codec/encoder/core/src/slice_multi_threading.cpp',
	    'openh264/codec/encoder/core/src/mv_pred.cpp',
	    'openh264/codec/encoder/core/src/deblocking.cpp',
	    'openh264/codec/encoder/core/src/wels_preprocess.cpp',
	    'openh264/codec/encoder/core/src/encoder.cpp',
	    'openh264/codec/encoder/core/src/set_mb_syn_cavlc.cpp',
	    'openh264/codec/encoder/core/src/encoder_data_tables.cpp',
	    'openh264/codec/encoder/core/src/wels_task_encoder.cpp',
	    'openh264/codec/encoder/core/src/wels_task_management.cpp',
	    'openh264/codec/encoder/core/src/encode_mb_aux.cpp',
	    'openh264/codec/encoder/core/src/set_mb_syn_cabac.cpp',
	    'openh264/codec/encoder/core/src/svc_motion_estimate.cpp',
	    'openh264/codec/encoder/core/src/svc_base_layer_md.cpp',
	    'openh264/codec/encoder/core/src/get_intra_predictor.cpp',
	    'openh264/codec/encoder/core/src/md.cpp',
#	    'openh264/codec/encoder/plus/src/DllEntry.cpp',
	    'openh264/codec/encoder/plus/src/welsEncoderExt.cpp',
		])
	if target.config["arch"] == "arm":
		if target.config["bus-size"] == "64":
			my_module.add_src_file([
			    'openh264/codec/encoder/core/arm64/svc_motion_estimation_aarch64_neon.S',
			    'openh264/codec/encoder/core/arm64/reconstruct_aarch64_neon.S',
			    'openh264/codec/encoder/core/arm64/intra_pred_aarch64_neon.S',
			    'openh264/codec/encoder/core/arm64/pixel_aarch64_neon.S',
			    'openh264/codec/encoder/core/arm64/intra_pred_sad_3_opt_aarch64_neon.S',
			    'openh264/codec/encoder/core/arm64/memory_aarch64_neon.S',
			    ])
		else:
			my_module.add_src_file([
			    'openh264/codec/encoder/core/arm/intra_pred_neon.S',
			    'openh264/codec/encoder/core/arm/memory_neon.S',
			    'openh264/codec/encoder/core/arm/svc_motion_estimation.S',
			    'openh264/codec/encoder/core/arm/pixel_neon.S',
			    'openh264/codec/encoder/core/arm/intra_pred_sad_3_opt_neon.S',
			    'openh264/codec/encoder/core/arm/reconstruct_neon.S',
			    ])

	my_module.add_header_file([
	    'openh264/codec/encoder/core/inc/nal_encap.h',
	    'openh264/codec/encoder/core/inc/picture_handle.h',
	    'openh264/codec/encoder/core/inc/svc_motion_estimate.h',
	    'openh264/codec/encoder/core/inc/svc_set_mb_syn_cavlc.h',
	    'openh264/codec/encoder/core/inc/au_set.h',
	    'openh264/codec/encoder/core/inc/svc_encode_slice.h',
	    'openh264/codec/encoder/core/inc/svc_enc_slice_segment.h',
	    'openh264/codec/encoder/core/inc/mb_cache.h',
	    'openh264/codec/encoder/core/inc/wels_task_base.h',
	    'openh264/codec/encoder/core/inc/svc_set_mb_syn.h',
	    'openh264/codec/encoder/core/inc/get_intra_predictor.h',
	    'openh264/codec/encoder/core/inc/extern.h',
	    'openh264/codec/encoder/core/inc/rc.h',
	    'openh264/codec/encoder/core/inc/wels_func_ptr_def.h',
	    'openh264/codec/encoder/core/inc/svc_enc_macroblock.h',
	    'openh264/codec/encoder/core/inc/param_svc.h',
	    'openh264/codec/encoder/core/inc/set_mb_syn_cavlc.h',
	    'openh264/codec/encoder/core/inc/svc_enc_golomb.h',
	    'openh264/codec/encoder/core/inc/stat.h',
	    'openh264/codec/encoder/core/inc/set_mb_syn_cabac.h',
	    'openh264/codec/encoder/core/inc/svc_base_layer_md.h',
	    'openh264/codec/encoder/core/inc/deblocking.h',
	    'openh264/codec/encoder/core/inc/slice.h',
	    'openh264/codec/encoder/core/inc/parameter_sets.h',
	    'openh264/codec/encoder/core/inc/encode_mb_aux.h',
	    'openh264/codec/encoder/core/inc/mv_pred.h',
	    'openh264/codec/encoder/core/inc/wels_const.h',
	    'openh264/codec/encoder/core/inc/wels_task_encoder.h',
	    'openh264/codec/encoder/core/inc/svc_enc_frame.h',
	    'openh264/codec/encoder/core/inc/encoder_context.h',
	    'openh264/codec/encoder/core/inc/svc_encode_mb.h',
	    'openh264/codec/encoder/core/inc/as264_common.h',
	    'openh264/codec/encoder/core/inc/encoder.h',
	    'openh264/codec/encoder/core/inc/wels_preprocess.h',
	    'openh264/codec/encoder/core/inc/md.h',
	    'openh264/codec/encoder/core/inc/slice_multi_threading.h',
	    'openh264/codec/encoder/core/inc/vlc_encoder.h',
	    'openh264/codec/encoder/core/inc/wels_task_management.h',
	    'openh264/codec/encoder/core/inc/wels_common_basis.h',
	    'openh264/codec/encoder/core/inc/sample.h',
	    'openh264/codec/encoder/core/inc/wels_transpose_matrix.h',
	    'openh264/codec/encoder/core/inc/ref_list_mgr_svc.h',
	    'openh264/codec/encoder/core/inc/picture.h',
	    'openh264/codec/encoder/core/inc/decode_mb_aux.h',
	    'openh264/codec/encoder/core/inc/mt_defs.h',
	    'openh264/codec/encoder/core/inc/dq_map.h',
	    'openh264/codec/encoder/core/inc/paraset_strategy.h',
	    'openh264/codec/encoder/core/inc/svc_mode_decision.h',
	    'openh264/codec/encoder/plus/inc/welsEncoderExt.h',
		],
		destination_path="")
	my_module.compile_version("C++", 2003)
	my_module.add_module_depend([
	    'openh264-common',
	    'openh264-processing'
	    ])
	return my_module
