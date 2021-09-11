from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageForm
from .forms import SearchForm
from .models import Post
from django.views.generic import View, TemplateView
from django.http.response import JsonResponse

class MainView(TemplateView):
    template_name= 'home.html'

class PostJsonListView(View):
    def get(self, *args, **kwargs):
        print(kwargs)
        upper = kwargs.get('num_posts')
        lower = upper - 10
        posts = list(Post.objects.values().order_by('-id')[lower:upper])
        posts_size = len(Post.objects.all())
        max_size = True if upper >= posts_size else False
        return JsonResponse({'data':posts, 'max': max_size}, safe=False)

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