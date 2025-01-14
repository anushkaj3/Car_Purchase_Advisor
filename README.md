
# Car Purchase Advisor System

## Description
This project implements a **Car Purchase Advisor System** for a car retailer using Python. It interacts with two data files, `stock.txt` and `order.txt`, located in the `data` folder. The program provides a text-based interface for customers to perform various tasks such as finding the nearest car retailer, getting purchase advice, and placing orders.

---

## Features

### Automatic Test Data Generation
When the program starts, test data is automatically generated to populate the `stock.txt` file with a randomized list of available cars. This data is also loaded into the program memory to facilitate operations. The format follows the provided example, ensuring consistency.

### Intuitive Menu System
Upon launching the program, users are presented with a menu that allows them to:
- Find the nearest car retailer.
- Get tailored car purchase advice.
- Place car orders.
- Exit the program.

### Finding the Nearest Car Retailer
By entering their postcode, users can locate the closest car retailer. The program calculates proximity based on the numerical difference between postcodes, assuming smaller differences indicate closer locations.

### Tailored Car Purchase Advice
Users can select a retailer from a list of options to receive personalized car purchase advice. The system provides:
1. **Car Recommendations**: Randomly selects and suggests a car from the retailer's stock.
2. **Full Stock Overview**: Displays all available cars at the selected retailer.
3. **Filtered Search by Type**: Lists cars based on specific types (e.g., `AWD`, `RWD`).
4. **Probationary Licence Options**: Highlights cars suitable for probationary licence holders.

Each output is well-formatted, displaying retailer details and stock information in an organized manner.

### Streamlined Car Ordering Process
The program enables users to place car orders by providing a retailer ID and car ID. Before processing an order, the system ensures:
- The retailer is open (based on current business hours).
- The provided IDs are valid.

If the order is valid, it is recorded in `order.txt`, and the details are displayed to the user. In case of errors, the program provides meaningful feedback.

---

## Getting Started

### Prerequisites
- Python 3.6 or higher
