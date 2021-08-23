from django import forms
from .models import Post

class ImageForm(forms.ModelForm):
    """Form for the image model"""

    def init(self, args, **kwargs):
        super().init(args, **kwargs)
        self.fields['performance', 'year', 'costume'].required = True

    class Meta:
        model = Post
        fields = ('performance', 'year', 'costume', 'guild', 'image')
        widgets = {
            'performance': forms.TextInput(attrs={'placeholder': 'Baile'}),
            'year': forms.TextInput(attrs={'placeholder': 'Año en que se sacó la fotografía'}),
            'costume': forms.TextInput(attrs={'placeholder': 'Tipo de vestimenta según ritmo'}),
        }