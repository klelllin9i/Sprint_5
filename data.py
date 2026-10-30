import random
import string

BASE_URL = "https://qa-stellarburgers.education-services.ru/"
LOGIN_URL = BASE_URL + "login"
REGISTER_URL = BASE_URL + "register"
FORGOT_PASSWORD_URL = BASE_URL + "forgot-password"
PROFILE_URL = BASE_URL + "account/profile"
API_REGISTER_URL = BASE_URL + "api/auth/register"

USER_NAME = "Anatolii"
EMAIL_PREFIX = "Anatolii_Larin_57"  # имя_фамилия_номер когорты
EMAIL_DOMAIN = "yandex.ru"


def generate_email():
    """Генерирует уникальный email: имя_фамилия_когорта_3 цифры@домен."""
    digits = "".join(random.choices(string.digits, k=3))
    return f"{EMAIL_PREFIX}_{digits}@{EMAIL_DOMAIN}"


def generate_password(length=6):
    """Генерирует пароль заданной длины (по умолчанию 6 — минимально допустимая)."""
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))
