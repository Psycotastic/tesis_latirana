from django.db import models

# Create your models here.

GUILDS = (
    ('sociedad religiosa chilenitos de santa teresita','​​SOCIEDAD RELIGIOSA CHILENITOS DE SANTA TERESITA'),
    ('sociedad católica indios tobas del norte virgen de la tirana', 'SOCIEDAD CATÓLICA INDIOS TOBAS DEL NORTE VIRGEN DE LA TIRANA'),
    ('sociedad religiosa gitanos del carmen trinidad ponce','SOCIEDAD RELIGIOSA GITANOS DEL CARMEN TRINIDAD PONCE'),
    ('baile religioso auténtica diablada','BAILE RELIGIOSO AUTÉNTICA DIABLADA'),
    ('baile religioso aymara','BAILE RELIGIOSO AYMARA'),
)

class Post(models.Model):
    image = models.ImageField(upload_to='images')
    performance = models.CharField(max_length=255, default="baile")
    year = models.CharField(max_length=4, default="año")
    costume = models.CharField(max_length=255, default="vestimenta")
    guild = models.CharField(max_length=255, default="Sociedad Religiosa Chilenitos de Santa Teresita", choices=GUILDS)

    def __str__(self):
        return self.year