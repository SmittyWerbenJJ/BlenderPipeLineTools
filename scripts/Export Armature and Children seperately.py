import bpy
import os

# serpens props
filepath: str


def getMeshObjectsInView():
    objs = []
    for x in bpy.context.view_layer.objects:
        x: bpy.types.Object
        if x.type == "MESH":
            objs.append(x)
    return objs


print("exporting...")
armature = bpy.context.view_layer.objects.active

if armature == None:
    raise Exception("YOU HAVE TO SELECT SOMETHING")
children = [x for x in armature.children]

bpy.ops.object.select_all(action="DESELECT")
bpy.context.view_layer.objects[armature.name].select_set(True)

out_dir = os.path.dirname(filepath)
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

for child in children:
    bpy.context.view_layer.objects[child.name].select_set(True)
    out_path = os.path.join(out_dir, child.name)
    bpy.ops.better_export.fbx(
        filepath=out_path,
        my_file_type=".fbx",
        use_selection=True,
    )
    bpy.context.view_layer.objects[child.name].select_set(False)
print("exporting: Done!")
