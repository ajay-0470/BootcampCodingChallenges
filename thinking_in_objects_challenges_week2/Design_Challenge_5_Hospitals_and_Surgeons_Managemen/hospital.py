class Hospital:
    def __init__(self, hospital_id, hospital_name):
        self.hospital_id = hospital_id

        self.hospital_name = hospital_name


class Ward:
    def __init__(self, ward_id, ward_name, hospital):
        self.ward_id = ward_id

        self.ward_name = ward_name
        
        self.hospital = hospital


class Patient:
    def __init__(self, patient_id, patient_name, ward):
        self.patient_id = patient_id


        self.patient_name = patient_name
        self.ward = ward


class Surgeon:
    def __init__(self, surgeon_id, surgeon_name, surgeon_type):
        self.surgeon_id = surgeon_id

        self.surgeon_name = surgeon_name

        self.surgeon_type = surgeon_type


class Operation:
    def __init__(self, operation_id, surgeon, patient):
        self.operation_id = operation_id

        self.surgeon = surgeon
        
        self.patient = patient


class HospitalManager:
    def __init__(self):
        self.operations = []

    def add_operation(self, operation):
        self.operations.append(operation)

    def total_operated_patients(self):
        patient_ids = {op.patient.patient_id for op in self.operations}
        return len(patient_ids)

    def get_patients_by_surgeon(self, surgeon_name):
        return [op.patient for op in self.operations if op.surgeon.surgeon_name == surgeon_name]

    def get_patients_by_ward(self, ward_name):
        return [op.patient for op in self.operations if op.patient.ward.ward_name == ward_name]
