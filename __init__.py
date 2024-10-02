import bpy
import math
from bpy.props import BoolProperty, FloatProperty

def get_distance(p1, p2):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2 + (p2.z - p1.z) ** 2)

def join_objects(self, context):
    selected_obj = bpy.context.selected_objects.copy()
    if len(selected_obj) > 0:
        done = []
        joined = []

        if self.set_origin_to_object:
            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='MEDIAN')

        for obj in bpy.context.selected_objects:
            obj.select_set(False)

        for i, obj in enumerate(selected_obj):
            if obj not in done:
                for obj_inner in selected_obj[i+1:]:
                    if obj_inner not in done and obj_inner != obj:
                        distance = get_distance(obj.location, obj_inner.location)
                        if distance < self.scaling:
                            bpy.context.view_layer.objects.active = obj
                            obj.select_set(True)
                            obj_inner.select_set(True)
                            done.append(obj_inner)
                            bpy.ops.object.join()
                            joined.append(obj)
                            obj.select_set(False)

        # Select the remaining objects that were not joined
        for i, obj in enumerate(selected_obj):
            if obj not in done:
                if i == 0:
                    bpy.context.view_layer.objects.active = obj
                obj.select_set(True)
    else:
        print('Nothing selected!')

class OBJECT_OT_JoinByDistance(bpy.types.Operator):
    """Join by distance"""
    bl_idname = "object.join_by_distance"  # Blender Operator ID
    bl_label = "Join objects by distance"
    bl_options = {'REGISTER', 'UNDO'}

    scaling: FloatProperty(
        name="Distance",
        description="Minimal distance between objects",
        min=0.0,
        max=10000000.0,
        default=0.01
    )
    set_origin_to_object: BoolProperty(
        name="Set Origin to Object center first",
        description="If object origin is somewhere else",
        default=True
    )

    def execute(self, context):
        join_objects(self, context)
        return {'FINISHED'}

addon_keymaps = []

def register():
    bpy.utils.register_class(OBJECT_OT_JoinByDistance)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
        kmi = km.keymap_items.new(OBJECT_OT_JoinByDistance.bl_idname, 'J', 'PRESS')
        addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_JoinByDistance)
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
