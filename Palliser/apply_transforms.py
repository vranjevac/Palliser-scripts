import bpy

# --------- APPLY TRANSFORMS ---------    
class AV_apply_transforms(bpy.types.Operator):
    bl_idname = 'av.apply_transforms'
    bl_label = 'Apply Transforms'

    def execute(self, context):
        scene = bpy.context.scene
        objects = scene.objects
        active_object = bpy.context.object

        def parentless():
            nulti = []
            for i in range(0, len(objects)):
                if objects[i].parent == None:
                    nulti.append(objects[i])
            return nulti
                
        nulti = parentless()

        def hierarchy_traversal(root_object):
          objects = []

          def _traverse(obj):
            objects.append(obj)
            for child in obj.children:
              _traverse(child)

          _traverse(root_object)

          return objects

        hierarchy1 = []
        for i in nulti:
            hierarchy1.append(hierarchy_traversal(i))

        hierarchy = []
        for i in range(0, len(hierarchy1)):
            for j in range(0, len(hierarchy1[i])):
                hierarchy.append(hierarchy1[i][j])
            
        print(hierarchy)
        
        sockets = ["component_l", "component_r", "side_l", "side_r", "leg_f", "leg_b", "headboard"]
        for i in range(0, len(hierarchy)):
            if hierarchy[i].name not in sockets:
                hierarchy[i].select_set(True)
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True) 
                hierarchy[i].select_set(False)    
                
        for i in range(0, len(hierarchy)):
            if hierarchy[i].name in sockets:
                hierarchy[i].select_set(True)
                bpy.ops.object.transform_apply(location=False, rotation=True, scale=True) 
                hierarchy[i].select_set(False)         
        
        self.report({'INFO'}, "sve ok")
        return {'FINISHED'}
    
bpy.utils.register_class(AV_apply_transforms)  