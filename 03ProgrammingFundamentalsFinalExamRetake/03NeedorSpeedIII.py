number_cars = int(input())
cars = {}

for _ in range(number_cars):
    car, mileage, fuel = input().split("|")
    cars[car] = [int(mileage), int(fuel)]

while True:
    command = input()
    if command == "Stop":
        break

    command_args = command.split(" : ")
    action = command_args[0]
    car = command_args[1]

    if action == "Drive":
        distance = int(command_args[2])
        fuel = int(command_args[3])
        if fuel > cars[car][1]:
            print("Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car][0] >= 100000:
            cars.pop(car)
            print(f"Time to sell the {car}!")
    elif action == "Refuel":
        fuel = int(command_args[2])
        cars[car][1] += fuel
        if cars[car][1] > 75:
            fuel = 75 - (cars[car][1] - fuel)
            cars[car][1] = 75
        print(f"{car} refueled with {fuel} liters")
    elif action == "Revert":
        kilometers = int(command_args[2])
        cars[car][0] -= kilometers
        if cars[car][0] < 10000:
            cars[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car, details in cars.items():
    print(f"{car} -> Mileage: {details[0]} kms, Fuel in the tank: {details[1]} lt.")
