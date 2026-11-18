import bpy
from mathutils import Vector

# Clear existing scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Create collections for each pose
for pose_name in ["Zhongli_Chibi_Standing", "Zhongli_Chibi_Thinking", "Zhongli_Chibi_Battle"]:
    if pose_name not in bpy.data.collections:
        collection = bpy.data.collections.new(pose_name)
        bpy.context.scene.collection.children.link(collection)

# Create basic Chibi Zhongli model
def create_chibi_zhongli(name, location):
    # Head
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.75, location=location)
    head = bpy.context.object
    head.name = f"Head_{name}"
    
    # Body
    bpy.ops.mesh.primitive_cube_add(size=(1,1,1), location=(location[0], location[1], location[2]-1.0))
    body = bpy.context.object
    body.name = f"Body_{name}"
    body.scale = (0.65, 0.55, 0.95)
    
    # Hair (simple)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.82, location=(location[0], location[1], location[2]+0.1))
    hair = bpy.context.object
    hair.name = f"Hair_{name}"
    hair.scale = (1.05, 0.95, 0.75)
    
    # Coat
    bpy.ops.mesh.primitive_cube_add(size=(1.3,1,1.6), location=(location[0], location[1], location[2]-0.9))
    coat = bpy.context.object
    coat.name = f"Coat_{name}"
    coat.scale = (0.85, 0.7, 1.1)
    
    # Geo Vision
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.18, location=(location[0], location[1]-0.35, location[2]-0.3))
    vision = bpy.context.object
    vision.name = f"Geo_Vision_{name}"
    
    # Simple Spear
    bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=2.8, location=(location[0]+0.9, location[1], location[2]-0.2))
    spear = bpy.context.object
    spear.name = f"Spear_{name}"
    spear.rotation_euler = (0.8, 0, 2.0)
    
    return [head, body, hair, coat, vision, spear]

# Create 3 versions
objects1 = create_chibi_zhongli("Standing", (0, 0, 0))
objects2 = create_chibi_zhongli("Thinking", (3, 0, 0))
objects3 = create_chibi_zhongli("Battle", (6, 0, 0))

# Link to collections
for obj in objects1:
    bpy.data.collections["Zhongli_Chibi_Standing"].objects.link(obj)
for obj in objects2:
    bpy.data.collections["Zhongli_Chibi_Thinking"].objects.link(obj)
for obj in objects3:
    bpy.data.collections["Zhongli_Chibi_Battle"].objects.link(obj)

# Add simple materials
def add_material(obj, color):
    mat = bpy.data.materials.new(name=f"Mat_{obj.name}")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = color + (1.0,)
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)

add_material(objects1[0], (0.95, 0.8, 0.7))      # Skin
add_material(objects1[2], (0.08, 0.08, 0.15))    # Hair
add_material(objects1[3], (0.05, 0.05, 0.12))    # Coat
add_material(objects1[4], (1.0, 0.7, 0.0))       # Geo Vision

print("=== ZHONGLI CHIBI 3 POSES BERHASIL DIBUAT ===")
print("Pose tersedia:")
print("1. Zhongli_Chibi_Standing")
print("2. Zhongli_Chibi_Thinking")
print("3. Zhongli_Chibi_Battle")
print("\nSimpan file ini sebagai zhongli_chibi_3poses.blend")
