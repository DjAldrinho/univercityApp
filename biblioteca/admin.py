from django.contrib import admin
from .models import Autor, Reserva, Cliente
from .models import Categoria
from .models import Editorial
from .models import Libro
from .models import Revista
from .models import Tesis
from .models import Bloque
from .models import Seccion

# Register your models here.

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editorial)
admin.site.register(Libro)
admin.site.register(Revista)
admin.site.register(Tesis)
admin.site.register(Bloque)
admin.site.register(Seccion)
admin.site.register(Cliente)
admin.site.register(Reserva)

