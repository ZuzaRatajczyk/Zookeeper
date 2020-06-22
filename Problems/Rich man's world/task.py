initial_deposit = int(input())

num_of_years = 0
while initial_deposit < 700000:
    initial_deposit += (0.071 * initial_deposit)
    num_of_years += 1
print(num_of_years)