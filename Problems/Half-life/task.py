initial_amount = int(input())
final_quantity = int(input())

half_life = 0
while initial_amount > final_quantity:
    initial_amount /= 2
    half_life += 12

print(half_life)