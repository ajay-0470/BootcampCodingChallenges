Setting the Scene: A Day at HealWell Care Hospital
At HealWell Care Hospital, the day begins with the admin team preparing the system for patient
care. The admin updates the list of services available for the day, ensuring accuracy and clarity. These
services include a mix of diagnostics and consultations:
• General Consultation
• Blood Test
• Covid Test
• X-Ray
• CT Scan
• MRI
Once the services are set, the hospital welcomes patients who require seamless and efficient billing
processes. The objective is to build a robust system where patient information, service selection,
billing, and tax calculations are handled smoothly while keeping the user experience intuitive and
error-free.
Consider these 2 arrays (Declare them initially)
Services: ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
Costs: [500, 300, 800, 1500, 4000, 7000]
Requirements & Levels
Level 1: Patient Walks In and Shares Their Details
Patients like Mr. Arjun Kumar visit the hospital. At the reception, their basic details (name, age,
contact, and gender) are collected and stored in variables.
Example Input:
Name: Arjun Kumar
Age: 35
Gender: Male
Contact: 9876543210

Level 2: Displaying Services for Patient Selection
The system displays the list of services available for the day. The patient selects one or more services
they wish to avail. The selected services are stored in an array (selected_services).
Example Interaction:
Available Services:
1. General Consultation
2. Blood Test
3. Covid Test
4. X-Ray
5. CT Scan
6. MRI
Patient Selected: [1, 4] // General Consultation, X-Ray
Selected Services Array: ["General Consultation", "X-Ray"]

Level 3: Fetching Costs of Selected Services
The system iterates through the selected_services array, matches the services with the main services
array, and retrieves the respective costs from the costs array.
Example Output:
Selected Services: ["General Consultation", "X-Ray"]
Selected Costs: [500, 1500]
Level 4: Calculating the Total Cost
The total cost is calculated by summing up the costs of all selected services.
Example Output:
Total Cost (Before Tax): ₹2000
Level 5: Applying GST to the Bill
An 18% GST is applied to the total cost. The system calculates and adds this to the total bill amount.
Example Output:
GST (18%): ₹360
Grand Total: ₹2360
Level 6: Generating and Displaying the Invoice
The system generates a detailed invoice for the patient, including their details, services availed,
individual costs, and the grand total.
Example Output:
-----------------------------------------------
HealWell Care Hospital
Patient Invoice
-----------------------------------------------
Patient Information:
Name: Arjun Kumar
Age: 35
Gender: Male
Contact: 9876543210
Services Availed:
1. General Consultation: ₹500
2. X-Ray: ₹1500
Subtotal: ₹2000
GST (18%): ₹360
Grand Total: ₹2360
Thank you for choosing HealWell Care Hospital!
-----------------------------------------------


Level 7: Setting Up the Services of the Day (Admin Task)
The admin prepares the hospital system by entering the available services into the system. Hospital
wants the flexibility to configure the services. This list is stored in an array. Each service has a name,
and its corresponding cost is stored in a separate array for flexibility.
• Array 1: Stores the names of services (services array).
• Array 2: Stores the costs of the services (costs array).
Example Input:
Services: ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
Costs: [500, 300, 800, 1500, 4000, 7000]
Objective: Ensure services and costs are paired for seamless retrieval.
Level 8: Providing Discounts (Optional Enhancements)
Context
HealWell Care Hospital values its patients and strives to provide the best care at affordable rates. To
improve accessibility and express gratitude, the hospital offers discounts in specific scenarios.
Discount Rules
1. Senior Citizen Discount:
Patients aged 60 or above are eligible for a 10% discount on the subtotal (before GST).
2. High-Bill Discount:
If the subtotal exceeds ₹5000, an additional 5% discount is applied on the subtotal (after any
other discounts).
Steps
1. Check the patient's age to determine if the senior citizen discount applies.
2. Check the subtotal to determine if the high-bill discount applies.
3. Calculate the final total after applying discounts and GST.