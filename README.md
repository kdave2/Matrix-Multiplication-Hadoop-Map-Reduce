# Matrix-Multiplication
Matrix Multiplication performed using Hadoop

This Repository contains the implementation of Matrix Multplication ran on Hadoop Using Map Reduce written in Python.


# Matrix_Mapper.py
This file contains the implementation of mapper. It maps keys according to the the matrix.
For Example, 

![screen shot 2018-01-11 at 5 17 39 am](https://user-images.githubusercontent.com/22648497/34820586-f5f6dc54-f68e-11e7-8b8d-6834079d6519.png)
   
   We provided this matrices in flatened format as in txt files as we cannot provide data as 2D Array.
   So the first element in Matrix A which refers to 1st row and 1st column which is 5 as follows :
   a,0,0,5
   where "a" represents matrix, "0" represents row number, "0" reprents column number which contains element "5".
   
   After execution of mapper we have keys arranged like:
   
   ![mapperkeysandvalue](https://user-images.githubusercontent.com/22648497/34820379-5ca48e2a-f68e-11e7-86e0-78474be2f236.png)
   
 # Matrix_Reducer.py
 
 This file contains the implementation of reducer. Here we reduce the output received from mapper into actual 2D array for matrices A and B and calculate the matrix multiplication based on usual formula.
 
 # MatrixMulOutput.txt
 This file shows the output of the resultant matrix obtained by multiplying matrix A and B in the format "(row,column) value"
 
# Run MapReduce Job

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input /user/cloudera/input -output /user/cloudera/MatrixMulOutput -mapper /home/cloudera/Matrix/Matrix_Mapper.py -reducer /home/cloudera/Matrix/Matrix_Reducer.py

Ouput of above command Will look as follows:

![consoleoutput1](https://user-images.githubusercontent.com/22648497/34822165-f5aa3e3a-f693-11e7-8142-dd37a71a8a72.png)

 
