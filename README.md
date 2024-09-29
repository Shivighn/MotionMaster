# MotionMaster: Gamecontroller using Real-Time Face detection

This project aims to use the webcam or any other live video feed capturing devices to detect real-time human movements to be used as a game controller.

## Usage
1. Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/Shivighn/Motioncontroller.git
   ```
2. To view or run the code locally
     You can open the Motioncontroller.py in your personalized code editor.
   
4. To run it locally you need a few dependencies:
   - Python
   - openCV
   - Facecasscade file in openCv module (It is present in the repository)
   - pynput
   - NumPy
   - time

    You can download them using pip:
   ```
   pip install opencv-python pynput numpy time
   ```
   
5. To run it locally you need to open Motioncontroller.py
   Then in the 8th line of the code paste the Facecasscade file's location
   
6. Now the project has opened locally in your machine.
   Stand at least 2 meters from your webcam, and align your nose to the centre of the screen
   Now move right, left, jump or crouch in real-time to see the desired output in your terminal.

7. Now after this setup you can open your desired game and use this to play.
I recommend you play Subway Surfers first.

## Results
This model can also be further optimized and now it reads the inputs a little slowly and needs proper setup instructions.

## Contributions
This is my first project on computer vision which I developed during my 9th class.
I want to optimise and convert this code into a fully functioning project in the future.

I welcome contributions from the community. Feel free to suggest improvements, fixes, or new features through issues or pull requests.
