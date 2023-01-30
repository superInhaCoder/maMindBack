from rest_framework.exceptions import APIException

class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'
    
class DataTypeIncorrect(APIException):
    status_code = 503
    default_detail = '데이터 형식이 틀렸습니다.'
    default_code = 'data_incorrected'
    
class GoogleAuthError(APIException):
    status_code = 400
    default_detail = 'Google auth error'
    default_code = 'google_auth_error'