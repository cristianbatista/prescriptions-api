from prescriptions.exception.base_exception import ExceptionBase


class MalformedRequestError(ExceptionBase):
    def __init__(self):
        super().__init__(code="01", message="malformed request")


class PhysicianNotFound(ExceptionBase):
    def __init__(self):
        super().__init__(code="02", message="physician not found")


class PatientNotFound(ExceptionBase):
    def __init__(self):
        super().__init__(code="03", message="patient not found")


class MetricsServiceNotAvailable(ExceptionBase):
    def __init__(self):
        super().__init__(code="04", message="metrics service not available")


class PhysiciansServiceNotAvailable(ExceptionBase):
    def __init__(self):
        super().__init__(code="05", message="physicians service not available")


class PatientsServiceNotAvailable(ExceptionBase):
    def __init__(self):
        super().__init__(code="06", message="patients service not available")
