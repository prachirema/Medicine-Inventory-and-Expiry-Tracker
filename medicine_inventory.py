import datetime

# Medicine Inventory List: Generic Name, Stock, and Expiry Date (YYYY-MM-DD)
# Expiry dates are set to demonstrate different status flags (expired, soon, OK).
inventory = [
    # Common Drugs in Bangladesh (Categories based on high-frequency prescription)

    # I. Gastrointestinal (Antiulcerants, Antiemetics)
    {"name": "Esomeprazole 20mg", "stock": 500, "expiry": "2026-03-01"},
    {"name": "Omeprazole 20mg", "stock": 120, "expiry": "2024-12-25"}, # Expiring Soon
    {"name": "Pantoprazole 40mg", "stock": 350, "expiry": "2025-09-10"},
    {"name": "Domperidone 10mg", "stock": 600, "expiry": "2026-07-20"},
    {"name": "Metoclopramide 10mg", "stock": 250, "expiry": "2025-04-15"},
    {"name": "Tiemonium Methyl Sulphate 50mg", "stock": 80, "expiry": "2026-01-05"},
    {"name": "Oral Rehydration Salts (ORS) Pkt", "stock": 1500, "expiry": "2027-04-01"},
    {"name": "Loperamide 2mg", "stock": 90, "expiry": "2024-03-01"}, # EXPIRED
    {"name": "Aluminum Hydroxide Gel", "stock": 15, "expiry": "2025-06-01"}, # Low Stock

    # II. Pain & Inflammation (Analgesics & NSAIDs)
    {"name": "Paracetamol 500mg", "stock": 1500, "expiry": "2027-10-01"},
    {"name": "Ibuprofen 200mg", "stock": 250, "expiry": "2024-12-10"}, # Expiring Soon
    {"name": "Diclofenac Sodium 50mg", "stock": 110, "expiry": "2025-11-01"},
    {"name": "Ketorolac 10mg", "stock": 45, "expiry": "2026-02-28"},
    {"name": "Etoria 90mg (Etoricoxib)", "stock": 0, "expiry": "2025-05-30"}, # Out of Stock
    {"name": "Tramadol 50mg", "stock": 70, "expiry": "2026-05-01"},
    {"name": "Codeine Linctus 100ml", "stock": 12, "expiry": "2024-03-25"}, # EXPIRED

    # III. Antibiotics & Anti-Infectives
    {"name": "Cefixime 200mg", "stock": 400, "expiry": "2026-06-15"},
    {"name": "Amoxicillin 500mg", "stock": 750, "expiry": "2025-01-01"}, # Expiring Soon
    {"name": "Amoxi-Clav (625mg)", "stock": 180, "expiry": "2025-09-01"},
    {"name": "Azithromycin 500mg", "stock": 300, "expiry": "2026-04-20"},
    {"name": "Ciprofloxacin 500mg", "stock": 420, "expiry": "2025-02-10"},
    {"name": "Metronidazole 400mg", "stock": 650, "expiry": "2027-01-01"},
    {"name": "Flucloxacillin 500mg", "stock": 55, "expiry": "2025-08-01"},
    {"name": "Cefuroxime 500mg", "stock": 200, "expiry": "2026-09-01"},
    {"name": "Doxycycline 100mg", "stock": 150, "expiry": "2025-10-10"},
    {"name": "Fluconazole 150mg", "stock": 80, "expiry": "2027-03-01"},
    {"name": "Albendazole 400mg", "stock": 100, "expiry": "2026-11-01"},

    # IV. Cardiovascular & Diabetes
    {"name": "Amlodipine 5mg", "stock": 550, "expiry": "2026-12-31"},
    {"name": "Losartan 50mg", "stock": 380, "expiry": "2025-03-20"},
    {"name": "Atenolol 50mg", "stock": 95, "expiry": "2025-07-01"},
    {"name": "Lisinopril 10mg", "stock": 85, "expiry": "2026-08-01"},
    {"name": "Furosemide 40mg", "stock": 130, "expiry": "2025-10-25"},
    {"name": "Metformin 500mg", "stock": 700, "expiry": "2027-05-01"},
    {"name": "Atorvastatin 10mg", "stock": 210, "expiry": "2026-04-10"},
    {"name": "Rosuvastatin 5mg", "stock": 30, "expiry": "2025-11-20"}, # Low Stock
    {"name": "Aspirin 75mg", "stock": 900, "expiry": "2027-02-01"},
    {"name": "Clopidogrel 75mg", "stock": 160, "expiry": "2025-06-25"},
    {"name": "Isosorbide Mononitrate 20mg", "stock": 10, "expiry": "2024-11-01"}, # Low Stock / Expiring Soon

    # V. Vitamins, Supplements & Respiratory
    {"name": "B1/B6/B12 Tab", "stock": 800, "expiry": "2027-08-01"},
    {"name": "Calcium + Vitamin D3 Tab", "stock": 1100, "expiry": "2026-10-01"},
    {"name": "Zinc Sulphate 20mg", "stock": 450, "expiry": "2027-01-15"},
    {"name": "Ferrous Fumarate Tab", "stock": 60, "expiry": "2025-05-01"},
    {"name": "Salbutamol 2mg", "stock": 140, "expiry": "2025-03-10"},
    {"name": "Montelukast 10mg", "stock": 280, "expiry": "2026-03-25"},
    {"name": "Cetirizine 10mg", "stock": 350, "expiry": "2027-06-01"},
    {"name": "Fexofenadine 120mg", "stock": 200, "expiry": "2025-12-01"},
    {"name": "Ambroxol Syrup 100ml", "stock": 180, "expiry": "2026-05-15"},
    {"name": "Dexamethasone 0.5mg", "stock": 50, "expiry": "2024-02-01"}, # EXPIRED
    {"name": "Prednisolone 5mg", "stock": 40, "expiry": "2025-01-20"},
    {"name": "Thyroxine 50mcg", "stock": 90, "expiry": "2026-04-01"},
    {"name": "Ondansetron 4mg", "stock": 100, "expiry": "2025-07-20"},
    {"name": "Clonazepam 0.5mg", "stock": 25, "expiry": "2024-12-01"},

    # VI. Other Common Drugs (Total 53 Common Drugs)
    {"name": "Gliclazide 80mg", "stock": 110, "expiry": "2026-02-15"},
    {"name": "Levofloxacin 500mg", "stock": 70, "expiry": "2025-08-20"},
    {"name": "Atova (Atorvastatin 10mg)", "stock": 20, "expiry": "2025-11-01"},
    {"name": "Clobetasol Cream 10g", "stock": 18, "expiry": "2024-10-10"}, # Low Stock

    # VII. Rare/Specialized Drugs (4 Rare Drugs)
    {"name": "Elexacaftor/Teza/Ivacaftor (CF Combo)", "stock": 5, "expiry": "2026-06-30"}, # Rare Genetic Disorder Drug
    {"name": "Imatinib 400mg (TKI)", "stock": 8, "expiry": "2025-05-15"}, # Specialized Cancer Drug
    {"name": "Interferon Beta-1a Injection (MS)", "stock": 2, "expiry": "2024-12-05"}, # Rare Autoimmune Biologic
    {"name": "Lonafarnib 50mg (Progeria Treatment)", "stock": 1, "expiry": "2025-04-01"}, # Extremely Rare Disease Drug
]

