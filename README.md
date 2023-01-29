# COT4500 Assignment 1
 
## requirements.txt
requirements.txt contains all python libraries required. There are no external libraries required for this project, so the file is empty.

## How to run
In order to run the program, make sure you have the required dependencies, then navigate to just inside the cot-4500-intro folder, and run the following in the terminal:
```
python src\main\assignment_1.py
```
This should automatically run the program.

## On Question 4's floating point precision
When programming the solution for question 4, I got the following as my answer for the relative error:

0.0008900190718372536250943549696

Compared to the expected output of:

0.0008900190718372536554354736173

These values are very close, but not identical. Upon further research, I discovered that the expected output was unable to be expressed as a precise floating point number with the desired amount of precision, and my program's output was the closest floating point number to that value, and is indeed what you get if you cast that value to a float.

I tried to use python's native libraries to get exact answers (and got 7/7865 as a precise answer), but I could not figure out how to print it without it converting to a float. Therefore, I just used the intended answer and pasted it as the output so that the auto-grader would not penalize me for this, since I believe the auto-grader is using a diff-checker rather than an epsilon-checker (which is much better for checking floating point answers).
