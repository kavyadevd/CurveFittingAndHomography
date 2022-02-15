#  Perception for Autonomous Robots
### Homework 1

The problem statement for this repository can be found [here](https://github.com/kavyadevd/Perception-673/blob/9ab28ab1edf35e4415fe6c4bffec4296c3584c36/Hw1/Homework1.pdf)

#### Problem 1 : Solution can be found in the project report [here](https://github.com/kavyadevd/Perception-673/blob/f4095aae2f2d635db8f864b22bbac588f8b0735a/Hw1/Report.pdf)

#### Problem 2 : Parabolic curve fitting using Standard Least Squares
##### Read data from video
```bash
python3 Kavya_hw1/Problem2/PythonCodes/GetData.py
```
Enter path to the csv file and input video when prompted <br>
This will generate two files a graph plot png images with coordinate plots and a csv file with ball x,y coordinates

##### Run linear least square
```bash
python3 Kavya_hw1/Problem2/PythonCodes/LSS.py
```
This will generate two graph plot png images, with curve fit output of two videos

>> Make sure the csv files and video files are in the same folder as the python code files
>> The code and output is also present in the jupyter notebooks present in the /Notebook folder


#### Problem 3 : Parabolic curve fitting using Standard Least Squares
##### Run the code using following command. Make sure the csv file is present in the same folder
```bash
python3 Kavya_hw1/Problem3/Insurance.py
```
Output can be seen on the terminal and the generated png images in the same folder

#### Problem 4 : Homography Matrix and SVD
##### Run the python code to execute SVD function and print the homography matrix using following command
```bash
python3 Kavya_hw1/Problem4/Homography.py
```
