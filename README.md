# AI Trainer: Bicep Curl Rep Counter

Control your workout routine with an AI-powered trainer that counts your bicep curl reps in real-time using computer vision techniques!


## Description

This project is an AI-based trainer that counts the number of bicep curl repetitions you perform. The AI trainer uses a camera to track your arm movements and counts reps based on the angle of your arm during the exercise. The project is implemented using OpenCV and MediaPipe.

## Detecting Bicep Curl Reps

The AI trainer detects the following actions based on your arm's position and movement:

- **Start Position**: Arm extended.
- **Bicep Curl**: Arm curled towards your shoulder.
- **Rep Count**: Each full curl and return to start position is counted as one rep.

## Getting Started

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
https://github.com/helithd/AI-Personal-Trainer.git
```

### 2. Install the Required Libraries

Install the required libraries using the following command:

```bash
pip install -r requirements.txt
```
### 3. Run the Program

Run the program by executing the following command:

```bash
python AiTrainerProject.py
```
Note:
Ensure that the camera is connected to your computer.<br>
If you're not using the default camera, change the camera index in the cv2.VideoCapture() function in the AiTrainerProject.py file.

### Enjoy Your Workout! 💪😁