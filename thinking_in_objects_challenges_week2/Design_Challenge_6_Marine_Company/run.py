"""
Design Challenge 6: Marine Company
A marine company has many ships with them. Ship are either cruise type, or cargo type. Some
register to a particular ship to travel from one place to another or to send the cargo from one place
to another. Design the OO model for the above problem statement and implement the
code to
• Total amount been collected.
• List the total amount for every ship
• List all the customer details for a particular cruise ship
"""
from marine import (
    CruiseShip,
    CargoShip,
    Customer,
    Booking,
    MarineManager,
)

cruise_aurora = CruiseShip(1, "Aurora")


cruise_tides = CruiseShip(2, "Tides Voyager")

cargo_triton = CargoShip(3, "Titanic")

c1 = Customer(1, "A B", "ab@mail.com")

c2 = Customer(2, "C D", "cd@mail.com")

c3 = Customer(3, "E F", "ef@mail.com")

b1 = Booking(1, cruise_aurora, c1, 250.0)
b2 = Booking(2, cruise_aurora, c2, 300.0)
b3 = Booking(3, cruise_tides, c3, 220.0)
b4 = Booking(4, cruise_aurora, c1, 150.0)  
b5 = Booking(5, cargo_triton, c2, 500.0)    

manager = MarineManager()
for b in (b1, b2, b3, b4, b5):
    manager.add_booking(b)

print("Total amount collected:", manager.total_amount_collected())

print("\nTotal amount per ship:")
for ship_name, amt in manager.get_amounts_by_ship().items():
    print("-", ship_name + ":", "Rupees: " + f"{amt:.2f}")

print("\nCustomers for cruise ship 'Aurora':")
for cust in manager.get_customers_by_cruise_ship("Aurora"):
    print("-", cust.customer_name, f"(ID:{cust.customer_id})", "-", cust.contact)
