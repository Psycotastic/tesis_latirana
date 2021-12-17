"""latirana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from latirana.fotos.views import SearchResultJsonListView
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from fotos import views

urlpatterns = [
    path('', include('fotos.urls')),
    path('admin/', admin.site.urls),
    path('', views.MainView.as_view(), name='index'),
    path('posts/<int:num_posts>/', views.PostJsonListView.as_view(), name='post-json-view'),
    path('search/<str:input>/posts/<int:num_posts>/', views.SearchResultJsonListView.as_view(), name='search-json-view'),
    path('entries/', views.GetGuildEntriesView.as_view(), name='get-entries-view'),
    path('entry/<int:entry_id>',views.cofradia_detalle, name='detalle'),
    path('info/', views.information, name='information'),
    path('guilds/', views.cofradias, name='cofradias'),
    path('corrections/', views.correcciones, name='correcciones'),
    path('tags/', views.tags, name='tags'),
    path('tirana/', views.fiesta_Tirana, name='Tirana'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
