import sys
import site
import subprocess
from pathlib import Path

import bpy

def add_user_site_path():
    # packages maybe installed in user site
    # in default, user site are not used in blender
    user_site = site.getusersitepackages()
    # print('user site:', user_site)
    if user_site is not None and user_site not in sys.path:
        sys.path.append(user_site)
    # print(sys.path)


def install_packages(req_file):

    # Ensure pip exists and get path to python executable
    if bpy.app.version[0] == 2 and bpy.app.version[1] < 81:
        # pip is not enabled in blender with version < 2.81
        py_path = Path(sys.prefix) / 'bin'
        py_exec = str(next(py_path.glob('python')))

        if subprocess.call([py_exec, '-m', 'ensurepip']) != 0:
            raise ImportError("Coundn't activate pip")
    else:
        try:
            import pip
        
        except ModuleNotFoundError as e:
            print('Failed to import pip:', e)

            try:
                import ensurepip
                ensurepip.bootstrap()
            except:
                e = sys.exc_info()[0]
                raise Exception(f'Bootstrap Failed: {e}')

        py_exec = bpy.app.binary_path_python

    # Upgrade pip
    try:
        print('Try upgrade pip')
        output = subprocess.check_output([py_exec, '-m', 'pip', 'install', '--upgrade', 'pip'])
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(e.output)
        raise Exception("Couldn't update pip. Please restart Blender and try again")

    # Install required packages
    try:
        print('Try to install required packages')
        output = subprocess.check_output([py_exec, '-m', 'pip', 'install', '-r', req_file])
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(e.output)
        raise Exception("Failed to install required packages")

    # Log installed packages
    output = subprocess.check_output([py_exec, '-m', 'pip', 'list'])
    print(output.decode('utf-8'))

