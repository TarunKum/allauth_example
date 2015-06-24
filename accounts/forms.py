from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import pgettext, ugettext_lazy as _, ugettext


class MySignupForm(forms.Form):
    user_model = get_user_model()

    first_name = forms.CharField(label=_("First name"),
                                 max_length=user_model._meta.get_field('first_name').max_length,
                                 widget=forms.TextInput(attrs={'placeholder':
                                                         _('First name'),
                                                        'autofocus': 'autofocus'})
                                 )
    last_name = forms.CharField(label=_("Last Name"),
                                max_length=user_model._meta.get_field('last_name').max_length,
                                widget=forms.TextInput(attrs={'placeholder':
                                                              _('Last name')})
                                )

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
