"""
Design Challenge 5: Hospitals and Surgeons Management
There is a surgeon management system where a surgeon works for many hospitals and conducts
operation on patients admitted in a ward. The surgeon are of various type such as Senior, Non-senior
,etc.
Design the OO model for the above problem statement and implement the code to
• Total number of patient being operated
• List all the patient being operated by a surgeon
• List all the patient admitted to a ward.
"""
from hospital import Hospital, Ward, Patient, Surgeon, Operation, HospitalManager

h1 = Hospital(1, "City General")

w1 = Ward(1, "Ward A", h1)

w2 = Ward(2, "Ward B", h1)


p1 = Patient(1, "Arjun ", w1)

p2 = Patient(2, "Mahesh", w2)



s1 = Surgeon(1, "Dr. Rao", "Senior")

s2 = Surgeon(2, "Dr. Menon", "Non-senior")

op1 = Operation(1, s1, p1)

op2 = Operation(2, s1, p2)


 


manager = HospitalManager()
for op in (op1, op2):
    manager.add_operation(op)

print("Total number of patients being operated:", manager.total_operated_patients())

print("\nPatients operated by Dr. Rao:")
for pt in manager.get_patients_by_surgeon("Dr. Rao"):
    print("-", pt.patient_name, f"(ID:{pt.patient_id})")

print("\nPatients admitted to 'Ward A':")
for pt in manager.get_patients_by_ward("Ward A"):
    print("-", pt.patient_name, f"(ID:{pt.patient_id})")
