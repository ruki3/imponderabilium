# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "brenchtroom",
    "author" : "pomidorek",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (1, 0, 0),
    "location" : "View3D",
    "warning" : "",
    "category" : "View3D"
}

import bpy
import bmesh
import mathutils
import rna_keymap_ui
from bpy.props import *
from bpy.types import AddonPreferences

def get_preferences():
    return bpy.context.preferences.addons[__name__].preferences

class BH_AddonPreferences(AddonPreferences):
    bl_idname = __name__

    keyboard_section : BoolProperty(
        name="Keyboard Shortcuts",
        description="Keyboard Shortcuts",
        default=True
    )

    def draw(self, context):
        
        wm = bpy.context.window_manager 

        layout = self.layout

        # Keyboard shortcuts section
        layout.prop(self, "keyboard_section", icon='DISCLOSURE_TRI_DOWN' if self.keyboard_section else 'DISCLOSURE_TRI_RIGHT')
        if self.keyboard_section:

            km_items = wm.keyconfigs.user.keymaps['3D View'].keymap_items   

            km_item = km_items['bh.increase_grid_scale']

            row = self.layout.row()
            row.label(text=km_item.name)
            row.prop(km_item, 'type', text='', full_event=True)

            km_item = km_items['bh.decrease_grid_scale']

            row = self.layout.row()
            row.label(text=km_item.name)
            row.prop(km_item, 'type', text='', full_event=True)


class BH_GridSettings(bpy.types.PropertyGroup):
    dropdown : EnumProperty(
        name= "Grid Scale",
        default= "6",
        description= "Choose a preset grid size.",
        items= [("1", "0.0625", ""),
            ("2", "0.125", ""),
            ("3", "0.25", ""),
            ("4", "0.5", ""),
            ("5", "1", ""),
            ("6", "2", ""),
            ("7", "4", ""),
            ("8", "8", ""),]
    )

class BH_TriplanarSettings(bpy.types.PropertyGroup):

    scale_uniform : bpy.props.BoolProperty(
        name="Scale Uniform", description="If true, both axes will be scaled by the same amount. Otherwise U and V scaling can be specified separately.", default = True
    )
    
    scale_u : bpy.props.FloatProperty(
        name="U Scale", description="Scale of texture along horizontal axis", default = 1, min=0, soft_max = 4
    )

    scale_v : bpy.props.FloatProperty(
        name="V Scale", description="Scale of texture along vertical axis", default = 1, min=0, soft_max = 4
    )

    use_grid_scale : bpy.props.BoolProperty(
        name="Use Grid Scale", description="If true, multiply coords by current grid size.", default = False
    )

def redraw_all_viewports(context):
    for area in bpy.context.screen.areas: # iterate through areas in current screen
        if area.type == 'VIEW_3D':
            area.tag_redraw()

def map_editmode(context):
    settings = context.scene.triplanar_settings_props

    scale = context.space_data.overlay.grid_scale
    use_grid_scale = settings.use_grid_scale
    print("scale %s" % (str(scale)))
    print("use_grid_scale %s" % (str(use_grid_scale)))

    for obj in context.selected_objects:
        if obj.type != 'MESH':
            continue

        l2w = obj.matrix_world

        me = obj.data
        bm = bmesh.from_edit_mesh(me)
#        bm = bmesh.new()
#        bm.from_mesh(me)

        uv_layer = bm.loops.layers.uv.verify()


        # adjust uv coordinates
        for face in bm.faces:
            if face.select:
                xAbs = abs(face.normal.x)
                yAbs = abs(face.normal.y)
                zAbs = abs(face.normal.z)

                for loop in face.loops:
                    loop_uv = loop[uv_layer]

                    wco = l2w @ loop.vert.co

                    # use xy position of the vertex as a uv coordinate
                    uv = None
                    if (xAbs > yAbs and xAbs > zAbs):
                        uv = mathutils.Vector(wco.yz)
                    elif (yAbs > zAbs):
                        uv = mathutils.Vector(wco.xz)
                    else:
                        uv = mathutils.Vector(wco.xy)

                    if settings.scale_uniform:
                        uv.x /= settings.scale_u
                        uv.y /= settings.scale_u
                    else:
                        uv.x /= settings.scale_u
                        uv.y /= settings.scale_v

                    if use_grid_scale:
                        uv /= scale

                    loop_uv.uv = uv

        bmesh.update_edit_mesh(me)
