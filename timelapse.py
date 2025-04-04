import os
import time
from datetime import datetime
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
import cv2

def create_timelapse():
    # Create main timelapse directory if it doesn't exist
    if not os.path.exists('timelapses'):
        os.makedirs('timelapses')
   
    # Create a unique folder for this session
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_dir = os.path.join('timelapses', f'timelapse_{timestamp}')
    photos_dir = os.path.join(session_dir, 'photos')
   
    os.makedirs(photos_dir, exist_ok=True)
   
    print(f"Session directory: {session_dir}")
   
    # Initialize the camera
    picam2 = Picamera2()
    config = picam2.create_still_configuration(main={"size": (1080, 1920)})
    picam2.configure(config)
   
    # Start the camera
    picam2.start()
   
    frame_count = 0
   
    print("Press 'q' to stop capturing and create timelapse...")
   
    try:
        while True:
            # Capture image
            frame_count += 1
            filename = os.path.join(photos_dir, f"frame_{frame_count:04d}.jpg")
            picam2.capture_file(filename)
            print(f"Captured {filename}")
           
            # Check for 'q' key press
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == ord('Q'):
                break
           
            # Adjust delay between captures (e.g., 1 second)
            time.sleep(3)
   
    finally:
        # Stop the camera
        picam2.stop()
       
        # Create timelapse video if we captured any frames
        if frame_count > 0:
            print("Creating timelapse video...")
            video_filename = os.path.join(session_dir, f"timelapse_{timestamp}.mp4")
           
            # Use ffmpeg to create the video
            os.system(f"ffmpeg -framerate 30 -pattern_type glob -i '{photos_dir}/frame_*.jpg' -c:v libx264 -pix_fmt yuv420p -crf 20 {video_filename}")
           
            print(f"Timelapse video created: {video_filename}")
        else:
            print("No frames captured. No video created.")

if __name__ == "__main__":
    create_timelapse()
