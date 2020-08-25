# put your python code here
duration_in_days = int(input())
food_cost_day = int(input())
flight_cost = int(input())
hotel_cost = int(input())
print((food_cost_day * duration_in_days) + (hotel_cost * (duration_in_days - 1)) + (flight_cost * 2))
