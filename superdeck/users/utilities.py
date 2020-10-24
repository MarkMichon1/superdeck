from django.contrib.auth.password_validation import CommonPasswordValidator, MinimumLengthValidator, \
    NumericPasswordValidator, UserAttributeSimilarityValidator
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

from users.models import AppUser


def validate_name_return_errors(first_name: str, last_name: str) -> list:

    try:
        ascii_username_validator = ASCIIUsernameValidator()
        ascii_username_validator(first_name)
        ascii_username_validator(last_name)
        return []
    except ValidationError:
        return ["Name may contain only English letters, numbers, and these characters: @ . + - _"]


def validate_email_return_errors(email: str) -> list:
    email_validator = EmailValidator()
    try:
        email_validator(value=email)
    except ValidationError:
        return ["Invalid email address"]
    try:
        AppUser.objects.get(email__iexact=email)
        return ["Email address is already in use"]
    except AppUser.DoesNotExist:
        return []


def validate_password_return_errors(password: str, active_user=None) -> list:
    """This iterates through active validators and returns error messages for each of them.  Used for user creation
    and password changes.
    """

    error_list = []

    try:
        min_length_validator = MinimumLengthValidator()
        min_length_validator.validate(password=password)
    except ValidationError:
        error_list.append("Minimum length is 8 characters")

    try:
        common_password_validator = CommonPasswordValidator()
        common_password_validator.validate(password=password)
    except ValidationError:
        error_list.append("This password is too common")

    try:
        numeric_password_validator = NumericPasswordValidator()
        numeric_password_validator.validate(password=password)
    except ValidationError:
        error_list.append("Cannot have an entirely numeric password")

    try:
        user_attribute_similarity_validator = UserAttributeSimilarityValidator()
        user_attribute_similarity_validator.validate(password=password, user=active_user)
    except ValidationError:
        error_list.append("This password is too similar to your username or email address")

    return error_list


def final_validation(first_name: str, last_name: str, email: str) -> dict:
    """This runs a final validation check when a valid form is submitted for registration, to return form feedback for
    any last moment errors, specifically if the email address gets used by someone else between initial field validation
    and site registration.
    """

    final_validation_status = {}
    username_errors = validate_name_return_errors(first_name=first_name, last_name=last_name)
    if username_errors:
        final_validation_status['username'] = username_errors

    email_errors = validate_email_return_errors(email=email)
    if email_errors:
        final_validation_status['email'] = email_errors

    return final_validation_status