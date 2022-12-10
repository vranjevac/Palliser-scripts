import bpy

# --------- RESOLUTION ---------    
class AV_set_resolution(bpy.types.Operator):
    bl_idname = 'av.set_res'
    bl_label = 'Set Resolution'

    def execute(self, context):
        bpy.context.preferences.addons["ZenUV"].preferences.td_im_size_presets = "4096"
        self.report({'INFO'}, "sve ok")
        return {'FINISHED'}

bpy.utils.register_class(AV_set_resolution)   
    
    
# --------- TEXEL DENSITY ---------
class AV_set_texel_density(bpy.types.Operator):
    bl_idname = 'av.set_td'
    bl_label = 'Set Texel Density'

    def execute(self, context):
        bpy.context.preferences.addons["ZenUV"].preferences.TexelDensity = 4000
        self.report({'INFO'}, "sve ok")
        return {'FINISHED'}

bpy.utils.register_class(AV_set_texel_density)


# --------- UV SETS ---------
class AV_set_uv_maps(bpy.types.Operator):
    bl_idname = 'av.set_uv_maps'
    bl_label = 'Set UV Maps'

    def execute(self, context):
        if len(bpy.context.object.data.uv_layers) > 1:
            return {'FINISHED'}
        bpy.context.object.data.uv_layers[0].name = "uv_fabrics"
        bpy.ops.mesh.uv_texture_add()
        bpy.context.object.data.uv_layers[1].name = "uv_maps"

        bpy.context.object.data.uv_layers['uv_fabrics'].active = True 
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.select_all(action='SELECT')

        try:
            bpy.ops.uv.zenuv_set_texel_density()
        except RuntimeError:
            bpy.ops.uv.zenuv_set_texel_density('INVOKE_DEFAULT')

        bpy.ops.object.editmode_toggle()

        bpy.context.object.data.uv_layers["uv_maps"].active_render = True
        bpy.context.object.data.uv_layers['uv_fabrics'].active = True
        
        self.report({'INFO'}, "sve ok")
        return {'FINISHED'}

bpy.utils.register_class(AV_set_uv_maps)


# --------- RES, TD, SETS ---------
class AV_set_UV(bpy.types.Operator):
    bl_idname = 'av.set_uv'
    bl_label = 'Set UV parameters'

    def execute(self, context):
        bpy.ops.av.set_td()
        bpy.ops.av.set_res()
        bpy.ops.av.set_uv_maps()

        self.report({'INFO'}, "sve ok")
        return {'FINISHED'}

bpy.utils.register_class(AV_set_UV)