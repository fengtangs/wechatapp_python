import  re

from rest_framework.exceptions import ValidationError


def phone_validator(value):
    if not re.match(r"^((13[0-9])|(17[0-1,6-8])|(15[^4,\\D])|(18[0-9]))\d{8}$",value):
        raise ValidationError("手机格式错误")