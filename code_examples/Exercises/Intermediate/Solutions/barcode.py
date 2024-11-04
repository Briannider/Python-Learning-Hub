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
    print(f"Calculated check digit: {check_calculated} (from result: {result})")
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
