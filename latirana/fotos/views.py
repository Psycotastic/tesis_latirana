from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageForm
from .models import Post


def index(request):
    post_list = Post.objects.all()
    for p in post_list: print (p)
    return render(request, 'home.html', {'post_list': post_list})

def upload(request):
    # return render(request, 'upload.html')
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})