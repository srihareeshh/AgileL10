def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    print("\n   Temperature Converter   ")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Exit")
    
    choice = input("Enter your choice (1-2): ")
    
    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C is equal to {f}°F")
    elif choice == '2':
        print("Goodbye!")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
