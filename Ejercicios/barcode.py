"""
Exercise: Barcode Reading and Validation

In this exercise, you will write a Python program that simulates reading and validating barcodes using the EAN-13 format. 
The EAN-13 code is a standard 13-digit barcode. The first 12 digits represent product information, 
while the last digit is a check or control digit, which ensures that the code is correct.

Program Requirements:

1. Input:
   - The program should prompt the user to enter a 13-digit barcode.
   - If the code entered does not contain exactly 13 digits, display an error message and ask for the input again.

2. Check digit calculation:
   - The first 12 digits of the barcode are used to calculate the check digit. The calculation is done as follows:
     - Add the digits in odd positions (1, 3, 5, etc.).
     - Multiply the sum of the digits in even positions (2, 4, 6, etc.) by 3.
     - Add both results together.
     - The check digit is the number that must be added to this total to make it a multiple of 10.

3. Code validation:
   - The program should compare the calculated check digit with the last digit of the barcode entered by the user.
   - If the check digit matches, the program should output: `"Valid barcode"`.
   - If it does not match, it should output: `"Invalid barcode"`.

4. Example:
   - Input: `4006381333931`
   - Calculation: (4 + 0 + 6 + 8 + 1 + 3) + (0 + 6 + 3 + 3 + 3 + 9) * 3 = 22 + 72 = 94
   - Check digit: (94 + 6 = 100), so the code is valid.
   - Output: `"Valid barcode"`

---
This exercise will help you practice string manipulation, validation, and basic arithmetic operations in Python.
"""


def codechecker(barcode: str) -> bool:
    check = int(barcode[-1])  # Last digit is the check digit
    odd = 0  # Sum of digits at odd positions (1st, 3rd, 5th...)
    even = 0  # Sum of digits at even positions (2nd, 4th, 6th...)

    # Iterate through the first 12 digits (without the check digit)
    for i in range(len(barcode) - 1):
        if (
            i % 2 == 0
        ):  # Even index in Python corresponds to an odd position in the barcode
            odd += int(barcode[i])  # Odd positions are added directly
        else:
            even += int(barcode[i])  # Even positions are multiplied by 3

    # Calculate the total sum
    result = odd + even * 3

    # Calculate the check digit
    check_calculated = (10 - (result % 10)) % 10

    # Compare the calculated check digit with the actual check digit
    return check_calculated == check


barcode = ""
while True:
    barcode = str(input("Enter the barcode: "))
    if len(barcode) != 13:
        print("Invalid barcode. Please enter a 13-digit barcode.")
    else:
        print(f"{'Valid barcode' if codechecker(barcode) else 'Invalid barcode'}")
        break
