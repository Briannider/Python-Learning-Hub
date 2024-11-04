# Exercise: Barcode Reading and Validation
## Input

* The program should prompt the user to enter a 13-digit barcode.
* If the code entered does not contain exactly 13 digits, display an error message and ask for the input again.

## Check digit calculation

* The first 12 digits of the barcode are used to calculate the check digit.
* The calculation is done as follows:
  * Add the digits in odd positions (1, 3, 5, etc.).
  * Multiply the sum of the digits in even positions (2, 4, 6, etc.) by 3.
  * Add both results together.
  * The check digit is the number that must be added to this total to make it a multiple of 10.

## Code validation

* The program should compare the calculated check digit with the last digit of the barcode entered by the user.
* If the check digit matches, the program should output: `"Valid barcode"`.
* If it does not match, it should output: `"Invalid barcode"`.

## Example

* Input: `4006381333931`
* Calculation: (4 + 0 + 6 + 8 + 1 + 3) + (0 + 6 + 3 + 3 + 3 + 9) * 3 = 22 + 72 = 94
* Check digit: (94 + 6 = 100), so the code is valid.
* Output: `"Valid barcode"`
