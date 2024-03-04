import os
import cv2
import time

def play_video(video_path):
    cap = cv2.VideoCapture(video_path)

    # Get the screen resolution
    screen_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    screen_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create a full-screen window
    cv2.namedWindow('Video Slideshow', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Video Slideshow', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame to fit the screen
        frame = cv2.resize(frame, (screen_width, screen_height))

        # Display the frame
        cv2.imshow('Video Slideshow', frame)

        # Wait for a few milliseconds before displaying the next frame
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def read_first_character( file_path):
        with open(file_path, 'r') as file:
           
            return file.read()


def slideshow_with_videos(folder_path,catgory):
    print( catgory)
    video_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')) and f.startswith(catgory)]
    print(video_files)
    for video_file in video_files:
        video_path = os.path.join(folder_path, video_file)
        print(f"Playing video: {video_path}")
        play_video(video_path)
        time.sleep(0.01)  # Add a delay between videos

if __name__ == "__main__":
    folder_path = r'C:\Users\Amal\Downloads\Gender-and-Age-Detection-master\adds\vid'  # Replace with the actual path to your video folder
    slideshow_with_videos(folder_path,read_first_character(r"C:\Users\Amal\Downloads\Gender-and-Age-Detection-master\first_characters.txt"))
