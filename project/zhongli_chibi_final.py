import bpy
from mathutils import Euler

# Clear everything
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Create Collections
for name in ["Standing", "Thinking", "Battle"]:
    coll_name = f"Zhongli_Chibi_{name}"
    if coll_name not in bpy.data.collections:
        collection = bpy.data.collections.new(coll_name)
        bpy.context.scene.collection.children.link(collection)

def make_material(name, color):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs['Base Color'].default_value = color
    return mat

def create_chibi_zhongli(pose_name, x_pos):
    loc = (x_pos, 0, 0)
    
    # HEAD
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.85, location=loc)
    head = bpy.context.object
    head.name = f"Head_{pose_name}"
    head.data.materials.append(make_material("Skin", (0.96, 0.82, 0.72, 1.0)))
    
    # HAIR (main)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.95, location=(loc[0], loc[1], loc[2]+0.15))
    hair = bpy.context.object
    hair.name = f"Hair_{pose_name}"
    hair.scale = (1.1, 1.05, 0.9)
    hair.data.materials.append(make_material("Hair", (0.08, 0.08, 0.18, 1.0)))
    
    # BODY
    bpy.ops.mesh.primitive_cube_add(size=1, location=(loc[0], loc[1], loc[2]-1.1))
    body = bpy.context.object
    body.name = f"Body_{pose_name}"
    body.scale = (0.7, 0.55, 1.0)
    body.data.materials.append(make_material("Coat_Dark", (0.05, 0.05, 0.12, 1.0)))
    
    # COAT DETAIL
    bpy.ops.mesh.primitive_cube_add(size=1, location=(loc[0], loc[1], loc[2]-0.9))
    coat = bpy.context.object
    coat.name = f"Coat_Detail_{pose_name}"
    coat.scale = (0.85, 0.7, 1.25)
    coat.data.materials.append(make_material("Coat_Gold", (0.7, 0.55, 0.15, 1.0)))
    
    # GEO VISION
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.2, location=(loc[0], loc[1]-0.38, loc[2]-0.55))
    vision = bpy.context.object
    vision.name = f"Vision_{pose_name}"
    vision.data.materials.append(make_material("Geo_Vision", (1.0, 0.75, 0.0, 1.0)))
    
    # SPEAR
    bpy.ops.mesh.primitive_cylinder_add(radius=0.045, depth=3.2, location=(loc[0]+0.9, loc[1], loc[2]-0.4))
    spear = bpy.context.object
    spear.name = f"Spear_{pose_name}"
    spear.rotation_euler = Euler((0.6, 0.2, 2.2), 'XYZ')
    spear.data.materials.append(make_material("Spear", (0.6, 0.65, 0.7, 1.0)))
    
    objects = [head, hair, body, coat, vision, spear]
    
    # Link to collection
    for obj in objects:
        bpy.data.collections[f"Zhongli_Chibi_{pose_name}"].objects.link(obj)
    
    return objects

# Generate 3 poses
create_chibi_zhongli("Standing", 0)
create_chibi_zhongli("Thinking", 5)
create_chibi_zhongli("Battle", 10)

print("\n" + "="*60)
print("✅ ZHONGLI CHIBI 3D BERHASIL DIBUAT!")
print("="*60)
print("3 Pose telah dibuat di Collection:")
print("   • Zhongli_Chibi_Standing")
print("   • Zhongli_Chibi_Thinking")
print("   • Zhongli_Chibi_Battle")
print("\nSilakan save file sebagai zhongli_chibi_final.blend")
print("="*60)