#        bm.to_mesh(me)
#        bm.free()

    redraw_all_viewports(context)    


def map_objectmode(context):
    settings = context.scene.triplanar_settings_props
    scale = context.space_data.overlay.grid_scale
    use_grid_scale = settings.use_grid_scale
    print("scale %s" % (str(scale)))
    print("use_grid_scale %s" % (str(use_grid_scale)))

    for obj in context.selected_objects:
        if obj.type != 'MESH':
            continue

        l2w = obj.matrix_world

        me = obj.data
#        bm = bmesh.from_edit_mesh(me)
        bm = bmesh.new()
        bm.from_mesh(me)

        uv_layer = bm.loops.layers.uv.verify()

        # adjust uv coordinates
        for face in bm.faces:
            xAbs = abs(face.normal.x)
            yAbs = abs(face.normal.y)
            zAbs = abs(face.normal.z)

            for loop in face.loops:
                loop_uv = loop[uv_layer]

                wco = l2w @ loop.vert.co

                # use xy position of the vertex as a uv coordinate
                uv = None
                if (xAbs > yAbs and xAbs > zAbs):
                    uv = mathutils.Vector(wco.yz)
                elif (yAbs > zAbs):
                    uv = mathutils.Vector(wco.xz)
                else:
                    uv = mathutils.Vector(wco.xy)

                if settings.scale_uniform:
                    uv.x /= settings.scale_u
                    uv.y /= settings.scale_u
                else:
                    uv.x /= settings.scale_u
                    uv.y /= settings.scale_v

                if use_grid_scale:
                    uv /= scale

                loop_uv.uv = uv

#        bmesh.update_edit_mesh(me)
        bm.to_mesh(me)
        bm.free()

    redraw_all_viewports(context)    


class BH_TriplanarUnwrap(bpy.types.Operator):
    """Perform cubemap projection using grid coodinates to generate UVs."""
    bl_idname = "bh.triplanar_unwrap"
    bl_label = "Triplanar Unwrap"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return obj and obj.type == 'MESH' and (obj.mode == 'EDIT' or obj.mode == 'OBJECT')
#        return obj and obj.type == 'MESH' and obj.mode == 'OBJECT'

    def execute(self, context):
        obj = context.active_object
        if obj.mode == 'EDIT':
            map_editmode(context)
        elif obj.mode == 'OBJECT':
            map_objectmode(context)
        return {'FINISHED'}

class BH_GridScale(bpy.types.Operator):
    """Change the grid scale"""
    bl_idname = "bh.grid_scale"
    bl_label = "Set"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        grid_s = context.scene.grid_settings
        scale = 2
        i = 0



        for screen in bpy.data.screens:
            i += 1
            for area in screen.areas:
                if area.type == "VIEW_3D":
                    for space in area.spaces:
                        if space.type == "VIEW_3D":
                            if grid_s.dropdown == "1":
                                space.overlay.grid_scale = 0.0625
                            elif grid_s.dropdown == "2":
                                space.overlay.grid_scale = 0.125
                            elif grid_s.dropdown == "3":
                                space.overlay.grid_scale = 0.25
                            elif grid_s.dropdown == "4":
                                space.overlay.grid_scale = 0.5
                            elif grid_s.dropdown == "5":
                                space.overlay.grid_scale = 1
                            elif grid_s.dropdown == "6":
                                space.overlay.grid_scale = 2
                            elif grid_s.dropdown == "7":
                                space.overlay.grid_scale = 4
                            elif grid_s.dropdown == "8":
                                space.overlay.grid_scale = 8
                #else:
                   # print("no 3d viewport in given screen, skipping")

        return {"FINISHED"}

    def invoke(self, context, event):
        self.execute(context)

        return {"FINISHED"}

