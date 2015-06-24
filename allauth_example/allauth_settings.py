# Configuration for django-allauth plugin
# http://django-allauth.readthedocs.org/en/latest/configuration.html

ACCOUNT_AUTHENTICATION_METHOD = "username"  # Look up acct by username

ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED
SOCIALACCOUNT_EMAIL_REQUIRED = ACCOUNT_EMAIL_REQUIRED
ACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_EMAIL_VERIFICATION = ACCOUNT_EMAIL_VERIFICATION
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"  # change this for launch

ACCOUNT_SIGNUP_FORM_CLASS = "accounts.forms.MKSignupForm"
# SOCIALACCOUNT_FORMS (={})
# Used to override forms, for example: {‘signup’: ‘myapp.forms.SignupForm’}


ACCOUNT_USERNAME_MIN_LENGTH = 3
ACCOUNT_PASSWORD_MIN_LENGTH = 6

ACCOUNT_SESSION_REMEMBER = None  # ask user if they want to be remembered
ACCOUNT_SESSION_COOKIE_AGE = 1814400  # 3 weeks in seconds

SOCIALACCOUNT_PROVIDERS = {'google': {'SCOPE': ['profile', 'email'],
                                      'AUTH_PARAMS': {'access_type': 'online'}
                                      }
                           }

SITE_ID = 1
