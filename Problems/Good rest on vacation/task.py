# put your python code here
duration = int(input())
day_food_cost = int(input())
total_food_cost = duration * day_food_cost
flight_cost = int(input())
one_night_cost = int(input())
num_of_nights = duration - 1
total_hotel_cost = one_night_cost * num_of_nights

print(total_food_cost + (flight_cost * 2) + total_hotel_cost)