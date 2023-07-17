bl_info = {
    "name": "Custom GLTF Export Add-on",
    "description": "Inserts custom data into GLTF export",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "File > Export",
    "category": "Import-Export",
}
import bpy


class kok(bpy.types.Panel):
    bl_label = "glTF Extras Data"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "glTF Extras data"
    


def register():
    bpy.utils.register_class(kok)


def unregister():
    bpy.utils.unregister_class(kok)


if __name__ == "__main__":
    register()
