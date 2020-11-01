from prescriptions.application.repository.prescription_repository import (
    PrescriptionRepository,
)
from prescriptions.infrastructure.postgre import SessionLocal
from prescriptions.models.prescription_model import PrescriptionModel
from prescriptions.schemas.create_prescription_schema import CreatePrescriptionSchema
from prescriptions.schemas.prescription_schema import (
    ClinicSchema,
    PatientSchema,
    PhysicianSchema,
    PrescriptionSchema,
)


class PostgrePrescriptionRepository(PrescriptionRepository):

    db = SessionLocal()

    async def create(self, dto: CreatePrescriptionSchema) -> PrescriptionSchema:
        db_record = PrescriptionModel(
            clinic_id=dto.clinic.id,
            physician_id=dto.physician.id,
            patient_id=dto.patient.id,
            text=dto.text,
        )

        self.db.add(db_record)
        self.db.commit()

        prescription = PrescriptionSchema(
            id=db_record.id,
            clinic=ClinicSchema(id=db_record.clinic_id),
            physician=PhysicianSchema(id=db_record.physician_id),
            patient=PatientSchema(id=db_record.patient_id),
            text=db_record.text,
        )

        self.db.close()
        return prescription
