
import  re

from django_redis import get_redis_connection
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .validator import phone_validator



class MessageSerializer(serializers.Serializer):
    phone= serializers.CharField(label="phone",validators=[phone_validator,])


class LoginSerializer(serializers.Serializer):
    phone= serializers.CharField(label="phone",validators=[phone_validator,])
    code = serializers.CharField(label="code",)

    def validate_code(self,value):
        if len(value)!=4:
            raise ValidationError("格式错误")
        if not value.isdecimal():
            raise  ValidationError("格式错误")

        phone = self.initial_data.get("phone")
        conn =get_redis_connection()
        code = conn.get(phone)

        if not code:
            raise ValidationError('验证码过期')
        if value != code.decode('utf-8'):
            raise ValidationError('验证码错误')
        return value