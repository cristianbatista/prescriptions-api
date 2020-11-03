from prescriptions.http.clinics_http import ClinicsHttp
from prescriptions.http.metrics_http import MetricsHttp
from prescriptions.http.patients_http import PatientsHttp
from prescriptions.http.physicians_http import PhysiciansHttp
from prescriptions.infrastructure.postgre import create_session_local
from prescriptions.repository.postgre_prescription_repository import (
    PostgrePrescriptionRepository,
)
from prescriptions.schemas.clinic_schema import ClinicSchema
from prescriptions.schemas.create_metrics_schema import CreateMetricsSchema
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
        clinics_http=None,
        metrics_http=None,
    ):
        self.db = create_session_local() if not db else db
        self.prescripton_repository = (
            PostgrePrescriptionRepository()
            if not prescription_repository
            else prescription_repository
        )
        self.patients_http = PatientsHttp() if not patients_http else patients_http
        self.physicians_http = (
            PhysiciansHttp() if not physicians_http else physicians_http
        )
        self.clinics_http = ClinicsHttp() if not clinics_http else clinics_http
        self.metrics_http = MetricsHttp() if not metrics_http else metrics_http

    async def create_prescription(
        self, dto: CreatePrescriptionSchema
    ) -> PrescriptionSchema:
        try:

            patient = await self.patients_http.get(dto.patient.id)
            physician = await self.physicians_http.get(dto.physician.id)
            clinic = await self.clinics_http.get(dto.clinic.id)

            if not clinic:
                dto.clinic.id = None

            record = await self.prescripton_repository.create(dto, self.db)

            create_metrics_schema = CreateMetricsSchema(
                clinic_id=dto.clinic.id,
                clinic_name=clinic["name"] if clinic else None,
                physician_id=physician["id"],
                physician_name=physician["name"],
                physician_crm=physician["crm"],
                patient_id=patient["id"],
                patient_name=patient["name"],
                patient_email=patient["email"],
                patient_phone=patient["phone"],
            )
            await self.metrics_http.post(create_metrics_schema.dict())

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
