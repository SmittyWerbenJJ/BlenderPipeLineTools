import bpy


def getMeshObjectsInView():
    return [x for x in bpy.context.view_layer.objects if x.type == "MESH"]


print("SPlitting...")
active_obj = bpy.context.view_layer.objects.active

if active_obj == None:
    raise Exception("YOU HAVE TO SELECT A MESH OBJECT IN EDIT MODE")
if not (active_obj.type == "MESH"):
    raise Exception("YOU HAVE TO SELECT A MESH OBJECT IN EDIT MODE")


all_objects = getMeshObjectsInView()
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.separate(type="MATERIAL")
new_all_objects = getMeshObjectsInView()

for old_obj in all_objects:
    if old_obj in new_all_objects:
        new_all_objects.remove(old_obj)
new_all_objects.append(bpy.context.view_layer.objects.active)

# rename objects
for obj in new_all_objects:
    material = obj.material_slots[0].material
    obj.name = material.name

bpy.ops.object.mode_set(mode="OBJECT")
