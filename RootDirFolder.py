import os
import config
from FolderVideoCompress import folderVideoCompress
from pathlib import Path
import datetime # Added to prevent script running too long
import ffmpeg
def rename_files(directory):
    """Renames all files in a directory and its subdirectories.
    Args:
        directory: The directory to rename files in.
     """
    now = datetime.datetime.now()
    hours_run_allowed = now - datetime.timedelta(hours=17)
    to_delete = True
    folder_path = Path(directory)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_extension = os.path.splitext(file)[1]
            # os.rename(old_path, new_path)
            #print(os.path.join(root, file))
            # pass the path to the FPC Function if filetype match
            if now > hours_run_allowed: # Added condition to limit script for over running a given period
                file_name = os.path.splitext(file)[0]
                file_extension = os.path.splitext(file)[1]
                # Create the new file name
                #output_file_path = file + "_" + current_date.strftime("%Y-%m-%d") + file_extension
                output_file_name = file_name + "_min" + file_extension
                # Create the FFmpeg command type mp4 (customize here to your video format)
                input_file_path = root+"\\"+file
                if file_extension == '.mp4' and file_name[-4:] != '_min' :
                    video_streams = ffmpeg.probe(input_file_path, select_streams = "v")
                    print(video_streams)
                    w=video_streams['streams'][0]['width'] # get width
                    h=video_streams['streams'][0]['height'] # get height
                    if (w/2)%2 != 0 or (h/2)%2 != 0:
                        vf_conf = 'fps=25,scale=1280:720'
                    else: 
                        vf_conf = 'fps=25,scale=1280:720'
                        
                    output_file_path = root+"\\"+output_file_name
                    command = ffmpeg.input(input_file_path).output(output_file_path, video_bitrate="100k", vf=vf_conf).run()
                    # Rename the file
                    #os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, output_file_path))
                    # Delete file when done
                    if to_delete:
                        os.remove(input_file_path)
                elif file_name[-4:] != '_min' and file_extension!='.jpg' :
                    os.remove(input_file_path)
            else:
                break
                # Future Reference
                # old_path = os.path.join(root, file)
                # new_path = os.path.join(root, file.replace(" ", "_"))

if __name__ == "__main__":
    folder_path_dir = config.dir_D
    
    rename_files(folder_path_dir)