from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import pgettext, ugettext_lazy as _, ugettext
from allauth.account.forms import SignupForm


class MKSignupForm(SignupForm):
    user_model = get_user_model()

    first_name = forms.CharField(label=_("First Name"),
                                 max_length=user_model._meta.get_field('first_name').max_length,
                                 )
    last_name = forms.CharField(label=_("Last Name"),
                                max_length=user_model._meta.get_field('last_name').max_length,
                                )

    def __init__(self, *args, **kwargs):
        super(MKSignupForm, self).__init__(*args, **kwargs)
