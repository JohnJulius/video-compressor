import ffmpeg

# Input and output video file paths
input_file_path = "video.mp4"
output_file_path = "output.mp4"

# Set the compression bitrate
bitrate = 1000000
resolution = "640x480"
fps=30
# Create the FFmpeg command
#command = ffmpeg.input(input_file_path).output(output_file_path, video_bitrate="100k", vf='scale=640:480').run()
command = ffmpeg.input(input_file_path).output(output_file_path, video_bitrate="100k", vf='scale=640:-1').run()
# Wait for the command to finish

command.wait()
