# Exercise Statement: Number Sequence Solver

**Objective:** This application solves the following task:

A computer starts by printing the numbers **2023**, **2024**, and **2025**. Then, without stopping, it continues printing the sum of the three most recent numbers it has printed, such as **6072**, **10121**, **18218**, and so on.

Your challenge is to determine what the last four digits of the number printed in position **2023202320232023** are. 

To illustrate, in position **50**, the printed number is **8188013234823360**, which ends in **3360**.

## Instructions:
- Implement a function named `find_last_4_digits(target_position: int) -> int` that returns the last four digits of the number printed in the specified position.
- The function should utilize the initial numbers and the rule of summing the last three printed numbers to generate the sequence.
- Print the last four digits of the number in the specified position.
