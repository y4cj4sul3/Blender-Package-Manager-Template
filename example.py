# This is a test script for testing 3rd-party packages can be imported properly
import cv2

import bpy


class ExampleOperator(bpy.types.Operator):
    bl_idname = 'example.test_package'
    bl_label = 'Test Package'
    bl_options = {'REGISTER'}

    def execute(self, context):

        try:
            return {'FINISHED'}
        except:
            return {'CANCELED'}
