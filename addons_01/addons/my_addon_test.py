bl_info = {
    "name": "My_Addon_test",
    "description": "A custom add-on with a UI for inputting various types of data in the 3D viewport.",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D",
    "category": "Object"
}

import bpy
from bpy.props import StringProperty, IntProperty, EnumProperty, CollectionProperty
from bpy.types import Operator, Panel


class MyAddonProperties(bpy.types.PropertyGroup):
    my_string: StringProperty(name="String")
    my_integer: IntProperty(name="Integer")
    my_enum: EnumProperty(
        name="Enum",
        items=[
            ("OPTION1", "Option 1", "Description for Option 1"),
            ("OPTION2", "Option 2", "Description for Option 2"),
            ("OPTION3", "Option 3", "Description for Option 3"),
        ]
    )
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

        # Print the input values
        print("String:", my_string)
        print("Integer:", my_integer)
        print("Enum:", my_enum)
        print("String Array:", my_string_array)

        return {'FINISHED'}


class MyAddonPanel(Panel):
    bl_idname = "OBJECT_PT_my_addon_panel"
    bl_label = "My Addon Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My Addon'

    def draw(self, context):
        layout = self.layout
        props = context.scene.my_addon_properties

        layout.label(text="Input Data:")

        layout.prop(props, "my_string")
        layout.prop(props, "my_integer")
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
    bpy.types.Scene.my_addon_properties = bpy.props.PointerProperty(type=MyAddonProperties)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.my_addon_properties


if __name__ == "__main__":
    register()
