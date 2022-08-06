import bpy

bpy.ops.better_export.fbx(
    filepath="",
    check_existing=True,
    filter_glob="*.fbx;*.dae;*.obj;*.dxf",
    my_file_type=".fbx",
    my_fbx_format="binary",
    my_fbx_version="FBX201800",
    my_fbx_axis="MayaZUp",
    use_selection=False,
    use_only_deform_bones=False,
    use_only_selected_deform_bones=False,
    use_vertex_animation=False,
    use_vertex_format="mcx",
    use_vertex_space="world",
    my_vertex_frame_start=1,
    my_vertex_frame_end=10,
    use_animation=True,
    my_animation_offset=0,
    use_apply_modifiers=True,
    use_include_armature_deform_modifier=False,
    use_triangulate=False,
    my_animation_type="Active",
    use_concatenate_all=False,
    my_max_bone_influences="Unlimited",
    use_rigify_armature=False,
    use_rigify_root_bone=True,
    my_scale=100,
    use_optimize_for_game_engine=True,
    use_reset_mesh_origin=True,
    use_ignore_armature_node=True,
    use_edge_crease=True,
    my_edge_smoothing="FBXSDK",
    my_edge_crease_scale=1,
    my_separate_files=False,
    my_material_style="Blender",
    use_embed_media=False,
    use_copy_texture=False,
    my_texture_subdirectory="textures",
    use_simplify_keyframe=False,
    my_simplify_keyframe_factor=1,
)