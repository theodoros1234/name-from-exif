# name-from-exif
This is a script that bulk renames jpg and mp4 files based on file metadata.

After recovering files from a corrupted SD card, none of them had their proper file names, so I quickly put this script together to change all the names of my photos and videos back to their original names. The name format matches Samsung's format on their Android camera app.

**Usage**
`$ python3 name-from-exif.py [file 1] [file 2] [file 3] [...]`
- `python3` can be ommited on Linux if the executable attribute is set for the script.
