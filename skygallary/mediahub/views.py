import re
from django.shortcuts import render, redirect

from django.shortcuts import render

from .models import PhotoAsset

# Create your views here.

def gallary(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        caption = request.POST.get('caption')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        PhotoAsset.objects.create(title=title, caption=caption, category=category, image=image)
        return redirect('gallary')
    photos=PhotoAsset.objects.all().order_by('-created_at')
    return render(request, 'gallary.html', {'photos': photos})