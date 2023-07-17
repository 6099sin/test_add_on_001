import bpy
import json 
import os

filepath=r'D:\Github\DevCDTools_02\glTF-Sample-Models\test_add_on_001\cube1.gltf'

filepath2=r'D:\Github\DevCDTools_02\glTF-Sample-Models\test_add_on_001\addons\test.json'
# filepath1=os.path('D:\Github\DevCDTools_02\glTF-Sample-Models\test_add_on_001\addons\test.json')
# with open('D:\Github\DevCDTools_02\glTF-Sample-Models\test_add_on_001\cube1.gltf', 'r') as f:
#   data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
with open(filepath,'r') as file:
    data = json.load(file)
# data= open(filepath2, 'r')
# data1=data.read()
person=json.loads(data)

print(json.dumps(person, indent = 4, sort_keys=True))
# test=json.load(filepath2)
print(filepath)
# print(dir(json))