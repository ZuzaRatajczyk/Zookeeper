# Save the input in this variable
ticket = (input())
first_digit = int(ticket[0])
second_digit = int(ticket[1])
third_digit = int(ticket[2])
fourth_digit = int(ticket[3])
fifth_digit = int(ticket[4])
sixth_digit = int(ticket[5])


# Add up the digits for each half
half1 = first_digit + second_digit + third_digit
half2 = fourth_digit + fifth_digit + sixth_digit

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")