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

![video1plot](https://user-images.githubusercontent.com/13993518/153971170-d725cc8b-d468-40a5-a33f-1f29e5590ebf.png)
![video2plot](https://user-images.githubusercontent.com/13993518/153971258-db84f542-3ca9-4d50-98cf-ca6decf7b310.png)


##### Run linear least square
```bash
python3 Kavya_hw1/Problem2/PythonCodes/LSS.py
```
This will generate two graph plot png images, with curve fit output of two videos

![curvefit1](https://user-images.githubusercontent.com/13993518/153971307-f941bf47-ba01-4057-b561-724a4848e4c5.png)

![curvefit2](https://user-images.githubusercontent.com/13993518/153971268-97f58856-63a8-431d-8f2e-ee2a60dabcbd.png)


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
