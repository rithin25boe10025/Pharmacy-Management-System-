# Pharmacy Management System (Python)

A Python-based terminal application designed to help pharmacists identify medications, track inventory levels, and process sales with real-time stock updates. This tool demonstrates the practical application of software development within healthcare logistics.

## 📌 Features

* **Medicine Identifier**: Search the database by name to instantly retrieve price, current stock levels, and expiry dates.
* **Inventory Management**: Add new medications to the system or restock existing supplies.
* **Sales Processing**: Deduct stock automatically during a sale and calculate the total cost for the customer.
* **Pre-loaded Database**: Comes with a built-in inventory of common medicines including Paracetamol, Amoxicillin, Ibuprofen, and more.
* **Error Handling**: Includes validation to prevent system crashes when entering incorrect data types for prices or quantities.

## 🚀 How to Run

1.  **Prerequisites**: Ensure you have **Python 3.x** installed on your system.
2.  **Save the Code**: Save the script as `medicine_and_pharmacy_management.py`.
3.  **Open Terminal/PowerShell**: Navigate to the folder where you saved the file.
4.  **Execute**: Run the following command:
    ```powershell
    python "medicine_and_pharmacy_management.py"
    ```

## 📋 Usage Guide

Upon launching, the system presents a main menu with four options:
1.  **Search/Identify Medicine**: Enter the name of a drug to see its full details.
2.  **Add/Restock Medicine**: Input the name, price, quantity, and expiry date (YYYY-MM-DD) to update the inventory.
3.  **Sell Medicine**: Specify the quantity to sell; the system will verify if enough stock is available before completing the transaction.
4.  **Exit**: Safely close the application.

## 🛠️ Data Structure

The system utilizes a Python dictionary-based inventory for fast lookups:
* **Key**: Medicine Name (String)
* **Values**: Price (Float), Quantity (Integer), Expiry (String)

---

**Author: Rithin Bala B** 

**Reg No.: 25BOE10025**

**course: Python Essentials**

**Branch: B tech. Bioengineering**
