# Pybullet_Workshop
Pybullet workshop for batch of 2023 

## Installation For Task 2

We recommend you to go through the pybullet and OpenCV installation video before moving forward to setup the project. 

### STEP 1: Clone  repository using this command:
```bash
git clone https://github.com/ShashwatPatil/Pybullet_Workshop.git
```


### STEP 2: Change your current directory to the env's root.
```bash
cd Pybullet_Workshop/gym-line-follower-env/
```


### STEP 3: Install environment using command.
```bash
pip install -e .
```


#### Test your setup by running solution.py file.
#### There is also a description.py file, running which will introduce you to the env functions, arguments they need and their return types.
<hr>

## Objective

The goal is to make the robot car follow the line given in the arena by controlling the motors of the robot car. The movement of the robot has to be entirely autonomous. If the car comes back to its initial position after completing one lap of the track, the objective of the Task will be achieved.

## Using the Arena

1. Run the solution.py file. If you see the bot moving with forward velocity, Voila! Your installation is complete.

2. In solution.py, you'll see a working loop. You'll have to write the code to control the robot within this working loop. 

3. There are several functions in [helper.py](https://github.com/ShashwatPatil/Pybullet_Workshop/blob/main/gym-line-follower-env/gym_line_follower/helper.py) for you to navigate the arena. Their names and use cases are as follows: 

   - `husky.get_full_path()` 
     This function will return an array of the path. Each element of this array will have the x and y coordinates of the path at the 0th and 1st index. 
   - `husky.reset()` 
     Once this function is run, the present arena will be replaced with another with a new random path and the husky initilized to one of the points in this path. 
   - `husky.setvelocity([v, v])`
     Use this function to manipulate the velocity of the husky wheels. This function takes an array of two values. The value at 0th index will be the velocity of the front and rear left motors while the value at 1st indext will be the velocity of the front and rear right motors. 
   - `husky.getposition()`
     This function will return the x & y coordinates and the yaw angle of the robot. 

   You may look into the file to explore the working of these function and to add or remove functions of your own.
   

## Sample Use of Arena

 <p align="center">
  <img width="100%" src="https://i.imgur.com/yLoWS3F.gif" alt="Loading arena">
</p>

Note: this Arena is only for reference. The track is randomized and changes every time `husky.reset()` is run. 
