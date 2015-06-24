## Example site

I am trying to override the django-allauth default signup forms so we
can ask for first and last time at time of registration.

I can override the template by simply putting a signup.html file into
the 'accounts/templates/account' directory.

The available configuration settings indicate that it is fairly common
to override the default forms. You can list ACCOUNT_FORMS and
SOCIALACCOUNT_FORMS by form name. There is also an explicit option for
overriding the signup form: ACCOUNT_SIGNUP_FORM_CLASS. But when I set
that to the name of my signup form, I get the following error:

```
ImproperlyConfigured at /
Error importing form class accounts.forms: "cannot import name 'SignupForm'"


Request Method: GET
Request URL: http://127.0.0.1:8000/

Django Version: 1.8.2
Python Version: 3.4.3
Installed Applications:
('django.contrib.admin',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.sites',
 'django.contrib.messages',
 'django.contrib.staticfiles',
 'accounts',
 'allauth',
 'allauth.account',
 'allauth.socialaccount',
 'allauth.socialaccount.providers.github',
 'allauth.socialaccount.providers.google',
 'django_extensions')
Installed Middleware:
('django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
 'django.middleware.clickjacking.XFrameOptionsMiddleware',
 'django.middleware.security.SecurityMiddleware')


Traceback:
File "/Users/cnk/.pyenv/versions/mk-web-core-3.4.3/lib/python3.4/site-packages/django/core/handlers/base.py" in get_response
119.                 resolver_match = resolver.resolve(request.path_info)
File "/Users/cnk/.pyenv/versions/mk-web-core-3.4.3/lib/python3.4/site-packages/django/core/urlresolvers.py" in resolve
366.             for pattern in self.url_patterns:
File "/Users/cnk/.pyenv/versions/mk-web-core-3.4.3/lib/python3.4/site-packages/django/core/urlresolvers.py" in url_patterns
402.         patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
File "/Users/cnk/.pyenv/versions/mk-web-core-3.4.3/lib/python3.4/site-packages/django/core/urlresolvers.py" in urlconf_module
396.             self._urlconf_module = import_module(self.urlconf_name)
File "/Users/cnk/.pyenv/versions/3.4.3/lib/python3.4/importlib/__init__.py" in import_module
109.     return _bootstrap._gcd_import(name[level:], package, level)
File "/Users/cnk/Code/sandbox/allauth_example/allauth_example/urls.py" in <module>
24.     url(r'^accounts/', include('allauth.urls')),
File "/Users/cnk/.pyenv/versions/mk-web-core-3.4.3/lib/python3.4/site-packages/django/conf/urls/__init__.py" in include
33.         urlconf_module = import_module(urlconf_module)
File "/Users/cnk/.pyenv/versions/3.4.3/lib/python3.4/importlib/__init__.py" in import_module
109.     return _bootstrap._gcd_import(name[level:], package, level)
File "/Users/cnk/.pyenv/versions/mk-web-core-3.4.3/lib/python3.4/site-packages/allauth/urls.py" in <module>
12. urlpatterns = patterns('', url('^', include('allauth.account.urls')))
File "/Users/cnk/.pyenv/versions/mk-web-core-3.4.3/lib/python3.4/site-packages/django/conf/urls/__init__.py" in include
33.         urlconf_module = import_module(urlconf_module)
File "/Users/cnk/.pyenv/versions/3.4.3/lib/python3.4/importlib/__init__.py" in import_module
109.     return _bootstrap._gcd_import(name[level:], package, level)
File "/Users/cnk/.pyenv/versions/mk-web-core-3.4.3/lib/python3.4/site-packages/allauth/account/urls.py" in <module>
4. from . import views
File "/Users/cnk/.pyenv/versions/mk-web-core-3.4.3/lib/python3.4/site-packages/allauth/account/views.py" in <module>
19. from .forms import AddEmailForm, ChangePasswordForm
File "/Users/cnk/.pyenv/versions/mk-web-core-3.4.3/lib/python3.4/site-packages/allauth/account/forms.py" in <module>
206. class BaseSignupForm(_base_signup_form_class()):
File "/Users/cnk/.pyenv/versions/mk-web-core-3.4.3/lib/python3.4/site-packages/allauth/account/forms.py" in _base_signup_form_class
188.                                               ' "%s"' % (fc_module, e))

Exception Type: ImproperlyConfigured at /
Exception Value: Error importing form class accounts.forms: "cannot import name 'SignupForm'"
```