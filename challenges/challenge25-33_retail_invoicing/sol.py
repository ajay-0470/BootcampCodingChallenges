"""Challenge25-33 Retail Invoicing"""


def challenge25():
    code = input("Item code: ").strip()
    desc = input("Description: ").strip()
    qty = int(input("Quantity: "))
    price = float(input("Price: "))
    total = qty * price
    return [code, desc, qty, price, total]

def challenge26():
    items = []
    n = int(input("Number of items: "))
    for i in range(n):
        items.append(challenge25())
    grand_total = sum(it[4] for it in items)
    return items, grand_total

def challenge27(grand_total, items):
    total_qty = sum(it[2] for it in items)
    if grand_total > 10000:
        d = 0.10 * grand_total
        grand_total -= d
        print("10% bulk discount: - Rupees", f"{d:.2f}")
    if total_qty > 20:
        d2 = 0.05 * grand_total
        grand_total -= d2
        print("5% quantity discount: - Rupees", f"{d2:.2f}")
    return grand_total

def challenge28(grand_total):
    member = input("Member (y/n): ").strip().lower()
    if member == 'y':
        m = 0.02 * grand_total
        grand_total -= m
        print("Member discount 2%: - Rupees", f"{m:.2f}")
    return grand_total

def challenge29(grand_total):
    if grand_total < 5000:
        rate = 0.05
    elif grand_total <= 20000:
        rate = 0.10
    else:
        rate = 0.15
    tax = rate * grand_total
    grand_total += tax
    print(f"Tax @ {int(rate*100)}%: + Rupees {tax:.2f}")
    return grand_total

def challenge30(grand_total, items):
    promo_sum = 0.0
    for it in items:
        if it[0].upper() == "PROMO10":
            disc = 0.10 * it[4]
            it[4] -= disc
            promo_sum += disc
    if promo_sum > 0:
        grand_total -= promo_sum
        print("PROMO10 total discount: - Rupees", f"{promo_sum:.2f}")
    return grand_total

def challenge31(grand_total):
    method = input("Payment method (Cash/Credit Card): ").strip().lower()
    if "card" in method:
        s = 0.02 * grand_total
        grand_total += s
        print("Credit card surcharge 2%: + Rupees", f"{s:.2f}")
    return grand_total

def challenge32(grand_total):
    if grand_total < 500:
        print("Final amount less than Rupees 500. Invoice not generated.")
        return False
    return True

def challenge33(grand_total):
    points = int(grand_total // 100)
    return points

def main():
    items, total = challenge26()
    total = challenge27(total, items)
    total = challenge28(total)
    total = challenge29(total)
    total = challenge30(total, items)
    total = challenge31(total)
    if not challenge32(total):
        return
    points = challenge33(total)


    print("\nInvoice:")
    for it in items:
        print(f"{it[0]} | {it[1]} | Qty:{it[2]} | Unit:{it[3]:.2f} | Line_Total:{it[4]:.2f}")
    print("Final Payable: Rupees", f"{total:.2f}")
    print("Loyalty points:", points)


main()
