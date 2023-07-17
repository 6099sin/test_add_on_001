from bpy.types import Operator, Panel
from bpy.props import StringProperty, IntProperty, EnumProperty, CollectionProperty
import json
import bpy
bl_info = {
    "name": "My_Addon_test",
    "description": "A custom add-on with a UI for inputting various types of data in the 3D viewport.",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D",
    "category": "Object"
}


class MyAddonProperties(bpy.types.PropertyGroup):
    my_string: EnumProperty(
        name="Component",
        items=[
            ("OPTION1", "Middle", "Description for Option 1"),
            ("OPTION2", "Lower", "Description for Option 2"),
            ("OPTION3", "Upper", "Description for Option 3"),
            ("OPTION4", "Hat", "Description for Option 3"),
            ("OPTION5", "Hair", "Description for Option 3"),
        ]
    )
    my_integer: IntProperty(name="VersionNumber",default=0,min=0,max=12)
    my_enum: EnumProperty(
        name="MasterMaterial",
        items=[
            ("OPTION1", "MM_Mat_v6", "Description for Option 1"),
            ("OPTION2", "MM_Mat_v6_Emission", "Description for Option 2"),
            ("OPTION3", "MM_Fur_v3", "Description for Option 3"),
        ]
    )

    my_name_asset: StringProperty(name="Asset Name")

    my_string_array: CollectionProperty(
        type=bpy.types.PropertyGroup,
        name="String Array",
    )


class MyAddonOperator(Operator):
    bl_idname = "object.my_addon_operator"
    bl_label = "My Addon Operator"

    def execute(self, context):
        props = context.scene.my_addon_properties

        # Access the input values
        my_string = props.my_string
        my_integer = props.my_integer
        my_enum = props.my_enum
        my_string_array = [item.string_item for item in props.my_string_array]
        my_name_asset= props.my_name_asset
        # Create JSON data
        data = {
            "String": my_string,
            "Integer": my_integer,
            "Enum": my_enum,
            "String Array": my_string_array,
            "String" : my_name_asset
        }
        json_data = json.dumps(data, indent=4)
        print("JSON Data:")
        print(json_data)
        
        return json_data
        # return {'FINISHED'}


class MyAddonPanel(Panel):
    bl_idname = "OBJECT_PT_my_addon_panel"
    bl_label = "I/O Extras Data"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My Addon'

    def draw(self, context):
        layout = self.layout
        props = context.scene.my_addon_properties

        layout.label(text="Input Data:")
        #layout.label(text="my_name_asset")
        layout.prop(props,"my_name_asset")
        layout.prop(props, "my_integer")
        layout.prop(props, "my_string")
        
        layout.prop(props, "my_enum")

        layout.label(text="String Array:")
        for item in props.my_string_array:
            layout.prop(item, "string_item", text="")

       

        layout.operator("object.my_addon_operator", text="Execute")


classes = [
    MyAddonProperties,
    MyAddonOperator,
    MyAddonPanel,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.my_addon_properties = bpy.props.PointerProperty(
        type=MyAddonProperties)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.my_addon_properties


if __name__ == "__main__":
    register()