# Set the low stock threshold
LOW_STOCK_THRESHOLD = 20

 

def get_status(item):
    """
    Checks the expiry and stock status of an item.
    Returns the most critical status: EXPIRED > LOW STOCK > Expiring Soon > OK.
    """
    expiry_date_str = item["expiry"]
    stock = item["stock"]
    
    try:
        # Convert the expiry string ('YYYY-MM-DD') into a datetime object
        expiry_date = datetime.datetime.strptime(expiry_date_str, "%Y-%m-%d").date()
        today = datetime.date.today()
        time_to_expiry = expiry_date - today
        
        # 1. Check for Expiry
        if time_to_expiry.days <= 0:
            return "🔴 EXPIRED"
        
        # 2. Check for Stock (Out of Stock)
        if stock <= 0:
            return "⚫ OUT OF STOCK"

        # 3. Check for Stock (Low Stock)
        if stock <= LOW_STOCK_THRESHOLD:
            return "🟠 LOW STOCK"

        # 4. Check for items Expiring Soon (within 90 days)
        if time_to_expiry.days <= 90:
            return "🟡 Expiring Soon"
        
        # 5. Default Status
        return "🟢 OK"
            
    except ValueError:
        return "⚠ Invalid Date Format"


def view_inventory():
    """Displays all items in the inventory with their status."""
    print("\n" + "="*85)
    print("🇧🇩 PHARMACY INVENTORY & EXPIRY TRACKER (BANGLADESH DRUGS)")
    print(f"REPORT DATE: {datetime.date.today().strftime('%Y-%m-%d')} | LOW STOCK THRESHOLD: {LOW_STOCK_THRESHOLD}")
    print("="*85)
    
    # Header
    print(f"{'No.':<4}{'Medicine Name':<45}{'Stock':<10}{'Expiry Date':<15}{'Status':<15}")
    print("-" * 85)
    
    # Iterate through the list and print details for each medicine
    for i, item in enumerate(inventory):
        # Determine the final status
        status = get_status(item)
        
        print(f"{i+1:<4}{item['name']:<45}{item['stock']:<10}{item['expiry']:<15}{status:<15}")
    
    print("-" * 85)
    print(f"Total Unique Items: {len(inventory)}")


