Retail Shopping– Hackathon Retail Shopping Application with Enhanced Rules
You are tasked with developing a retail shopping application for generating itemized invoices,
applying business rules for discounts, surcharges, and quantities, and providing a seamless customer
experience. The application unfolds across levels, each introducing new functionality, culminating in
a complete solution that includes invoice generation and a breakdown of purchases.
Coding Challenge 25: Basic Item Entry and Total Calculation
Objective: Allow the user to input item details (code, description, quantity, price) and calculate the
total cost for the item.
Key Steps:
1. Accept item code, description, quantity, and price.
2. Compute the total for a single item.
3. Display the total for the item.
Coding Challenge 26: Iterative Item Entry and Grand Total
Objective: Enable multiple items to be added iteratively, and compute the grand total for all items.
Key Steps:
1. Use a loop to accept details for multiple items.
2. Compute the grand total by summing individual totals.
3. Display the grand total after all items have been entered.
Coding Challenge 27: Applying Discounts
Objective: Introduce business rules for modifying the grand total based on conditions.
Rules Implemented:
1. Discount: If the grand total exceeds ₹10,000, apply a 10% discount.
2. Quantity Discount: If the total quantity exceeds 20, apply an additional 5% discount on the
grand total (after other discounts).
Key Steps:
1. Check conditions for discounts.
2. Adjust the grand total accordingly.
3. Display the modified total with adjustments explained.
Coding Challenge 28: Membership Discounts
Objective: Introduce a membership system where customers get an additional discount.
Rules Implemented:
1. If the customer is a member (choice: 'y'), apply an additional 2% discount on the grand total
after all other adjustments.
Key Steps:
1. Prompt the user for membership status.
2. Apply the membership discount if applicable.
3. Update and display the final grand total.


Coding Challenge 29: Tax Calculation Based on Purchase Amount
Objective: Introduce tiered tax rates based on the grand total.
Rules Implemented
1. If the grand total is below ₹5,000, apply 5% tax.
2. If the grand total is between ₹5,000 and ₹20,000, apply 10% tax.
3. If the grand total exceeds ₹20,000, apply 15% tax.
Key Steps
1. Calculate the tax based on the applicable tier.
2. Add the tax to the grand total.
3. Display the tax amount and updated grand total.
Coding Challenge 30: Promotional Discounts on Specific Items
Objective: Introduce promotional discounts on specific items identified by their code.
Rules Implemented
1. If the item code matches a promotional code (e.g., PROMO10), apply a 10% discount on that
item.
2. Compute the grand total considering the discounts on applicable items.
Key Steps
1. Check if the item code matches the promotional code.
2. Apply the discount to the item total.
3. Update the grand total and display the final value.
Coding Challenge 31: Payment Mode Rules
Objective: Incorporate business rules based on the selected payment method.
Rules Implemented
1. If the customer chooses Cash, no surcharge applies.
2. If the customer chooses Credit Card, apply a flat 2% surcharge on the final grand total after
all adjustments.
Key Steps
1. Prompt the user to select the payment method.
2. Apply the surcharge if the method is Credit Card.
3. Display the payment method, surcharge amount, and final payable amount.
Coding Challenge 32: Minimum Purchase Requirements
Objective
Add a condition to enforce a minimum purchase value to generate an invoice.
Rules Implemented
1. If the final grand total (after discounts and taxes) is below ₹500, inform the user that the
minimum purchase amount is not met.
Key Steps
1. Check the final grand total.
2. If below ₹500, display an appropriate message and terminate the process.
3. Otherwise, proceed to generate the invoice.


Coding Challenge 33: Loyalty Points
Objective: Introduce a loyalty program where customers earn points based on the final grand total.
Rules Implemented
1. For every ₹100 spent, the customer earns 1 loyalty point.
2. Display the total loyalty points earned.
Key Steps
1. Calculate loyalty points (points = grand_total // 100).
2. Display the earned points along with the invoice.