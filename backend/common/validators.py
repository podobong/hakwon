from django.core.validators import RegexValidator


phone_validator = RegexValidator(
        regex=r'[0-9]{9,11}',
        message='It is not a phone number format.'
        )

zip_validator = RegexValidator(
        regex=r'[0-9]{5}',
        message='It is not a zip code format.'
        )

