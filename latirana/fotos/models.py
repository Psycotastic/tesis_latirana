from django.db import models

# Create your models here.

GUILDS = (
    ('Baile Moreno Promesante Nuestra Señora del Carmen','Baile Moreno Promesante Nuestra Señora del Carmen'),
    ('Baile Promesero Los Pelícanos Nuestra Señora de Andacollo','Baile Promesero Los Pelícanos Nuestra Señora de Andacollo'),
    ('Baile Religioso Auténtica Diablada','Baile Religioso Auténtica Diablada'),
    ('Baile Religioso Aymara','Baile Religioso Aymara'),
    ('Baile Religioso Chinitos del Carmen','Baile Religioso Chinitos del Carmen'),
    ('Baile Religioso Diablada Hijos de Dios y María','Baile Religioso Diablada Hijos de Dios y María'),
    ('Baile Religioso Diablada Morenada Servidores de la Virgen del Carmen','Baile Religioso Diablada Morenada Servidores de la Virgen del Carmen'),
    ('Baile Religioso Gitanos Hijos de la Pampa','Baile Religioso Gitanos Hijos de la Pampa'),
    ('Baile Religioso Indiada del Carmen','Baile Religioso Indiada del Carmen'),
    ('Baile Religioso Indios Castores','Baile Religioso Indios Castores'),
    ('Baile Religioso Moreno Cóndor','Baile Religioso Moreno Cóndor'),
    ('Baile Religioso Moreno Of. Salitrera Victoria','Baile Religioso Moreno Of. Salitrera Victoria'),
    ('Baile Religioso Morenos de San Pedro de Cavancha','Baile Religioso Morenos de San Pedro de Cavancha'),
    ('Baile Religioso Pieles Rojas Águilas Blancas','Baile Religioso Pieles Rojas Águilas Blancas'),
    ('Baile Religioso Pieles Rojas de Ayquina','Baile Religioso Pieles Rojas de Ayquina'),
    ('Baile Religioso Pieles Rojas Peña Chica','Baile Religioso Pieles Rojas Peña Chica'),
    ('Baile Religioso Sambos Caporales Marianos','Baile Religioso Sambos Caporales Marianos'),
    ('Comunidad Religiosa Labradores de la Esperanza', 'Comunidad Religiosa Labradores de la Esperanza'),
    ('Cuerpo de Baile Indios Católicos','Cuerpo de Baile Indios Católicos'),
    ('Cuerpo de Baile Pieles Rojas','Cuerpo de Baile Pieles Rojas'),
    ('Cuerpo de Baile Religioso Indios Sioux','Cuerpo de Baile Religioso Indios Sioux'),
    ('Cuerpo de Baile Religioso Morenos Santa Inés','Cuerpo de Baile Religioso Morenos Santa Inés'),
    ('Cuerpo de Baile Religioso Pieles Rojas del Espíritu Santo','Cuerpo de Baile Religioso Pieles Rojas del Espíritu Santo'),
    ('Diablada del Salitre', 'Diablada del Salitre'),
    ('Diablada Hermanos del Norte', 'Diablada Hermanos del Norte'),
    ('Sambos Caporales del Sagrado Corazón', 'Sambos Caporales del Sagrado Corazón'),
    ('Sociedad Baile Religioso Morenos Nuestra Señora del Carmen','Sociedad Baile Religioso Morenos Nuestra Señora del Carmen'),
    ('Sociedad Baile Religioso Tinkus Nuestra Señora del Perpetuo Socorro','Sociedad Baile Religioso Tinkus Nuestra Señora del Perpetuo Socorro'),
    ('Sociedad Baile Religioso Zambos Caporales de La Tirana','Sociedad Baile Religioso Zambos Caporales de La Tirana'),
    ('Sociedad Católica Indios Tobas del Norte Virgen de La Tirana','Sociedad Católica Indios Tobas del Norte Virgen de La Tirana'),
    ('Sociedad Católica Pieles Rojas','Sociedad Católica Pieles Rojas'),
    ('Sociedad de Baile Religioso Carmelo Promesante','Sociedad de Baile Religioso Carmelo Promesante'),
    ('Sociedad de Baile Religioso Diablada del Sol','Sociedad de Baile Religioso Diablada del Sol'),
    ('Sociedad de Baile Religioso Indios Cheyenns','Sociedad de Baile Religioso Indios Cheyenns'),
    ('Sociedad de Baile Religioso Morenada Nuestra Señora del Carmen de La Tirana','Sociedad de Baile Religioso Morenada Nuestra Señora del Carmen de La Tirana'),
    ('Sociedad de Baile Religioso Pieles Rojas del Carmen','Sociedad de Baile Religioso Pieles Rojas del Carmen'),
    ('Sociedad Religiosa Águila Blanca','Sociedad Religiosa Águila Blanca'),
    ('Sociedad Religiosa Aldeanos de La Tirana','Sociedad Religiosa Aldeanos de La Tirana'),
    ('Sociedad Religiosa Alí Babá Hijos de Jesús','Sociedad Religiosa Alí Babá Hijos de Jesús'),
    ('Sociedad Religiosa Alí Babá Tocopillano','Sociedad Religiosa Alí Babá Tocopillano'),
    ('Sociedad Religiosa Anta Wara del Carmen','Sociedad Religiosa Anta Wara del Carmen'),
    ('Sociedad Religiosa Árabe Promesante San Rafael Arcángel','Sociedad Religiosa Árabe Promesante San Rafael Arcángel'),
    ('Sociedad Religiosa Baile Chino','Sociedad Religiosa Baile Chino'),
    ('Sociedad Religiosa Baile Chunchos de Nuestra Señora del Carmen', 'Sociedad Religiosa Baile Chunchos de Nuestra Señora del Carmen'),
    ('Sociedad Religiosa Baile Gitano Pedro de Valdivia','Sociedad Religiosa Baile Gitano Pedro de Valdivia'),
    ('Sociedad Religiosa Baile Gitanos Guillermo Díaz','Sociedad Religiosa Baile Gitanos Guillermo Díaz'),
    ('Sociedad Religiosa Baile Moreno Los Chilenitos','Sociedad Religiosa Baile Moreno Los Chilenitos'),
    ('Sociedad Religiosa Baile Moreno Los Promesantes del Carmen','Sociedad Religiosa Baile Moreno Los Promesantes del Carmen'),
    ('Sociedad Religiosa Baile Morenos Los Liras','Sociedad Religiosa Baile Morenos Los Liras'),
    ('Sociedad Religiosa Bolivianada Nuestra Señora de Los Ángeles','Sociedad Religiosa Bolivianada Nuestra Señora de Los Ángeles'),
    ('Sociedad Religiosa Bolivianada San Marcos de Arica','Sociedad Religiosa Bolivianada San Marcos de Arica'),
    ('Sociedad Religiosa Chilenitos de Santa Teresita','Sociedad Religiosa Chilenitos de Santa Teresita'),
    ('Sociedad Religiosa Chinos del Rosario de Andacollo','Sociedad Religiosa Chinos del Rosario de Andacollo'),
    ('Sociedad Religiosa Chuncho San Lorenzo','Sociedad Religiosa Chuncho San Lorenzo'),
    ('Sociedad Religiosa Chunchos de Iquique','Sociedad Religiosa Chunchos de Iquique'),
    ('Sociedad Religiosa Chunchos de la Virgen del Carmen','Sociedad Religiosa Chunchos de la Virgen del Carmen'),
    ('Sociedad Religiosa Chunchos de Victoria','Sociedad Religiosa Chunchos de Victoria'),
    ('Sociedad Religiosa Chunchos del Carmelo','Sociedad Religiosa Chunchos del Carmelo'),
    ('Sociedad Religiosa Chunchos Ñusta Huillac Pablo Vargas','Sociedad Religiosa Chunchos Ñusta Huillac Pablo Vargas'),
    ('Sociedad Religiosa Cullagua San Pedro','Sociedad Religiosa Cullagua San Pedro'),
    ('Sociedad Religiosa Cuyacas del Carmen de Victoria Vernal','Sociedad Religiosa Cuyacas del Carmen de Victoria Vernal'),
    ('Sociedad Religiosa Danzantes y Pieles Rojos','Sociedad Religiosa Danzantes y Pieles Rojos'),
    ('Sociedad Religiosa del Carmen Gitano','Sociedad Religiosa del Carmen Gitano'),
    ('Sociedad Religiosa del Carmen Gitano Español','Sociedad Religiosa del Carmen Gitano Español'),
    ('Sociedad Religiosa Devotos de la Virgen del Carmen Diablada Alianza','Sociedad Religiosa Devotos de la Virgen del Carmen Diablada Alianza'),
    ('Sociedad Religiosa Diablada del Salitre','Sociedad Religiosa Diablada del Salitre'),
    ('Sociedad Religiosa Diablada Hijos de María','Sociedad Religiosa Diablada Hijos de María'),
    ('Sociedad Religiosa Diablada María Reina','Sociedad Religiosa Diablada María Reina'),
    ('Sociedad Religiosa Diablada Oro Blanco','Sociedad Religiosa Diablada Oro Blanco'),
    ('Sociedad Religiosa Diablada Reina de Chile','Sociedad Religiosa Diablada Reina de Chile'),
    ('Sociedad Religiosa Diablada San José de Coya Sur','Sociedad Religiosa Diablada San José de Coya Sur'),
    ('Sociedad Religiosa Fraternidad Diablada Arcángel Miguel Hijos de María','Sociedad Religiosa Fraternidad Diablada Arcángel Miguel Hijos de María'),
    ('Sociedad Religiosa Gitanos de Belén','Sociedad Religiosa Gitanos de Belén'),
    ('Sociedad Religiosa Gitanos de Jesús Nazareno','Sociedad Religiosa Gitanos de Jesús Nazareno'),
    ('Sociedad Religiosa Gitanos de la Santa Cruz de Aroma','Sociedad Religiosa Gitanos de la Santa Cruz de Aroma'),
    ('Sociedad Religiosa Gitanos de María','Sociedad Religiosa Gitanos de María'),
    ('Sociedad Religiosa Gitanos de San Lorenzo','Sociedad Religiosa Gitanos de San Lorenzo'),
    ('Sociedad Religiosa Gitanos de Santa Rosa','Sociedad Religiosa Gitanos de Santa Rosa'),
    ('Sociedad Religiosa Gitanos del Carmen','Sociedad Religiosa Gitanos del Carmen'),
    ('Sociedad Religiosa Gitanos del Carmen Trinidad Ponce','Sociedad Religiosa Gitanos del Carmen Trinidad Ponce'),
    ('Sociedad Religiosa Gitanos del Colorado','Sociedad Religiosa Gitanos del Colorado'),
    ('Sociedad Religiosa Gitanos Escuderos del Carmen','Sociedad Religiosa Gitanos Escuderos del Carmen'),
    ('Sociedad Religiosa Gitanos Nuestra Señora del Rosario','Sociedad Religiosa Gitanos Nuestra Señora del Rosario'),
    ('Sociedad Religiosa Gitanos Peregrinos del Tamarugal','Sociedad Religiosa Gitanos Peregrinos del Tamarugal'),
    ('Sociedad Religiosa Gitanos Promesantes','Sociedad Religiosa Gitanos Promesantes'),
    ('Sociedad Religiosa Gitanos Promeseros del Carmen','Sociedad Religiosa Gitanos Promeseros del Carmen'),
    ('Sociedad Religiosa Gitanos Sagrado Corazón de Jesús','Sociedad Religiosa Gitanos Sagrado Corazón de Jesús'),
    ('Sociedad Religiosa Gitanos San Andrés','Sociedad Religiosa Gitanos San Andrés'),
    ('Sociedad Religiosa Gitanos San Luis de Avelino','Sociedad Religiosa Gitanos San Luis de Avelino'),
    ('Sociedad Religiosa Gitanos Virgen de Andacollo','Sociedad Religiosa Gitanos Virgen de Andacollo'),
    ('Sociedad Religiosa Gloria a Dios y María','Sociedad Religiosa Gloria a Dios y María'),
    ('Sociedad Religiosa Indios Dakotas','Sociedad Religiosa Indios Dakotas'),
    ('Sociedad Religiosa Indios Devotos de María','Sociedad Religiosa Indios Devotos de María'),
    ('Sociedad Religiosa Indios Jalaguayos','Sociedad Religiosa Indios Jalaguayos'),
    ('Sociedad Religiosa Indios Nubes Blancas de Palza y Lamilla','Sociedad Religiosa Indios Nubes Blancas de Palza y Lamilla'),
    ('Sociedad Religiosa Indios Sioux de María','Sociedad Religiosa Indios Sioux de María'),
    ('Sociedad Religiosa Kallahuayas del Carmen','Sociedad Religiosa Kallahuayas del Carmen'),
    ('Sociedad Religiosa Kullaguas María de la Paz','Sociedad Religiosa Kullaguas María de la Paz'),
    ('Sociedad Religiosa La Diablada de Victoria Devotos de la Virgen del Carmen','Sociedad Religiosa La Diablada de Victoria Devotos de la Virgen del Carmen'),
    ('Sociedad Religiosa Morenada Reina del Tamarugal','Sociedad Religiosa Morenada Reina del Tamarugal'),
    ('Sociedad Religiosa Moreno Sara del Carmen','Sociedad Religiosa Moreno Sara del Carmen'),
    ('Sociedad Religiosa Morenos Alí Babá','Sociedad Religiosa Morenos Alí Babá'),
    ('Sociedad Religiosa Morenos Alí Babá del Carmen','Sociedad Religiosa Morenos Alí Babá del Carmen'),
    ('Sociedad Religiosa Morenos Chilenos','Sociedad Religiosa Morenos Chilenos'),
    ('Sociedad Religiosa Morenos Chilenos Antonio Huerta Ugalde','Sociedad Religiosa Morenos Chilenos Antonio Huerta Ugalde'),
    ('Sociedad Religiosa Morenos de Humberstone','Sociedad Religiosa Morenos de Humberstone'),
    ('Sociedad Religiosa Morenos del Calvario','Sociedad Religiosa Morenos del Calvario'),
    ('Sociedad Religiosa Morenos del Carmen de La Tirana','Sociedad Religiosa Morenos del Carmen de La Tirana'),
    ('Sociedad Religiosa Morenos Humberto Gutiérrez R.','Sociedad Religiosa Morenos Humberto Gutiérrez R.'),
    ('Sociedad Religiosa Morenos Indúes','Sociedad Religiosa Morenos Indúes'),
    ('Sociedad Religiosa Morenos San Lorenzo','Sociedad Religiosa Morenos San Lorenzo'),
    ('Sociedad Religiosa Morenos Sara del Carmen','Sociedad Religiosa Morenos Sara del Carmen'),
    ('Sociedad Religiosa Morenos Tocopillanos','Sociedad Religiosa Morenos Tocopillanos'),
    ('Sociedad Religiosa Nuestra Señora de la Merced','Sociedad Religiosa Nuestra Señora de la Merced'),
    ('Sociedad Religiosa Osada del Salitre','Sociedad Religiosa Osada del Salitre'),
    ('Sociedad Religiosa Osos del Colorado','Sociedad Religiosa Osos del Colorado'),
    ('Sociedad Religiosa Piel Roja del Carmelo','Sociedad Religiosa Piel Roja del Carmelo'),
    ('Sociedad Religiosa Pieles Rojas Cruzados','Sociedad Religiosa Pieles Rojas Cruzados'),
    ('Sociedad Religiosa Pieles Rojas de la Ex Oficina Alianza','Sociedad Religiosa Pieles Rojas de la Ex Oficina Alianza'),
    ('Sociedad Religiosa Pieles Rojas del Carmen','Sociedad Religiosa Pieles Rojas del Carmen'),
    ('Sociedad Religiosa Pieles Rojas Indios Pampinos','Sociedad Religiosa Pieles Rojas Indios Pampinos'),
    ('Sociedad Religiosa Primera Diablada de Alianza','Sociedad Religiosa Primera Diablada de Alianza'),
    ('Sociedad Religiosa Promesantes del Salitre Pieles Rojas','Sociedad Religiosa Promesantes del Salitre Pieles Rojas'),
    ('Sociedad Religiosa Promeseros de la Virgen del Carmen','Sociedad Religiosa Promeseros de la Virgen del Carmen'),
    ('Sociedad Religiosa Reina Madre del Carmelo 1a. Diablada del Goyo','Sociedad Religiosa Reina Madre del Carmelo 1a. Diablada del Goyo'),
    ('Sociedad Religiosa Sambos Nuestra Señora del Carmen','Sociedad Religiosa Sambos Nuestra Señora del Carmen'),
    ('Sociedad Religiosa Seguidores de Cristo y María Diablada Imperial','Sociedad Religiosa Seguidores de Cristo y María Diablada Imperial'),
    ('Sociedad Religiosa Servidores de la Virgen del Carmen','Sociedad Religiosa Servidores de la Virgen del Carmen'),
    ('Sociedad Religiosa Siervos de Jesús y María','Sociedad Religiosa Siervos de Jesús y María'),
    ('Sociedad Religiosa Siervos de María Diablada de Iquique','Sociedad Religiosa Siervos de María Diablada de Iquique'),
    ('Sociedad Religiosa Tata Jachura','Sociedad Religiosa Tata Jachura'),
    ('Sociedad Religiosa Thukkuri Corazón de María','Sociedad Religiosa Thukkuri Corazón de María'),
    ('Sociedad Religiosa y Baile Cuyacas de Iquique','Sociedad Religiosa y Baile Cuyacas de Iquique')
)


class Post(models.Model):
    image = models.ImageField(upload_to='images')
    performance = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    costume = models.CharField(max_length=255)
    #guild = models.CharField(max_length=255, default="Sociedad Religiosa Chilenitos de Santa Teresita", choices=GUILDS)
    guild = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)
    character = models.CharField(max_length=255, default="")
    author = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.year

class Cofradia(models.Model):
    society = models.CharField(max_length=100)
    foundation = models.CharField(max_length=4)
    association = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    dance = models.CharField(max_length=50)
    history = models.TextField()

    def __str__(self):
        return self.society