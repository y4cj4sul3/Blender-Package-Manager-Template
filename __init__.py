import bpy

bl_info = {
    'name': 'Blender Package Manager Template',
    'author': 'y4cj4sul3',
    'version': (1, 0),
    'blender': (2, 93, 3),
    'description': 'A Blender Addon template using 3rd-party python packages',
    'category': 'Development'
}


# Try to import modules
try:
    # add user site packages path to sys path
    from .package_manager import add_user_site_path
    add_user_site_path()

    # try import other scripts or 3rd-part packages
    print('Try to import modules')
    from . import example

except ModuleNotFoundError as e:
    print('Module Not Found:', e)

    # install packages
    import os
    from .package_manager import install_packages
    req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')
    install_packages(req_file)

    # import packages again
    print('Try to import modules again')
    from . import example

classes = [
    example.ExampleOperator
]

def register():
    # Uncomment this try except for development
    # try:
    #     print('Try to reload modules')
    #     import importlib
    #     importlib.reload(example)
    # except ModuleNotFoundError as e:
    #     print('Module Not Found:', e)

    #     # install packages
    #     import os
    #     from .package_manager import install_packages
    #     req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')
    #     install_packages(req_file)
    #     import importlib
    #     importlib.reload(example)
        
    #     print('Try to reload modules again')
    #     importlib.reload(example)

    for c in classes:
        bpy.utils.register_class(c)


def unregister():

    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == '__main__':
    register()
