# Medicine-Inventory-and-Expiry-Tracker
(Bangladesh Focus)

Overview

The Medicine Inventory and Expiry Tracker is a simple, command-line Python application designed to assist pharmacy staff or healthcare providers in managing their drug stock.
This project focuses on stock level and expiry date tracking, which are critical for patient safety and operational efficiency in a pharmacy setting. The initial inventory is pre loaded with over 50 common and a few specialized drugs frequently encountered in the Bangladeshi pharmaceutical market.

Features

Real-time Status Checking: Automatically checks and flags the status of each medicine based on the current date and stock level:
EXPIRED: The expiry date has passed.
Expiring Soon: The drug will expire within the next 90 days.
LOW STOCK: The stock count is below the defined threshold (default is 20 units).
OUT OF STOCK: The stock count is 0.
OK: Stock is healthy and the expiry date is far off.

Inventory Management: Allows users to view, add, and update stock counts for medicines.
Simple Command-Line Interface (CLI): Easy interaction via numbered menu options.
Pre-loaded Data: Includes a realistic initial dataset tailored to common prescribing patterns in Bangladesh.

How to Use

Prerequisites:
You only need Python 3 installed on your system. This script uses only standard Python modules (datetime) and requires no external libraries.
Save the Code:
Save the Python code provided in the next section into a file named medicine_inventory.py.
Run the Program:
Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script: medicine_inventory.py
