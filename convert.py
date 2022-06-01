import sys
import os
import cv2
import datetime

def convert_video_to_img(video_path, out_path):
	video = cv2.VideoCapture(video_path)
	video_fps = int(video.get(cv2.CAP_PROP_FPS))
	video_total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
	os.makedirs(os.path.join(out_path, "images"), exist_ok=True)
	
	start_time = datetime.datetime.now()
	with open(os.path.join(out_path, "timestamp.txt"), "w") as fp:
		for current_frame in range(video_total_frames):
			ret, img = video.read()
			if ret == False:
				print("Unable to convert all frames")
				break

			cv2.imwrite(os.path.join(out_path, "images", f"{current_frame:06}.png"), img)
			fp.write(f"{current_frame / video_fps}\n")
			duration = datetime.datetime.now() - start_time
			frame_rate = (current_frame + 1) / duration.total_seconds()
			print(f"  Converted {current_frame + 1}/{video_total_frames} frames (Remaining time: {(video_total_frames - current_frame - 1) / frame_rate:.2f}s ({frame_rate:.2f} frames/sec))", end="\r")
	print(f"\n  Saved to {out_path}")


if len(sys.argv) < 3:
	print("Usage: python3 convert.py [video path] [output directory path]")
	exit()

convert_video_to_img(sys.argv[1], sys.argv[2])
