# Matrix-Multiplication
Matrix Multiplication performed using Hadoop

This Repository contains the implementation of Matrix Multplication ran on Hadoop Using Map Reduce written in Python.


# Matrix_Mapper.py
This file contains the implementation of mapper. It maps keys according to the the matrix.
For Example, 

Input Matrices =

   [ 5	3	1 ]
A= |-2	3	-1|
   |7	 1 	-1|
   [0  1	 1]

   [5	 9	2	3	-4 ]
B= |5	 2	-6	3	9|
   [-10	0	3	-9	7]
   
   We provided this matrices in flatened format as in txt files as we cannot provide data as 2D Array as follows:
   So the first element in Matrix A which refers to 1st row and 1st column 5 as - a,0,0,5
   where a represents matrix, 0 represents row number, 0 reprents column number which contains 5.
   
   After execution of mapper we have keys arranged like:
   
   ![mapperkeysandvalue](https://user-images.githubusercontent.com/22648497/34820379-5ca48e2a-f68e-11e7-86e0-78474be2f236.png)
