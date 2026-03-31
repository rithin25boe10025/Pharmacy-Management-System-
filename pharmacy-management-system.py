import datetime

class PharmacySystem:
    def __init__(self):
        # Database structure with more medicines
        self.inventory = {
            "Paracetamol": {"price": 5.50, "quantity": 100, "expiry": "2026-12-01"},
            "Amoxicillin": {"price": 12.00, "quantity": 50, "expiry": "2025-06-15"},
            "Ibuprofen": {"price": 8.75, "quantity": 75, "expiry": "2027-01-20"},
            "Cetirizine": {"price": 4.25, "quantity": 120, "expiry": "2026-08-10"},
            "Metformin": {"price": 15.00, "quantity": 60, "expiry": "2026-03-25"},
            "Azithromycin": {"price": 22.50, "quantity": 30, "expiry": "2025-11-12"},
            "Vitamin D3": {"price": 18.00, "quantity": 200, "expiry": "2027-05-01"},
            "Omeprazole": {"price": 10.50, "quantity": 45, "expiry": "2026-10-30"}
        }

    def add_medicine(self):
        print("\n--- Add New Stock ---")
        name = input("Enter Medicine Name: ")
        try:
            price = float(input("Enter Price: "))
            qty = int(input("Enter Quantity: "))
            expiry = input("Enter Expiry Date (YYYY-MM-DD): ")
            
            if name in self.inventory:
                self.inventory[name]['quantity'] += qty
                print(f"Updated {name} stock. Total now: {self.inventory[name]['quantity']}")
            else:
                self.inventory[name] = {"price": price, "quantity": qty, "expiry": expiry}
                print(f"Added {name} to inventory.")
        except ValueError:
            print("Error: Please enter numbers for Price and Quantity.")

    def identify_medicine(self):
        print("\n--- Search Medicine ---")
        name = input("Enter name to search: ")
        med = self.inventory.get(name)
        if med:
            print(f"Details for: {name}")
            print(f"Price: ${med['price']} | Stock: {med['quantity']} | Expiry: {med['expiry']}")
        else:
            print(f"Medicine '{name}' not found.")

    def sell_medicine(self):
        print("\n--- Process Sale ---")
        name = input("Which medicine are you selling? ")
        med = self.inventory.get(name)
        if med:
            try:
                qty = int(input(f"How many units? (Available: {med['quantity']}): "))
                if med['quantity'] >= qty:
                    med['quantity'] -= qty
                    total = qty * med['price']
                    print(f"Sale successful! Total Cost: ${total:.2f}")
                    print(f"Remaining {name} stock: {med['quantity']}")
                else:
                    print("Error: Not enough stock available.")
            except ValueError:
                print("Error: Please enter a valid number for quantity.")
        else:
            print("Error: Medicine not found.")

# --- Main Program Logic ---
def main():
    pharmacy = PharmacySystem()
    
    while True:
        print("\n================================")
        print("   PHARMACY MANAGEMENT SYSTEM   ")
        print("================================")
        print("1. Search/Identify Medicine")
        print("2. Add/Restock Medicine")
        print("3. Sell Medicine (Update Stock)")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ")

        if choice == '1':
            pharmacy.identify_medicine()
        elif choice == '2':
            pharmacy.add_medicine()
        elif choice == '3':
            pharmacy.sell_medicine()
        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
