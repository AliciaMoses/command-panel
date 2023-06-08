from django.shortcuts import render

from .models import Script

def script_list(request):
    scripts = Script.objects.all()
    return render(request, 'commandpanel/scripts.html', {'scripts': scripts})
