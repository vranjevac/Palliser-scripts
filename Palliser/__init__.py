bl_info = {
    "name" : "Aleksandra Vranjevac",
    "author" : "Aleksandra Vranjevac",
    "version" : (1, 2),
    "blender" : (3, 1, 2),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Palliser"
}


import bpy
import sys
import os
#sys.path.append("D:/Addon/Palliser")     # stavi u isti folder! folder iznad
from Palliser import uv_maps, sockets, materials, rename, noncolor, apply_transforms

class palliser_view3d(bpy.types.Panel):
    bl_idname = 'PALLISER_VIEW_3D'
    bl_label = 'Palliser Add-on'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Palliser'
  
    def draw(self, context):
        layout = self.layout
        self.layout.label(text='HellooOoOoo', icon='GHOST_ENABLED')

        row = layout.row()
        row.label(icon="STICKY_UVS_DISABLE")
        row.operator("av.set_uv")
        
        row = layout.row()
        row.label(icon="OUTLINER_DATA_EMPTY")
        row.operator("av.add_sockets")
        
        row = layout.row()
        row.label(icon="NODE_MATERIAL")
        row.operator("av.append_materials")

        self.layout.label(text='Rename', icon='FILE_TEXT')
        row = layout.row()
        row.operator("av.mesh_rename")  
        row.operator("av.material_rename")
        
        row = layout.row()
        row.label(icon="COLORSET_10_VEC")
        row.operator("av.non_color")
        
        row = layout.row()
#        row.label(icon="COLORSET_10_VEC")
        row.operator("av.apply_transforms")

class palliser_shader(bpy.types.Panel):
    bl_idname = 'PALLISER_SHADER'
    bl_label = 'Palliser Add-on'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Palliser'
  
    def draw(self, context):
        layout = self.layout
        self.layout.label(text='HellooOoOoo', icon='GHOST_ENABLED')

        row = layout.row()
        row.label(icon="STICKY_UVS_DISABLE")
        row.operator("av.set_uv")
        
        row = layout.row()
        row.label(icon="NODE_MATERIAL")
        row.operator("av.append_materials")
        
        row = layout.row()
        row.label(icon="COLORSET_10_VEC")
        row.operator("av.non_color")
               
               
def register():
    bpy.utils.register_class(palliser_view3d)
    bpy.utils.register_class(palliser_shader)    
def unregister():
    bpy.utils.unregister_class(palliser_view3d)
    bpy.utils.unregister_class(palliser_shader)
    
if __name__ == "__main__":
    register()