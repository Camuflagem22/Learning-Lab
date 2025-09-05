This program was made to work with data from an ADXL345 acelerometer module for arduino. However, any acelerometer that is able to output the aceleration it's x, y and z axis should work.
At the time of writing (February 2024) the program is only able to calculate the norm of the aceleration vector. This means that it takes the x, y and z components as the dimentions of a paralelipipede, and calculates the lenght of it's diagonal.

To do so, the program takes a text file (inputdata.txt) as an input, where the acelerometer data is separated with  ; 
It is possible to change the separation character in the code itself. Simply edit the variable key at line 70.

The program also presents the option to save the data as an 'output.txt' file.

-------------------------------------------------------------------

> WHEN USING THE PROGRAM MAKE SURE THAT:

- The data file is named 'inputdata.txt' and it is in the same folder as the program;
- The components are in order x; y; z
- The value is either alone or starts with a letter, like x, y, z;
   Example: 0.75  or  x0.75
- The first line of the Data File is the first line with data;
- Each line has a maximum of 250 characters.
- You dont have any important file named output.txt

-------------------------------------------------------------------

> TEST DATA:

 The file 'inputdata.txt' present contains some test data you can use to test the program.

 Make sure to select up to 394 lines, and to input the 5th column.

-------------------------------------------------------------------

UPDATE: Added a Python Script to draw a line plot of the output data.


NOTE:  Project made in 2024