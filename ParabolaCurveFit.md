
## Parabolic curve fitting using Standard Least Squares
In this case, we read video files of a red ball following a parabolic path and try to fit a curve along it's trajectory using least square method.
To test the least square error minimization, we are testing the code for noiseless data (video1) and data with noise (video2)

### Computing Standard least square
The equation of parabola is $y = a + bx + cx^2$. Here, we need to find the variables a, b, c such that the error is minimum. The error function can be written as:
<br>
 <img src="https://render.githubusercontent.com/render/math?math=\Pi=\sum_{i=1}^{n}\left[y_{i}-f\left(x_{i}\right)\right]^{2}=\sum_{i=1}^{n}\left[y_{i}-\left(a+b x_{i}+c x_{i}^{2}\right)\right]^{2}">
<br>
To minimize the error, the unknown variables must have zero derivatives. Hence:<br>
<img src="https://render.githubusercontent.com/render/math?math=\sum_{i=1}^{n} y_{i}=a +b \sum_{i=1}^{n} x_{i}+c \sum_{i=1}^{n} x_{i}^{2}">

<img src="https://render.githubusercontent.com/render/math?math=\sum_{i=1}^{n} x_{i} y_{i}=a \sum_{i=1}^{n} x_{i}+b \sum_{i=1}^{n} x_{i}^{2}+c \sum_{i=1}^{n} x_{i}^{3}">

<img src="https://render.githubusercontent.com/render/math?math=\sum_{i=1}^{n} x_{i}^{2} y_{i}=a \sum_{i=1}^{n} x_{i}^{2}+b \sum_{i=1}^{n} x_{i}^{3}+c \sum_{i=1}^{n} x_{i}^{4}">

Next step is to solve the above three linear equations and get values for a, b, c.
The code and result can be found [here](https://github.com/kavyadevd/Perception-673/blob/0b46f2f48e2dc5124fb2d1e6531fe902121b7fa1/Hw1/Problem2/LSS.ipynb)

### Executing code
Navigate to /Problem2 directory
##### Read data from video
```bash
python3 /Problem2/PythonCodes/GetData.py
```
Enter path to the csv file and input video when prompted <br>
This will generate two files a graph plot png images with coordinate plots and a csv file with ball x,y coordinates


https://user-images.githubusercontent.com/13993518/154081757-a830fa56-599d-4582-b896-5e7b4ca4547a.mp4

![video1plot](https://user-images.githubusercontent.com/13993518/153971170-d725cc8b-d468-40a5-a33f-1f29e5590ebf.png)

https://user-images.githubusercontent.com/13993518/154081853-77470c4f-c768-4381-b50b-4bf258d23b9e.mp4

![video2plot](https://user-images.githubusercontent.com/13993518/153971258-db84f542-3ca9-4d50-98cf-ca6decf7b310.png)


##### Run linear least square
```bash
python3 /Problem2/PythonCodes/LSS.py
```
This will generate two graph plot png images, with curve fit output of two videos

![curvefit1](https://user-images.githubusercontent.com/13993518/153971307-f941bf47-ba01-4057-b561-724a4848e4c5.png)

![curvefit2](https://user-images.githubusercontent.com/13993518/153971268-97f58856-63a8-431d-8f2e-ee2a60dabcbd.png)
