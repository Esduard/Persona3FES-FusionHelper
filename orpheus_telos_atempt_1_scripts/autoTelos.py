from tensorflow.keras.models import load_model
import pyautogui
import os
import time
import pydirectinput
import time
import pyautogui
import numpy as np
import pickle
from PIL import Image
import logging
import pygetwindow as gw
import logging
import sys

# Create a logger object
logger = logging.getLogger(__name__)

# Set the log level
logger.setLevel(logging.INFO)

# Create a file handler
handler = logging.FileHandler('predictions.log')

# Add the handler to the logger
logger.addHandler(handler)



class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def __str__(self):
        return f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})"
        


class InferenceRunner():
    def __init__(self, model_path, label_encoder_path):
        self.model = load_model(model_path)
        with open(label_encoder_path, 'rb') as f:
            self.le = pickle.load(f)
        # rectangle list
        
        self.rectangle_list = []

        x = 490
        y = 988
        width = 1007 - 490
        height = 1060 - 990

        for i in range(4):
            rec = Rectangle(x,y + (76 * i), width, height)
            self.rectangle_list.append(rec)

        x = 1019
        for i in range(4):
            rec = Rectangle(x,y + (76 * i), width, height)
            self.rectangle_list.append(rec)

    def run_inference(self):
        images = []
        
        for rectangle in self.rectangle_list:
            # Take a screenshot of the rectangle
            cropped_img = pyautogui.screenshot(region=(rectangle.x, rectangle.y, rectangle.width, rectangle.height))

            # Convert the image to RGB
            rgb_img = cropped_img.convert('RGB')

            hex_color = '65dfcd'

            # Convert the target hex color to RGB
            target_r, target_g, target_b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            target_color = np.array([target_r, target_g, target_b])

            # Convert the image to a NumPy array
            img_array = np.array(rgb_img)

            # Calculate the Euclidean distance between each pixel's color and the target color
            color_distance = np.linalg.norm(img_array - target_color, axis=2)

            # Create a mask for pixels that are similar to the target color
            mask = color_distance < 65

            # Change the color of the pixels based on the mask
            img_array[mask] = [0, 0, 0]  # black
            img_array[~mask] = [255, 255, 255]  # white

            # Convert the NumPy array back to an image
            rgb_img = Image.fromarray(img_array)

            # Convert the image to grayscale
            gray_img = rgb_img.convert('L')

            # Apply a threshold to make it binary
            binary_img = gray_img.point(lambda x: 0 if x<128 else 255, '1')

            img_array = np.array(binary_img)
            
            images.append(img_array)
        
        # Convert the list of images to a numpy array
        images = np.array(images)

        # Use the model to make predictions
        predictions = self.model.predict(images,verbose=0)

        # Decode the predictions to their original form
        decoded_predictions = self.le.inverse_transform([np.argmax(prediction) for prediction in predictions])
        #print(decoded_predictions)
        return decoded_predictions



class SkillVerifier:
    def __init__(self, mandatory_skills, optional_skills):
        self.mandatory_skills_set = set(mandatory_skills)
        self.optional_skills_set = set(optional_skills)
        self.skills_aquired = [False]*6

        for i in range(6):
            if i == 2 or i == 3:
                 self.skills_aquired[i] = True

        self.dictonary_number_key = { 
            1 : 'f6',
            2 : 'f7',
            3 : 'f8',
            4 : 'f9',
            5 : 'f10',
        }

    def verify_skills(self, predictions):
        predictions_set = set(predictions)

        if self.mandatory_skills_set.issubset(predictions_set):
            logger.info('mandatory set found')
            if not self.skills_aquired[0]:
                pydirectinput.keyDown('f5')
                pydirectinput.keyUp('f5')
                self.skills_aquired[0] = True

            n = len(self.optional_skills_set & predictions_set)
            if n >= 1:
                logger.info(f'{n} optional skills found')
                if not self.skills_aquired[n]:
                    pydirectinput.keyDown(self.dictonary_number_key[n])
                    pydirectinput.keyUp(self.dictonary_number_key[n])
                    self.skills_aquired[n] = True

                    if n == 5:
                        return True
        return False

'''

'''

class MainJob():

    def __init__(self):
        # skill verifier

        mandatory_skills = [
            'High Counter',
            'Unshaken Will',
            'Panta Rhei',
            ]

        optional_skills = [
            'Wind Boost',
            'Wind Amp',
            'Spell Master',
            'Mind Charge',
            'Salvation',
        ]

        self.verifier = SkillVerifier(mandatory_skills, optional_skills)

        # inferencer

        self.inferencer = InferenceRunner('my_model.h5', 'label_encoder.pkl')

        # active window
        self.active_window_title = None

    def check_window_change(self):
        # Check if the active window has changed
        if gw.getActiveWindow().title != self.active_window_title:
            print('Active window has changed. Stopping the program.')
            return True
        return False
    
    def check(self):
        # Inside your class method or function
        if self.check_window_change():
            sys.exit()
    
    def timer(self,seconds):
        # Start a 5-second timer
        for i in range(seconds, 0, -1):
            print(f"Remaining: {i} seconds")
            time.sleep(1)

    def change(self):
        self.check()
        pydirectinput.keyDown('f4')
        pydirectinput.keyUp('f4')

        # Press the 'l' key
        self.check()
        pydirectinput.press('l')
        #print('l key pressed')

        # Wait for 0.1 seconds
        time.sleep(0.01)

        # Press the 'm' key
        self.check()
        pydirectinput.press('m')
        #print('m key pressed')
        
        time.sleep(0.01)

        self.check()
        pydirectinput.keyDown('f4')
        pydirectinput.keyUp('f4')

    def run(self):
        self.timer(10)
        # Press the F4 key
        #pydirectinput.keyDown('f4')
        #pydirectinput.keyUp('f4')
        # Get the title of the currently active window
        self.active_window_title = gw.getActiveWindow().title
        while True:
            if self.check_window_change():
                break
            predictions = self.inferencer.run_inference()
            # Log the predictions vector
            logger.info(f'{predictions}')
            if self.verifier.verify_skills(predictions):
                print('found')
                pydirectinput.keyDown('esc')
                pydirectinput.keyUp('esc')
                print('esc key pressed')
                break
            if self.check_window_change():
                break
            self.change()

if __name__ == "__main__":
    main_job = MainJob()
    main_job.run()