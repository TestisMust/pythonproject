def inches_to_feet(inches):
    return inches / 12

def feet_to_inches(feet):
    return feet * 12

def feet_to_yards(feet):
    return feet / 3

def yards_to_feet(yards):
    return yards * 3

def meters_to_feet(meters):
    return meters * 3.281

def feet_to_meters(feet):
    return feet / 3.281

def main():
    print("Measurement Converter")
    print("---------------------")
    print("1. Inches to Feet")
    print("2. Feet to Inches")
    print("3. Feet to Yards")
    print("4. Yards to Feet")
    print("5. Meters to Feet")
    print("6. Feet to Meters")
    print("---------------------")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        inches = float(input("Enter length in inches: "))
        feet = inches_to_feet(inches)
        print("Length in feet:", feet)
    elif choice == "2":
        feet = float(input("Enter length in feet: "))
        inches = feet_to_inches(feet)
        print("Length in inches:", inches)
    elif choice == "3":
        feet = float(input("Enter length in feet: "))
        yards = feet_to_yards(feet)
        print("Length in yards:", yards)
    elif choice == "4":
        yards = float(input("Enter length in yards: "))
        feet = yards_to_feet(yards)
        print("Length in feet:", feet)
    elif choice == "5":
        meters = float(input("Enter length in meters: "))
        feet = meters_to_feet(meters)
        print("Length in feet:", feet)
    elif choice == "6":
        feet = float(input("Enter length in feet: "))
        meters = feet_to_meters(feet)
        print("Length in meters:", meters)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
