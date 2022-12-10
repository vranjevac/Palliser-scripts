import bpy
    
# --------- MESH RENAME ---------    
class AV_mesh_rename(bpy.types.Operator):
    bl_idname = 'av.mesh_rename'
    bl_label = 'Meshes'

# --------- REMOVING ANYTHING AFTER "." ---------    
    def execute(self, context):
        scene = bpy.context.scene
        objects = scene.objects
        for obj in objects:
            obj.name = obj.name.split(".")[0]

# --------- REMOVING THE TAILS ---------    
        substring = ["sockets", "component_l", "component_r", "side_l", "side_r", "table_base", "LegsEspresso", "LegsMetal", "leg_base", "base_curve", "back_pillow", "seat_pillow", "seat_cushion", "skirt", "cushion_l", "cushion_r", "cushion_side", "nail_sides", "nail_base", "small_pins", "medium_pins", "large_pins", "side_pins", "acc_base"]
        scene = bpy.context.scene
        objects = scene.objects
        for obj in objects:
            for substr in substring:
                if substr in obj.name:
                    obj.name = substr
        
        self.report({'INFO'}, "sve ok")
        return {'FINISHED'}    
        
    
bpy.utils.register_class(AV_mesh_rename)


    
# --------- MATERIAL RENAME ---------    
class AV_material_rename(bpy.types.Operator):
    bl_idname = 'av.material_rename'
    bl_label = 'Materials'

# --------- REMOVING ANYTHING AFTER "." --------- 
    def execute(self, context):
        materials = bpy.data.materials
        for mat in materials:
            mat.name = mat.name.split(".")[0]    
    
# --------- REMOVING THE TAILS ---------
        substring = ["main", "back_pillow", "seat_cushion", "arm", "back", "metalMAT", "woodMAT", "woodLegs", "PlasticBlack", "contrast_welt", "Metal"]
        materials = bpy.data.materials
        for mat in materials:
            for substr in substring:
                if "back" in mat.name:
                    if "back_pillow" in mat.name:
                        mat.name = "back_pillow"
                        break
                if substr in mat.name:
                    mat.name = substr  
        
        self.report({'INFO'}, "sve ok")
        return {'FINISHED'} 
    
bpy.utils.register_class(AV_material_rename)


