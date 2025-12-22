from hospital import Hospital, Ward, Patient, Surgeon, Operation, HospitalManager

h1 = Hospital(1, "City General")

h2 = Hospital(2, "Green Valley")

w1 = Ward(1, "Ward A", h1)

w2 = Ward(2, "Ward B", h1)

w3 = Ward(3, "Ward C", h2)

p1 = Patient(1, "Arjun Kumar", w1)

p2 = Patient(2, "Sana Mehta", w2)

p3 = Patient(3, "Ravi Iyer", w3)

p4 = Patient(4, "Leela Das", w1)

s1 = Surgeon(1, "Dr. Rao", "Senior")

s2 = Surgeon(2, "Dr. Menon", "Non-senior")

op1 = Operation(1, s1, p1)

op2 = Operation(2, s1, p2)



op3 = Operation(3, s2, p3)

op4 = Operation(4, s1, p4)
op5 = Operation(5, s2, p2)  


manager = HospitalManager()
for op in (op1, op2, op3, op4, op5):
    manager.add_operation(op)

print("Total number of patients being operated:", manager.total_operated_patients())

print("\nPatients operated by Dr. Rao:")
for pt in manager.get_patients_by_surgeon("Dr. Rao"):
    print("-", pt.patient_name, f"(ID:{pt.patient_id})")

print("\nPatients admitted to 'Ward A':")
for pt in manager.get_patients_by_ward("Ward A"):
    print("-", pt.patient_name, f"(ID:{pt.patient_id})")
