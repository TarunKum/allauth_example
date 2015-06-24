from django.template.response import TemplateResponse

# Create your views here.
def profile(request):
    return TemplateResponse(request, 'account/profile.html')
