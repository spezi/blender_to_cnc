#----------------------------------------------------------
# File blender_to_cnc.py
#----------------------------------------------------------

import bpy
 
#
#    Menu in UI region
#

bpy.types.Object.myRnaInt = IntProperty(
    name="flat rotate", 
    min = -360, max = 360,
    default = 0)

class UIPanel(bpy.types.Panel):
    bl_label = "blender to cnc export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    def draw(self, context):
        self.layout.operator("hello.hello", text='Servus')
      
#
#    The Hello button prints a message in the console
#
class OBJECT_OT_HelloButton(bpy.types.Operator):
    bl_idname = "hello.hello"
    bl_label = "Say Hello"
    country = bpy.props.StringProperty()
    
    def execute(self, context):
        if self.country == '':
            print("Hello world!")
        else:
            print("Hello world from %s!" % self.country)
        return{'FINISHED'}    
      
#
#	Registration
#   All panels and operators must be registered with Blender; otherwise
#   they do not show up. The simplest way to register everything in the
#   file is with a call to bpy.utils.register_module(__name__).
#
 
bpy.utils.register_module(__name__)
