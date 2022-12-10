import bpy

# --------- NON-COLOR COLOR SPACE ---------    
class AV_non_color(bpy.types.Operator):
    bl_idname = 'av.non_color'
    bl_label = 'Non-Color'

    def execute(self, context):
        images = bpy.data.images
        for img in images:
            img.colorspace_settings.name = "Non-Color"
        
        self.report({'INFO'}, "sve ok")
        return {'FINISHED'}
    
bpy.utils.register_class(AV_non_color)