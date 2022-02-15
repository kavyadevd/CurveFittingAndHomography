## Line fitting using Standard Least Square, total least square and RANSAC
Here, we try to minimize error and fit a line for Age vs Insurance cost [data](https://github.com/kavyadevd/Perception-673/blob/a58e6276af46583ed1a361a21b7016bfc0a8846b/Hw1/Problem3/dataset.csv)
with outliers.

### Covariance matrix, its eigenvalues and eigenvectors
Part one is generating the covariance matrix for the dataset and visualizing it's eigen vectors on a plot as follows
![DataPlotWithEigenVectors](https://user-images.githubusercontent.com/13993518/154086161-9f3353d1-bd4b-4fa6-9d41-8bd5cdd659be.png)

### Linear least square method
To fit the line using Linear least square method, we minimise the error E:<br>
<img src="https://render.githubusercontent.com/render/math?math=E(a, b)=\sum_{n=1}^{N}\left(y_{n}-\left(a x_{n}+b\right)\right)^{2}">

By differentiating this and equating to zero, we get the following linear equations in a and b:<br>

<img src="https://render.githubusercontent.com/render/math?math=\left(\sum_{n=1}^{N} x_{n}^{2}\right) a+\left(\sum_{n=1}^{N} x_{n}\right) b &=\sum_{n=1}^{N} x_{n} y_{n}\left(\sum_{n=1}^{N} x_{n}\right) a+\left(\sum_{n=1}^{N} 1\right) b &=\sum_{n=1}^{N} y_{n}">

The solution can be obtained by easily solving the above two equations for a and b and plotting
the thus obtained equation of the line
![LLS](https://user-images.githubusercontent.com/13993518/154086010-fe22f0ae-87d2-490f-8fc4-0014ee93c06a.png)

### Total least square
Total least square considers errors in all the variables and hence provides a relatively robust model when the data has error in both directions.

To fit the line using Linear least square method, we minimise the error E:<br>
<img src="https://render.githubusercontent.com/render/math?math=E=\sum_{i=1}^{n}\left(a x_{i}+b y_{i}-d\right)^{2}">

### RANSAC
In RANSAC, we select any two random points of data and try to fit the line using any of the above
two methods. The error is calculated for these points. This is done in a number of iterations and the
line with minimum errors is selected.
RANSAC successfully eliminates outliers by comparing the error to a pre-described threshold value,
any point with an error greater than the threshold is eliminated
![RANSAC](https://user-images.githubusercontent.com/13993518/154088288-4a57032d-dbf4-4d58-b594-ddda0905fee7.png)
