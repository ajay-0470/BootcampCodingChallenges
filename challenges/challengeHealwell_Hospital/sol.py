
# Admin configuration
services = [
    "General Consultation",
    "Blood Test",
    "X-Ray",
    "MRI Scan",
    "ECG",
    "Ultrasound",
    "Physiotherapy",
    "Vaccination",
    "Pharmacy"
]
costs = [1000.00, 500.00, 2000.00, 5000.00, 1500.00, 1200.00, 800.00, 200.00, 300.00]

def get_patient_details():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")
    contact = input("Enter patient contact number: ")
    return name, age, gender, contact

def select_services(services):
    print("\nAvailable Services:")
    for i, service in enumerate(services, start=1):
        print(f"{i}. {service}")
    choices = input("Enter service numbers (comma-separated): ")
    
    selected_indices = [int(num.strip()) - 1 for num in choices.split(',') if num.strip().isdigit()]
    return selected_indices

def get_selected_costs(indices, services, costs):
    selected_services = []
    selected_costs = []
    for idx in indices:
        if 0 <= idx < len(services):
            selected_services.append(services[idx])
            selected_costs.append(costs[idx])
    return selected_services, selected_costs

def calculate_subtotal(cost_list):
    return sum(cost_list)

def apply_discounts(subtotal, age):
    discount = 0.0
    total_after = subtotal
    # Senior citizen discount
    if age >= 60:
        senior_discount = 0.10 * total_after
        total_after -= senior_discount
        discount += senior_discount
    # Additional discount if over 5000
    if total_after > 5000:
        extra_discount = 0.05 * total_after
        total_after -= extra_discount
        discount += extra_discount
    return total_after, discount

def calculate_gst(total):
    gst_amount = 0.18 * total
    grand_total = total + gst_amount
    return gst_amount, grand_total

def generate_invoice(name, age, gender, contact, services_selected, costs_selected, subtotal, discount, gst, grand_total):
   
    print("\n HealWell Care Hospital Invoice")
    print(f"Patient Name: {name}")
    print(f"Age: {age}    Gender: {gender}    Contact: {contact}")
    print("\nServices Availed:")
    for svc, cost in zip(services_selected, costs_selected):
        print(f"  - {svc}: Rupees{cost:.2f}")
    print("")
    print(f"Subtotal: Rupees{subtotal:.2f}")
    if discount > 0:
        print(f"Discount: -Rupees{discount:.2f}")
    print(f"GST @ 18%: Rupees{gst:.2f}")
    print(f"Grand Total: Rupees{grand_total:.2f}")
    print("End")

def main():
   
    name, age, gender, contact = get_patient_details()

    selected_indices = select_services(services)
   
    services_selected, costs_selected = get_selected_costs(selected_indices, services, costs)
  
    subtotal = calculate_subtotal(costs_selected)
   
    total_after_discounts, total_discount = apply_discounts(subtotal, age)
    
    gst_amount, grand_total = calculate_gst(total_after_discounts)
  
    generate_invoice(name, age, gender, contact, services_selected, costs_selected, subtotal, total_discount, gst_amount, grand_total)


main()
