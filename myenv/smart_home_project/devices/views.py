from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Light

@login_required
def home(request):
    lights = Light.objects.filter(user=request.user)
    return render(request, 'devices/home.html', {'lights': lights})

@login_required
def toggle_light(request, light_id):
    light = Light.objects.get(id=light_id)
    if light.user == request.user:  # Check if the user owns the light
        light.is_on = not light.is_on
        light.save()
    else:
        messages.error(request, "You don't have permission to control this light.")
    return redirect('home')
