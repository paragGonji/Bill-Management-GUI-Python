# Bill-Management-GUI-Python

### Bill-Managemen t<br>

1. GUI :
   
![bill-input](https://github.com/user-attachments/assets/82eaf208-948b-48b1-97f0-e0bbef403855)

3. Bill :

![bill-output](https://github.com/user-attachments/assets/bd0f3953-6699-4ab6-8093-7781e49c4934)

The **Bill Management System** is a user-friendly software designed to help customers and staff manage food orders and generate bills in a canteen or cafeteria. The system allows users to place orders, and the canteen staff can calculate the total bill based on the items ordered. The system is built using Python and Tkinter, providing a simple yet effective interface for daily operations.

---

## Description

### Event Handling
- **"RESET"** button clears all the input fields.
- **"TOTAL"** button calculates the total cost based on the quantities entered for each menu item.

### Menu Items and Pricing
The system displays a menu with the following items and prices:
- **Dosa** - Rs. 60/plate
- **Cookies** - Rs. 30/plate
- **Tea** - Rs. 7/plate
- **Coffee** - Rs. 100/plate
- **Juice** - Rs. 20/plate
- **Pancakes** - Rs. 35/plate
- **Milk** - Rs. 7/plate

---

### Database Operations
The system currently does not include a database integration. However, it can be extended in the future to include a backend database for storing orders and bill information.

---

### Data Retrieval
- The **"Total"** button calculates the total cost of the ordered items based on the quantities entered.

---

### Result Display
- The total cost of the bill is displayed with a label in the right frame of the window.

---

## Installation

To run the **Bill Management System**, follow these steps:

1. Ensure that Python and Tkinter are installed on your local machine.
2. Save the provided Python code in a file named `bill_management_system.py`.
3. Run the script using the command:
   ```
   python bill_management_system.py
   ```
4. The application window will open, where you can enter quantities for each item and calculate the total bill.


## Usage
1. Open the application.
2. Enter the quantities for each menu item (Dosa, Cookies, Tea, Coffee, Juice, Pancakes, and Milk).
3. Click the "Total" button to calculate the total bill based on the prices and quantities entered.
4. Click the "Reset" button to clear all the input fields.

# Notes
Ensure that Tkinter is installed on your system. If it's not installed, you can install it using:
   ```
   pip install tk
   ```
