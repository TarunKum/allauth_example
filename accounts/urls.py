from django.conf.urls import url

urlpatterns = [
    url(r'^profile/$', 'accounts.views.profile', name='account_profile'),
]
