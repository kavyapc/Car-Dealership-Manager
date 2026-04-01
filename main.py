from car import Car
from database import (initialize_database, import_cars, add_car, get_all_cars,
                      get_car_by_id, update_car, delete_car, search_cars)

def show_menu():
    print("\n" + "="*40)
    print("   🚗  CAR DEALERSHIP MANAGER")
    print("="*40)
    # Print options 1–6 here
    # Return the user's input
    print("1. Add a new car")
    print("2. View all cars")
    print("3. Update a car")
    print("4. Delete a car")
    print("5. Search cars")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    return choice

def add_car_flow():
    try:
        make = input("Enter make: ")
        model = input("Enter model: ")
        year = int(input("Enter year: "))
        price = float(input("Enter price: "))
        mileage = int(input("Enter mileage (km): "))

        car = Car(make, model, year, price, mileage)
        add_car(car)

        print(f"\nCar added successfully! New car ID: {car.id}")

    except ValueError:
        print("\nInvalid input. Please enter valid input.")


def view_all_cars_flow():
    cars = get_all_cars()
   
    if not cars:
        print("\nNo cars in inventory.")
    else:
        print("\nCars in inventory:")
        for car in cars:
            print(car)

def update_car_flow():
    try:
        car_id = int(input("Enter the ID of the car to update: "))

        car = get_car_by_id(car_id)

        if car is None:
            print("\nCar not found.")
            return

        print("\nCurrent car details:")
        print(car)
        print("\nPress Enter to keep the current value.\n")

        new_make = input(f"Make [{car.make}]: ")
        if new_make:
            car.make = new_make

        new_model = input(f"Model [{car.model}]: ")
        if new_model:
            car.model = new_model

        new_year = input(f"Year [{car.year}]: ")
        if new_year:
            car.year = int(new_year)

        new_price = input(f"Price [{car.price}]: ")
        if new_price:
            car.price = float(new_price)

        new_mileage = input(f"Mileage [{car.mileage}]: ")
        if new_mileage:
            car.mileage = int(new_mileage)

        update_car(car)

        print("\nCar updated successfully!")
        print(car)

    except ValueError:
        print("\nInvalid input. Please enter valid numbers for ID, year, price, and mileage.")


def delete_car_flow():
    try:
        car_id = int(input("Enter the ID of the car to delete: "))

        car = get_car_by_id(car_id)

        if car is None:
            print("\nCar not found.")
            return

        print("\nCar to delete:")
        print(car)

        confirm = input("\nAre you sure you want to delete this car? (y/n): ").lower()

        if confirm == "y":
            if delete_car(car_id):
                print("\nCar deleted successfully.")
            else:
                print("\nCould not delete the car.")
        else:
            print("\nDeletion cancelled.")

    except ValueError:
        print("\nInvalid input. Please enter a valid car ID.")

def search_cars_flow():
    keyword = input("Enter a make, model, or year to search for: ").strip()

    results = search_cars(keyword)

    print(f"\nFound {len(results)} car(s).")

    if not results:
        print("No matching cars found.")
    else:
        print("\nMatching cars:\n")
        for car in results:
            print(car)

def main():
    initialize_database()
    import_cars()

    while True:
        choice = show_menu()

        if choice == "1":
            add_car_flow()

        elif choice == "2":
            view_all_cars_flow()

        elif choice == "3":
            update_car_flow()

        elif choice == "4":
            delete_car_flow()

        elif choice == "5":
            search_cars_flow()

        elif choice == "6":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()