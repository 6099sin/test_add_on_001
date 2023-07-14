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
from bpy_extras.io_utils import ExportHelper


class ExportGLTFWithCustomDataOperator(bpy.types.Operator, ExportHelper):
    bl_idname = "export_custom.gltf"
    bl_label = "Export GLTF with Custom Data"
    filename_ext = ".gltf"

    def execute(self, context):
        # Custom export code here
        # Insert your custom data into the GLTF export process
        return {'FINISHED'}

def register():
    bpy.utils.register_class(ExportGLTFWithCustomDataOperator)


def unregister():
    bpy.utils.unregister_class(ExportGLTFWithCustomDataOperator)


if __name__ == "__main__":
    register()
