class Car:
    def __init__(self, max_speed, speed_unit):
        self.max_speed = max_speed
        self.speed_unit = speed_unit
        for i in range(n-1):
            if self.speed_unit:
                print("Car with maximum speed of", max_speed, speed_unit)
class Boat:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        print("Boat with the maximum speed of", max_speed, "knots")
global n
n = int(input("Enter total number of times cars should be print and one boat:"))
for i in range(n-1):
    car,sp = input("car and speed unit:").split()
boat = int(input("boat speed:"))
c =Car(car,sp)
b=Boat(boat)
