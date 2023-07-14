import bpy
import pprint
import bmesh
import pathlib
import json
obj=bpy.context.active_object





# pprint.pprint(obj.name)
# obj_data = bmesh.from_edit_mesh(obj.data)
# mesh_to_verts = []
# for face in obj_data.faces :
#         face_verts=[]
#         for vert in face.verts:
#             face_verts.append(vert.index)
#         mesh_to_verts.append(face_verts)
# for meshface in mesh_to_verts:
#     pprint.pprint(meshface)
#############################################################
def get_path_to_mesh_data():
    return pathlib.Path.home() / "Documents" / "mesh.json"


def save_data(data):
    path_to_file = get_path_to_mesh_data()

    # open the json file for writing and dump the data in text form
    with open(path_to_file, "w") as out_file_obj:
        # convert the dictionary into text
        text = json.dumps(data, indent=4)
        # write the text into the file
        out_file_obj.write(text)

def create_json_data_from_mesh(obj):

    # bpy.ops.mesh.primitive_cube_add()
    # bpy.ops.mesh.primitive_ico_sphere_add()
    # mesh_object = bpy.context.active_object

    pprint.pprint("create_json_data_Function")
    pprint.pprint(obj.name)
    data = get_mesh_data(obj)

    save_data(data)

def get_mesh_data(mesh_object):
    """Extract the vert indices that make up each face and the vert coordinates"""

    # enter edit mode for the mesh
    #bpy.ops.object.editmode_toggle(mode="EDIT")

    bmesh_obj = bmesh.from_edit_mesh(mesh_object.data)

    # extract the vert indices that make up each face
    face_to_vert = []
    for face in bmesh_obj.faces:
        face_verts = []
        for vert in face.verts:
            face_verts.append(vert.index)
        face_to_vert.append(face_verts)

    # initialize a list with the same size as the vert count
    vert_count = len(bmesh_obj.verts)
    vert_coords = [None] * vert_count
    # extract the vert coordinates
    for vert in bmesh_obj.verts:
        vert_coords[vert.index] = list(vert.co)

    # exit edit mode
    #bpy.ops.object.editmode_toggle(mode="OBJECT")

    # create a dictionary with the mesh data
    data = {
        "object_name": mesh_object.name,
        "face_verts": face_to_vert,
        "vert_coordinates": vert_coords,
    }

    pprint.pprint(data)
    pprint.pprint("get_mesh_data")
    return data
############################################################
def main():
    pprint.pprint(pathlib.Path.home())
    create_json_data_from_mesh(obj)

main()

#######################################################
# def getFaceVert():
#     #bpy.ops.object.mode_set(mode="EDIT")
#     bmesh_obj = bmesh.from_edit_mesh(get_mesh_data)

#     face_to_vert =[]
#     for face in bmesh_obj.faces :
#         face_verts=[]
#         for vert in face.verts:
#             face_verts.append(vert.index)
#         face_to_vert.append(face_verts)


#####################################################
# def get_mesh_data(mesh_object):
#     """Extract the vert indices that make up each face and the vert coordinates"""

#     # enter edit mode for the mesh
#     bpy.ops.object.editmode_toggle()

#     bmesh_obj = bmesh.from_edit_mesh(mesh_object.data)

#     # extract the vert indices that make up each face
#     face_to_vert = []
#     for face in bmesh_obj.faces:
#         face_verts = []
#         for vert in face.verts:
#             face_verts.append(vert.index)
#         face_to_vert.append(face_verts)

#     # initialize a list with the same size as the vert count
#     vert_count = len(bmesh_obj.verts)
#     vert_coords = [None] * vert_count
#     # extract the vert coordinates
#     for vert in bmesh_obj.verts:
#         vert_coords[vert.index] = list(vert.co)

#     # exit edit mode
#     bpy.ops.object.editmode_toggle()

#     # create a dictionary with the mesh data
#     data = {
#         "object_name": mesh_object.name,
#         "face_verts": face_to_vert,
#         "vert_coordinates": vert_coords,
#     }

#     pprint.pprint(data)

#     return data