from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageForm
from .forms import SearchForm
from .models import Post


def index(request):
    post_list = Post.objects.all()
    print(type(post_list))
    sorted_list = post_list.order_by('-id')
    return render(request, 'home.html', {'post_list': sorted_list})

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

def search(request):
    search_list = []
    if request.method == 'POST' :
        form = SearchForm(request.POST)
        if form.is_valid():
            entrada = form['buscar'].value()
            param = '%' + entrada + '%'
            search_list = Post.objects.raw("""select * from fotos_post where performance like %s UNION select * from fotos_post where guild like %s UNION select * from fotos_post where year like %s UNION select * from fotos_post where costume like %s""", [param, param, param, param])

    return render(request, 'search_results.html', {'search_list': search_list})