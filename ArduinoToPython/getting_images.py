from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
import os

class CameraApp(App):
    def build(self):
        self.capture = cv2.VideoCapture(1)  # Use the appropriate camera index
        self.frame_count = 0
        self.output_folder = 'output_images_2'
        
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
            
        Clock.schedule_interval(self.update, 1.0 / 30)  # Update every 30 frames per second
        return Image()

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            self.frame_count += 1
            if self.frame_count % 30 == 0:  # Save every 30 frames (1 second)
                image_filename = os.path.join(self.output_folder, f"image_{self.frame_count // 30}.jpg")
                cv2.imwrite(image_filename, frame)
            
            self.root.texture = self.convert_frame_to_texture(frame)

    def convert_frame_to_texture(self, frame):
        frame_texture = Texture.create(size=(frame.shape[1], frame.shape[0]))
        frame_texture.blit_buffer(frame.tobytes(), colorfmt='bgr', bufferfmt='ubyte')
        return frame_texture

    def on_stop(self):
        self.capture.release()

if __name__ == '__main__':
    CameraApp().run()
