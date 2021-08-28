# Blender Package Manager Template

This template shows how to install 3rd-party python package in Blender addon.

## Installation
### Requirements
- Blender (This template only tested on Blender 2.93.3)
  
### Install Add-on
1. Download the `zip` file or clone and compress the folder.
2. Open Blender and go to `Edit > Preference > Add-ons`. Click `Install...` and select the compressed file.
3. Check the check box to enable addon. It should take a some time to install packages for the first time.

## Usage
### Add Packages
List the required packages in the `requirements.txt` file. In default, packages will only be checked and installed on Blender starts. To check for packages everytime the addon enabled, uncomment the try/except in the `register` in `__init__.py`.

### Log
Logs can be found in `Window > Toggle System Console`.