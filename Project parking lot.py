import random

class ParkingLot:
    def __init__(self, square_footage):
        self.square_footage = square_footage
        self.parking_spots = self.square_footage // 96
        self.lot = [None for i in range(self.parking_spots)]
    
    def park_car(self, car, spot):
        if self.lot[spot] is None:
            self.lot[spot] = car
            return True
        return False
    
    def map_cars(self):
        spots = {}
        for i, car in enumerate(self.lot):
            if car is not None:
                spots[i] = str(car)
        return spots

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate
    
    def __str__(self):
        return self.license_plate
    
    def park(self, lot, spot):
        success = lot.park_car(self, spot)
        if success:
            print(f"Car with license plate {self.license_plate} parked successfully in spot {spot}")
            return True
        print(f"Car with license plate {self.license_plate} was not parked successfully")
        return False

def main(cars, lot):
    while cars and None in lot.lot:
        car = cars.pop()
        parked = False
        while not parked:
            spot = random.randint(0, len(lot.lot) - 1)
            parked = car.park(lot, spot)

if __name__ == "__main__":
    cars = [Car(str(i)) for i in range(10)]
    lot = ParkingLot(1920)
    main(cars, lot)
    spots = lot.map_cars()
    print(spots)
