class Ship:
    def __init__(self, ship_id, ship_name):
        self.ship_id = ship_id

        self.ship_name = ship_name


class CruiseShip(Ship):
    def __init__(self, ship_id, ship_name):


        super().__init__(ship_id, ship_name)


class CargoShip(Ship):
    def __init__(self, ship_id, ship_name):

        super().__init__(ship_id, ship_name)


class Customer:
    def __init__(self, customer_id, customer_name, contact):
        self.customer_id = customer_id
        self.customer_name = customer_name


        self.contact = contact


class Booking:
    def __init__(self, booking_id, ship, customer, amount):
        self.booking_id = booking_id
        self.ship = ship


        self.customer = customer

        self.amount = amount


class MarineManager:
    def __init__(self):
        self.bookings = []

    def add_booking(self, b):
        self.bookings.append(b)

    def total_amount_collected(self):
        total = 0.0
        for b in self.bookings:
            total += b.amount
        return total

    def get_amounts_by_ship(self):
        totals = {}
        for b in self.bookings:
            name = b.ship.ship_name
            
            totals[name] = totals.get(name, 0.0) + b.amount
        return totals

    def get_customers_by_cruise_ship(self, ship_name):
        seen = set()
        result = []
        for b in self.bookings:
            if isinstance(b.ship, CruiseShip) and b.ship.ship_name == ship_name:
                cid = b.customer.customer_id
                if cid not in seen:
                    seen.add(cid)

                    result.append(b.customer)
        return result
