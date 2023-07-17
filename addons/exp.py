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
from bpy_extras.io_utils  import ExportHelper
#from bpy_extras.io_utils import axis_conversion
import os
import json
import pprint
class kok(bpy.types.Panel):
    bl_label = "glTF Extras Data"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "glTF Extras data"
    
    # def draw(self, context):
    #     return super().draw(context)

class ExportGLTFWithCustomDataOperator(bpy.types.Operator, ExportHelper):
    bl_idname = "export_custom.gltf"
    bl_label = "Export GLTF with Custom Data"
    filename_ext = ".gltf"

    # def execute(self, context):
    #     # Get the export filepath
    #     filepath = os.path.join(self.filepath)

    #     # Define custom Extras and Asset data
    #     # custom_extras = []
    #     # custom_asset = {}
    #     custom_asset = {
    #         "generator": "My Custom Generator",
    #         "version": "1.0",
    #         "custom_field": "Custom Value"
    #     }
    #     custom_extras = [
    #         "Value 1",
    #         "Value 2",
    #         "Value 3"
    #     ]
        
        
            


    #     # Export GLTF with custom Extras and Asset
    #     bpy.ops.export_scene.gltf(filepath=filepath, export_extras=True, custom_extras=custom_extras, custom_asset=custom_asset)

    #     return {'FINISHED'}
    ##############################################################################
    def execute(self, context):
        pprint.pprint("Work State")
        # Get the export filepath
        filepath = os.path.join(self.filepath)
        pprint.pprint(filepath)
        # Export GLTF file
        bpy.ops.export_scene.gltf(filepath=filepath)

        # Read the exported GLTF file as JSON
        with open(filepath, 'r') as file:
            gltf_data = json.load(file)

        # Add custom "Extras" data
        gltf_data['extras'] = {
            "customExtras": "This is custom extras data"
        }

        # Add custom "Asset" data
        #gltf_data['asset']['customAssetField'] = "Custom asset value"

        # Write the modified GLTF data back to the file
        with open(filepath, 'w') as file:
            json.dump(gltf_data, file)
        
        return {'FINISHED'}
        
# Register the custom exporter operator
def menu_func_export(self, context):
    self.layout.operator(ExportGLTFWithCustomDataOperator.bl_idname, text="GLTF with Custom Data")
    pprint.pprint("Menu")
def register():
    # bpy.utils.register_class(kok)
    bpy.utils.register_class(ExportGLTFWithCustomDataOperator)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)
def unregister():
    # bpy.utils.unregister_class(kok)
    bpy.utils.unregister_class(ExportGLTFWithCustomDataOperator)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
if __name__ == "__main__":
    register()