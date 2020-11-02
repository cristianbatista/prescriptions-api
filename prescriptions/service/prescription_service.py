from fastapi import logger
from prescriptions.http.clinics_http import ClinicsHttp
from prescriptions.http.patients_http import PatientsHttp
from prescriptions.http.physicians_http import PhysiciansHttp
from prescriptions.infrastructure.postgre import create_session_local
from prescriptions.repository.postgre_prescription_repository import (
    PostgrePrescriptionRepository,
)
from prescriptions.schemas.clinic_schema import ClinicSchema
from prescriptions.schemas.create_prescription_schema import CreatePrescriptionSchema
from prescriptions.schemas.patient_schema import PatientSchema
from prescriptions.schemas.physician_schema import PhysicianSchema
from prescriptions.schemas.prescription_schema import PrescriptionSchema


class PrescriptionService:
    def __init__(
            self,
            db=None,
            prescription_repository=None,
            patients_http=None,
            physicians_http=None,
            clinics_http=None
    ):
        self.db = create_session_local() if not db else db
        self.prescripton_repository = (
            PostgrePrescriptionRepository()
            if not prescription_repository
            else prescription_repository
        )
        self.patitents_http = PatientsHttp() if not patients_http else patients_http
        self.physicians_http = PhysiciansHttp() if not physicians_http else physicians_http
        self.clinics_http = ClinicsHttp() if not clinics_http else clinics_http


    async def create_prescription(
        self, dto: CreatePrescriptionSchema
    ) -> PrescriptionSchema:
        try:

            await self.patitents_http.get(dto.patient.id)
            await self.physicians_http.get(dto.physician.id)
            clinic = await self.clinics_http.get(dto.clinic.id)

            if not clinic:
                dto.clinic.id = None

            record = await self.prescripton_repository.create(dto, self.db)
            self.db.commit()

            prescription = PrescriptionSchema(
                id=record.id,
                clinic=ClinicSchema(id=record.clinic_id),
                physician=PhysicianSchema(id=record.physician_id),
                patient=PatientSchema(id=record.patient_id),
                text=record.text,
            )
            return prescription
        except Exception as ex:
            self.db.rollback()
            raise ex
        finally:
            self.db.close()
