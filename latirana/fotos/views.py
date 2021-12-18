from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ImageForm, GuildForm, SearchForm
from .models import Post, Cofradia
from django.views.generic import View, TemplateView
from django.http.response import JsonResponse
from django.db import connection, transaction
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
            elements = Post.objects.all().last()
            id = getattr(elements, 'id')
            cursor = connection.cursor()
            cursor.execute("UPDATE fotos_post set image = '" + "images/" + new_img_name +  "' where id = " + str(id))
            transaction.commit()
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
            #TODO: La busqueda falla si se añade el campo 'characrter' por algún motivo
            search_list = Post.objects.raw("""select * from fotos_post where performance like %s UNION select * from fotos_post where guild like %s UNION select * from fotos_post where year like %s UNION select * from fotos_post where costume like %s UNION select * from fotos_post where author like %s ORDER BY id DESC""", [param, param, param, param, param])[0:10]
            results_size = len(Post.objects.raw("""select * from fotos_post where performance like %s UNION select * from fotos_post where guild like %s UNION select * from fotos_post where year like %s UNION select * from fotos_post where costume like %s UNION select * from fotos_post where author like %s""", [param, param, param, param, param]))
    return render(request, 'search_results.html', {'search_list': search_list, 'input' : entrada, 'result_size': results_size})

class SearchResultJsonListView(View):
    def get(self, *args, **kwargs):
        upper = kwargs.get('num_posts')
        entrada = kwargs.get('input')
        lower = upper - 10
        param = '%' + entrada + '%'
        results = Post.objects.raw("""select * from fotos_post where performance like %s UNION select * from fotos_post where guild like %s UNION select * from fotos_post where year like %s UNION select * from fotos_post where costume like %s ORDER BY id DESC""", [param, param, param, param])[lower:upper]
        results_size = len(Post.objects.raw("""select * from fotos_post where performance like %s UNION select * from fotos_post where guild like %s UNION select * from fotos_post where year like %s UNION select * from fotos_post where costume like %s""", [param, param, param, param]))
        max_size = True if upper >= results_size else False
        aux_list = "["
        for e in results:
            aux_list = aux_list + "{"
            aux_list = aux_list + '"image":"'  + str(e.image) + '"'
            aux_list = aux_list + ',"performance":"' + e.performance + '"'
            aux_list = aux_list + ',"year":"' + e.year + '"'
            aux_list = aux_list + ',"costume":"' + e.costume + '"'
            aux_list = aux_list + ',"guild":"' + e.guild + '"'
            aux_list = aux_list + ',"author":"' + e.author + '"'
            aux_list = aux_list + ',"character":"' + e.character + '"'
            aux_list = aux_list + ',"id":"' + str(e.id) + '"}'
            if e != results[-1]:
                aux_list = aux_list + ","
        aux_list = aux_list + "]"
        return JsonResponse({'data': aux_list, 'max':max_size},safe=False)

def information(request):
    return render(request, 'informacion.html')

def cofradias(request):
    uploaded_entry = ''
    if 'latest_entry_uploaded' in request.session:
        uploaded_entry = request.session['latest_entry_uploaded']
        request.session['latest_entry_uploaded'] = ''
    if request.method == 'POST':
        form = GuildForm(request.POST)
        if form.is_valid():
            registry = form.save(commit=False)
            registry.save()
            transaction.commit()
            # Get the current instance object to display in the template
            uploaded_entry = "Yes"
            request.session['latest_entry_uploaded'] = uploaded_entry
            return redirect( '/guilds')
    else:
        form = GuildForm()
    return render(request, 'cofradias.html', {'form': form, 'entry' : uploaded_entry})

class GetGuildEntriesView(View):
    def get(self, *args, **kwargs):
        results = Cofradia.objects.raw("""select * from fotos_cofradia ORDER BY id DESC""")
        aux_list = "["
        for e in results:
            aux_list = aux_list + "{"
            aux_list = aux_list + '"society":"' + e.society + '"'
            aux_list = aux_list + ',"id":"' + str(e.id) + '"}'
            if e != results[-1]:
                aux_list = aux_list + ","
        aux_list = aux_list + "]"
        return JsonResponse({'data': aux_list},safe=False)

def cofradia_detalle(request, entry_id):
    entry = Cofradia.objects.get(pk=entry_id)
    print(entry)
    return render(request, 'entry_detail.html', {'entry': entry})

def fiesta_Tirana(request):
    return render(request, 'fiesta_tirana.html')

def correcciones(request):
    return render(request, 'correcciones.html')

def tags(request):
    return render(request, 'tags.html')
