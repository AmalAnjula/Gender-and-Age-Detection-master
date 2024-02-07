import os
import tkinter as tk
from PIL import Image, ImageTk

class SlideshowApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Slideshow")
        self.attributes("-fullscreen", True)  # Open in full-screen mode
        self.current_slide = tk.Label(self)
        self.current_slide.pack(expand=True, fill="both")
        self.first_character = self.read_first_character('first_characters.txt')  # Replace with the actual path to your character file
        self.image_paths = self.load_images(r'C:\Users\Amal\Downloads\Gender-and-Age-Detection-master\adds', self.first_character)  # Replace with the actual path to your image folder
        self.current_image_index = 0
        self.max_images = 5  # Set the maximum number of images to display
        self.image_counter = 0  # Counter for displayed images
        self.display_image()

    def read_first_character(self, file_path):
        with open(file_path, 'r') as file:
             
            return file.read()

    def load_images(self, folder_path, first_character):
        image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')) and f.startswith(first_character)]
        return [os.path.join(folder_path, image_file) for image_file in image_files]

    def display_image(self):
        if self.image_counter < self.max_images:
            image_path = self.image_paths[self.current_image_index]
            img = Image.open(image_path)
            img = img.resize((self.winfo_screenwidth(), self.winfo_screenheight()), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.current_slide.config(image=photo)
            self.current_slide.image = photo
            self.after(1000, self.next_image)
            self.image_counter += 1
        else:
            # After displaying the specified number of images, close the application
            self.destroy()

    def next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.display_image()

if __name__ == "__main__":
    app = SlideshowApp()
    app.mainloop()
