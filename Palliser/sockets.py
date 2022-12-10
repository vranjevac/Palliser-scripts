import bpy
    
# --------- RESOLUTION ---------    
class AV_add_sockets(bpy.types.Operator):
    bl_idname = 'av.add_sockets'
    bl_label = 'Add Sockets'

    def execute(self, context):
        #--------- Extracting the FILENAME ---------
        filepath = bpy.data.filepath
        filename_blend = filepath.split("/")[-1].split("\\")[-1]
        filename = filename_blend.split(".blend")[0]
        
        if filename == "":
            filename = "сачувај фајл!!1"

        bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.context.selected_objects[0].name=filename

        bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.context.selected_objects[0].name="sockets"

        objects = bpy.data.objects
        parent_obj = objects[filename]
        for obj in objects:
            if obj != parent_obj:
                obj.parent = parent_obj        
        
        self.report({'INFO'}, "sve ok")
        return {'FINISHED'}
    
bpy.utils.register_class(AV_add_sockets)