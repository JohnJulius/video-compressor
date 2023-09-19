import os
import config
import datetime
from pathlib import Path
import ffmpeg

# Get the current date
current_date = datetime.date.today()
# Set to True if Delete Input file after convert
to_delete = True
# Get the path to the folder containing the files to rename
folder_path_dir = config.dir_C
folder_path = Path(folder_path_dir)
# Get a list of all files in the folder
files = os.listdir(folder_path)
# Set the compression bitrate
bitrate = 1000000
# Iterate over the files and rename them
for file in files:
    # Get the file extension
    file_name = os.path.splitext(file)[0]
    file_extension = os.path.splitext(file)[1]
    # Create the new file name
    #output_file_path = file + "_" + current_date.strftime("%Y-%m-%d") + file_extension
    output_file_name = file + "_min" + file_extension
    # Create the FFmpeg command type mp4 (customize here to your video format)
    if file_extension == '.mp4':
        input_file_path = folder_path_dir+"\\"+file
        output_file_path = folder_path_dir+"\\"+output_file_name
        command = ffmpeg.input(input_file_path).output(output_file_path, video_bitrate="100k", vf='scale=640:-1').run()
        # Rename the file
        #os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, output_file_path))
        # Delete file when done
        if to_delete:
            os.remove(input_file_path)
    else:
        # Delete file that is not the specified format
        if to_delete:
            os.remove(folder_path_dir+"\\"+file)

def folderVideoCompress(fpd):
    # Set to True if Delete Input file after convert
    to_delete = True
    # Get the path to the folder containing the files to rename
    folder_path_dir = fpd
    folder_path = Path(folder_path_dir)
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    # Set the compression bitrate
    bitrate = 1000000
    # Iterate over the files and rename them
    for file in files:
        # Get the file extension
        file_name = os.path.splitext(file)[0]
        file_extension = os.path.splitext(file)[1]
        # Create the new file name
        #output_file_path = file + "_" + current_date.strftime("%Y-%m-%d") + file_extension
        output_file_name = file + "_min" + file_extension
        # Create the FFmpeg command type mp4 (customize here to your video format)
        if file_extension == '.mp4':
            input_file_path = folder_path_dir+"\\"+file
            output_file_path = folder_path_dir+"\\"+output_file_name
            command = ffmpeg.input(input_file_path).output(output_file_path, video_bitrate="100k", vf='scale=640:-1').run()
            # Rename the file
            #os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, output_file_path))
            # Delete file when done
            if to_delete:
                os.remove(input_file_path)
        else:
            # Delete file that is not the specified format
            if to_delete:
                os.remove(folder_path_dir+"\\"+file)