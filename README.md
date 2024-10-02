# Join Objects by Distance
- Blender (4.2) Add-on
- Iterates through all selected objects and joins them individually if the distance is within the set threshold.
- Optionally: set origin to object center before joining.

![Imgur Image](https://imgur.com/J7ZYE51.png)

## ***How to Install***

1. Download the ZIP file from the [latest release page](https://github.com/milanwulf/object_join_by_distance/releases/latest).
2. Open Blender -> Edit -> Preferences -> Add-ons.
3. Click the "Install" button, browse to the download location of the ZIP file, and click "Install from Disk".
4. The Add-on should now appear in the Add-ons list as "Join Objects by Distance".

## ***How to Use***

1. Select multiple objects that you want to join into one.
2. Press <kbd>J</kbd> on your keyboard.
3. A property panel will appear in the lower left corner after pressing <kbd>J</kbd>.
4. Set the desired minimum ***Distance*** to define how close objects need to be to join.
5. Check ***Set Origin to Object center first*** if the object's origin is not placed in the center of the objects.

## ***History***

- **v0.1**: Initial version.
- **v0.2**: Fixed a bug where the script was not performing enough operations (forgot to remove a break).
- **Forked v0.3**: The original code has been optimized and a manifest added to ensure compatibility with Blender 4.2.

## ***Credits***

This version is a fork of the original add-on created by [leBluem](https://github.com/leBluem/object_join_by_distance). The code has been optimized and updated for compatibility with Blender 4.2.
