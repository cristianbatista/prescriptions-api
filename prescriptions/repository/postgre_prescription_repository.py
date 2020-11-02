from prescriptions.models.prescription_model import PrescriptionModel
from prescriptions.schemas.create_prescription_schema import CreatePrescriptionSchema


class PostgrePrescriptionRepository:
    async def create(self, dto: CreatePrescriptionSchema, db) -> PrescriptionModel:
        db_record = PrescriptionModel(
            clinic_id=dto.clinic.id,
            physician_id=dto.physician.id,
            patient_id=dto.patient.id,
            text=dto.text,
        )
        db.add(db_record)

        return db_record
