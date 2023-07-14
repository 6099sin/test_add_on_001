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
        # Custom data to insert
        custom_data = {
            "moew": ["hh", "kk"],
        }

        # Get the default GLTF export operator
        gltf_operator = bpy.ops.export_scene.gltf

        # Set the custom data as a property of the operator
        gltf_operator.custom_data = custom_data

        # Execute the GLTF export operator
        return gltf_operator(context, self.filepath)

def register():
    bpy.utils.register_class(ExportGLTFWithCustomDataOperator)


def unregister():
    bpy.utils.unregister_class(ExportGLTFWithCustomDataOperator)


if __name__ == "__main__":
    register()
