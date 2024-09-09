# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the descirption. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!


#options

# Custom calculator for travel distance and fuel consumption

# Prompt user for speed, time, and fuel efficiency
print("Enter the speed, time traveled, and fuel consumption to calculate the distance traveled and fuel used.")
speed = float(input("Speed of the car (e.g., in km/h or mph): "))
time = float(input("Time traveled (e.g., in hours): "))
fuel_efficiency = float(input("Fuel consumption (e.g., in liters per 100 km or miles per gallon): "))

# Option to specify units
distance_units = input("Distance units (e.g., kilometers, miles): ")
fuel_units = input("Fuel units (e.g., liters, gallons): ")

# Calculate the distance traveled and fuel used
distance_traveled = speed * time
fuel_used = (distance_traveled / 100) * fuel_efficiency

# Display the result
print(f"A car traveling at {speed} {distance_units} per hour for {time} hours will travel {distance_traveled:.2f} {distance_units}.")
print(f"It will consume approximately {fuel_used:.2f} {fuel_units} of fuel based on a fuel consumption rate of {fuel_efficiency} {fuel_units} per 100 {distance_units}.")
