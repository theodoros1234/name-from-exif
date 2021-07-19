#!/bin/python3

import sys, os, PIL.Image, ffmpeg

# Go through each parameter/file
for path in sys.argv:
  # Check if file exists
  if os.path.isfile(path):
    # Get file extension
    ext = str()
    ext_pos = path.rfind('.')
    if ext_pos!=-1:
      ext = path[ext_pos+1:]
    
    # Find source directory if specified
    source_dir = str()
    slash_pos = path.rfind('/')
    if slash_pos!=-1:
      source_dir = path[0:slash_pos+1]
    
    # Decide what to do based on file extension
    if ext=='jpg':
      # Try to read image data from file
      try:
        img = PIL.Image.open(path)
        # Try to extract exif data from file
        try:
          exif_data = img._getexif()
          name = exif_data[36867]
          
          # Transform the aqcuired date/time data to a file name
          name = name[0:4]+name[5:7]+name[8:10]+'_'+name[11:13]+name[14:16]+name[17:19]+'.'+ext
          
          # Try to rename the file
          try:
            os.rename(path,source_dir+name)
            print("Renamed '%s' to '%s'."%(path[slash_pos+1:],name))
          except:
            print("Could not rename '%s' to '%s'."%(path[slash_pos+1:],name))
        except:
          print("Could not extract date/time exif data from '%s'."%(path))
      except:
        print("'%s' is not a valid image file."%(path))
    elif ext=='mp4':
      # Try to read video file
      try:
        vid = ffmpeg.probe(path)
        # Try to extract metadata from file
        try:
          metadata = vid['streams']
          name = vid['streams'][0]['tags']['creation_time']
          
          # Transform the aqcuired date/time data to a file name
          name = name[0:4]+name[5:7]+name[8:10]+'_'+name[11:13]+name[14:16]+name[17:19]+'.'+ext
          
          # Try to rename the file
          try:
            os.rename(path,source_dir+name)
            print("Renamed '%s' to '%s'."%(path[slash_pos+1:],name))
          except:
            print("Could not rename '%s' to '%s'."%(path[slash_pos+1:],name))
        except:
          print("Could not extract date/time metadata from '%s'."%(path))
      except:
        print("'%s' is not a valid video file'"%(path))
  else:
    # Decide which error message to show
    if os.path.isdir(path):
      print("'%s' is a directory."%(path))
    else:
      print("File '%s' doesn't exist."%(path))
