from django import forms
from django.forms import widgets
from django.forms.formsets import MAX_NUM_FORM_COUNT
from .models import Post, Cofradia

class ImageForm(forms.ModelForm):
    """Form for the image model"""

    def init(self, args, **kwargs):
        super().init(args, **kwargs)
        self.fields['performance', 'year', 'costume'].required = True

    class Meta:
        model = Post
        fields = ('performance', 'year', 'costume', 'guild', 'image', 'author', 'character')
        widgets = {
            'performance': forms.TextInput(attrs={'placeholder': 'Baile'}),
            'year': forms.TextInput(attrs={'placeholder': 'Año en que se sacó la fotografía'}),
            'costume': forms.TextInput(attrs={'placeholder': 'Tipo de vestimenta según etapa de la fiesta'}),
            'author': forms.TextInput(attrs={'placeholder': 'Autor de la Fotografía'}),
            'character': forms.TextInput(attrs={'placeholder': 'Personajes que se visualizan en la fotografía'})
        }
    
class SearchForm(forms.Form):
    def init(self, args, **kwargs):
        super().init(args, **kwargs)
        self.fields['buscar'].required = True
    
    buscar = forms.CharField(max_length=500)

class GuildForm(forms.ModelForm):

    class Meta:
        model = Cofradia
        fields = ('society', 'fundation', 'dance', 'history')
        widgets = {
            'society': forms.TextInput(attrs={'placeholder': 'Sociedad religiosa'}),
            'fundation': forms.TextInput(attrs={'placeholder': 'Año de Fundación'}),
            'dance' : forms.TextInput(attrs={'placeholder' : 'Tipo de Baile'}),
            'history' : forms.Textarea(attrs={'placeholder' : 'Breve Historia de la Sociedad Religiosa'})
        }
        