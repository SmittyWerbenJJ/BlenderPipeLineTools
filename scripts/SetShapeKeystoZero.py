# serpens operator
import bpy

obj = bpy.context.view_layer.objects.active

if obj is None:
    raise Exception("YOU HAVE TO SELECT A OBJECT")

if obj.type != "MESH":
    raise Exception("YOU HAVE TO SELECT A MESH OBJECT")

for shapekey in obj.data.shape_keys.key_blocks:
    shapekey.value = int(0)