class BH_GridScaleUp(bpy.types.Operator):
    """Increase the grid scale"""
    bl_idname = "bh.increase_grid_scale"
    bl_label = "Increase grid scale"
    bl_options = {"REGISTER"}

    def execute(self, context):
        grid_s = context.scene.grid_settings
        i = int(grid_s.dropdown)

        if i != 8:
            i += 1
            grid_s.dropdown = str(i)
            bpy.ops.bh.grid_scale("EXEC_DEFAULT")

        return {"FINISHED"}

    def invoke(self, context, event):
        self.execute(context)

        return {"FINISHED"}

class BH_GridScaleDown(bpy.types.Operator):
    """Decrease the grid scale"""
    bl_idname = "bh.decrease_grid_scale"
    bl_label = "Decrease grid scale"
    bl_options = {"REGISTER"}

    def execute(self, context):
        grid_s = context.scene.grid_settings
        i = int(grid_s.dropdown)

        if i != 1:
            i -= 1
            grid_s.dropdown = str(i)
            bpy.ops.bh.grid_scale("EXEC_DEFAULT")

        return {"FINISHED"}

    def invoke(self, context, event):
        self.execute(context)

        return {"FINISHED"}
            


class BH_GridPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_idname = "OBJECT_PT_gscale"
    bl_region_type = "UI"
    bl_label = "brenchtroom"
    bl_category = "brenchtroom"


    def draw(self, context):
        layout = self.layout
        grid_s = context.scene.grid_settings
        uv_s = context.scene.triplanar_settings_props

        
        col = layout.column(align=True)
        col.label(text="-Grid Settings-")
        row = col.row()
        row.prop(grid_s, "dropdown")
        row.operator("bh.grid_scale")

        layout.separator()

        col = layout.column(align=True)
        col.label(text="-Triplanar UV-")
        col.prop(uv_s, "scale_uniform")
        row = col.row()
        if uv_s.scale_uniform:
            row.prop(uv_s, "scale_u", text="Scale")
        else:
            row.prop(uv_s, "scale_u")
            row.prop(uv_s, "scale_v")
        col.prop(uv_s, "use_grid_scale")
        col.operator("bh.triplanar_unwrap", text="Triplanar Unwrap")



addon_keymaps = []
classes = (BH_GridSettings, BH_GridScale, BH_GridScaleUp, BH_GridScaleDown, BH_AddonPreferences, BH_GridPanel, BH_TriplanarSettings, BH_TriplanarUnwrap)

def register():
    for i in classes:
        bpy.utils.register_class(i)

    bpy.types.Scene.grid_settings = bpy.props.PointerProperty(type=BH_GridSettings)
    bpy.types.Scene.triplanar_settings_props = bpy.props.PointerProperty(type=BH_TriplanarSettings)

    kc = bpy.context.window_manager.keyconfigs.addon
    
    if kc is not None:
        km = kc.keymaps.new(name= '3D View', space_type= 'VIEW_3D')

        kmi = km.keymap_items.new("bh.increase_grid_scale", type= "RIGHT_BRACKET", value= "PRESS")
        addon_keymaps.append((km, kmi))
        kmi.active = True

        kmi = km.keymap_items.new("bh.decrease_grid_scale", type= "LEFT_BRACKET", value= "PRESS")
        addon_keymaps.append((km, kmi))
        kmi.active = True


def unregister():
    del bpy.types.Scene.grid_settings
    del bpy.types.Scene.triplanar_settings_props
    for i in classes:
        bpy.utils.unregister_class(i)

    for km,kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()