def update_inventory():
    """Allows the user to update the stock count of an existing medicine."""
    view_inventory()
    
    while True:
        try:
            # Prompt user to select a number from the list
            selection = input("\nEnter the *No.* of the medicine to update stock (or '0' to cancel): ")
            if selection == '0':
                return
            
            index = int(selection) - 1
            
            # Validate the user's input index
            if 0 <= index < len(inventory):
                item = inventory[index]
                print(f"\nCurrently updating: *{item['name']}* (Current Stock: {item['stock']})")
                
                new_stock = int(input("Enter the *NEW* stock quantity: "))
                if new_stock < 0:
                    print("Error: Stock cannot be negative.")
                    continue
                
                # Update the stock and confirm
                item["stock"] = new_stock
                # Re-check status after update
                new_status = get_status(item)
                print(f"✅ Success! {item['name']} stock updated to {item['stock']}. New Status: {new_status}")
                break
            else:
                print("❌ Invalid number. Please enter a number from the list.")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")


def add_new_medicine():
    """Allows the user to add a new medicine to the inventory."""
    print("\n--- ➕ ADD NEW MEDICINE ---")
    
    # Get all required inputs from the user
    name = input("Enter medicine name (e.g., Generic + Dose): ").strip()
    
    while True:
        try:
            stock = int(input("Enter initial stock quantity: "))
            if stock < 0:
                 print("Stock cannot be negative.")
                 continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for stock.")
    
    while True:
        expiry_str = input("Enter expiry date (YYYY-MM-DD): ").strip()
        try:
            # Validate date format by trying to convert it
            datetime.datetime.strptime(expiry_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD (e.g., 2025-01-01).")

    # Create the new dictionary and add it to the global list
    new_item = {
        "name": name,
        "stock": stock,
        "expiry": expiry_str
    }
    inventory.append(new_item)
    print(f"\n✅ Success! *'{name}'* added to inventory.")


# ----------------- 3. Main Program Loop (User Interface) -----------------

def main_menu():
    """Displays the main menu and handles user commands."""
    
    # Get today's date to display in the menu
    today_date = datetime.date.today().strftime("%Y-%m-%d")
    
    while True:
        print("\n\n" + "="*35)
        print("MEDICINE INVENTORY TRACKER")
        print(f"DATE: {today_date}")
        print("="*35)
        print("1. View Current Inventory & Status")
        print("2. Update Medicine Stock")
        print("3. Add New Medicine")
        print("4. Exit Program")
        print("-" * 35)
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            view_inventory()
        elif choice == '2':
            update_inventory()
        elif choice == '3':
            add_new_medicine()
        elif choice == '4':
            print("\n👋 Exiting the system. Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 4.")

# Run the main program
if _name_ == "_main_":
    main_menu()