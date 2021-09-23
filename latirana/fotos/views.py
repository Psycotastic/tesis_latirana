from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ImageForm
from .forms import SearchForm
from .models import Post
from django.views.generic import View, TemplateView
from django.http.response import JsonResponse
import datetime
import os


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
    #print(request.session['latest_img_uploade'])
    img_url = ''
    if 'latest_img_uploaded' in request.session:
        img_url = request.session['latest_img_uploaded']
        request.session['latest_img_uploaded'] = ''

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        print(type(request.FILES))
        if form.is_valid():
            registry = form.save(commit=False)
            extension = str(registry.image).split('.')[-1]
            now = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            guild_name = registry.guild
            costume_name = registry.costume
            photo_year = registry.year
            performance_name = registry.performance
            new_img_name = guild_name + "-" + performance_name + "-" + costume_name + "-" + photo_year + "_" + now + "." + extension
            new_img_name = new_img_name.replace(" ","_")
            registry.save()
            new_path = registry.image.path.split("\\")
            new_filename = ""
            for e in new_path[:-1]:
                new_filename = new_filename + e + "\\"
            new_filename = new_filename + new_img_name
            os.rename(registry.image.path, new_filename)
            # Get the current instance object to display in the template
            img_url = "\\media\\images\\" + new_filename.split("\\")[-1]
            request.session['latest_img_uploaded'] = img_url
            return redirect( '/upload')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form, 'img_url' : img_url})

def search(request):
    search_list = []
    if request.method == 'POST' :
        form = SearchForm(request.POST)
        if form.is_valid():
            entrada = form['buscar'].value()
            param = '%' + entrada + '%'
            search_list = Post.objects.raw("""select * from fotos_post where performance like %s UNION select * from fotos_post where guild like %s UNION select * from fotos_post where year like %s UNION select * from fotos_post where costume like %s""", [param, param, param, param])

    return render(request, 'search_results.html', {'search_list': search_list})