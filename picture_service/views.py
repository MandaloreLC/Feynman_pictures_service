from django.shortcuts import render

from .models import Image


def display_image(request, image_id):
    image = Image.objects.get(pk=image_id)
    return render(request, 'image.html', {'image': image})
