from rest_framework.permissions import BasePermission
from datetime import timedelta
from django.utils import timezone
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from rest_framework import status

class IsCandidateUser(BasePermission):

    message = 'candy 만 사용 할 수 있습니다.'
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.user_type.user_type=="candidate")

class login_permission(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user.user_type =="candi")

class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)
