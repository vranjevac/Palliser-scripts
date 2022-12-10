import bpy

# --------- APPEND MATERIALS ---------    
class AV_append_materials(bpy.types.Operator):
    bl_idname = 'av.append_materials'
    bl_label = 'Append Materials'

    def execute(self, context):
        filepath = "X:/Palliser/BLENDER/materials.blend"
        link = False

        with bpy.data.libraries.load(filepath, link=False) as (data_from, data_to):
            data_to.materials = data_from.materials                
        
        self.report({'INFO'}, "sve ok")
        return {'FINISHED'}
    
bpy.utils.register_class(AV_append_materials)  