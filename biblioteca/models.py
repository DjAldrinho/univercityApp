from django.db import models


class Seccion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de Creacion', blank=False, null=False, auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Seccion'
        verbose_name_plural = 'Secciones'
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


class Bloque(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de Creacion', blank=False, null=False, auto_now=True, auto_now_add=False)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Bloque'
        verbose_name_plural = 'Bloques'
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=False, null=False)
    apellidos = models.CharField(max_length=150, blank=False, null=False)
    nacionalidad = models.CharField(max_length=50, blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de Creacion', blank=False, null=False, auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ('nombre',)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellidos)


class Categoria(models.Model):
    ESTADOS = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, blank=False, null=False)
    estado = models.CharField(max_length=1, choices=ESTADOS, null=False)
    fecha_creacion = models.DateField('Fecha de Creacion', blank=False, null=False, auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ('titulo',)

    def __str__(self):
        return self.titulo


class Editorial(models.Model):
    ESTADOS = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=False, null=False)
    estado = models.CharField(max_length=1, choices=ESTADOS, null=False)
    fecha_creacion = models.DateField('Fecha de Creacion', blank=False, null=False, auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


class MaterialBibliografico(models.Model):
    ESTADOS = (
        ('A', 'Disponible'),
        ('I', 'No Disponible'),
        ('E', 'En camino'),
    )

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, blank=False, null=False)
    portada = models.FileField(null=True)
    descripcion = models.TextField(blank=False, null=False)
    fecha_publicacion = models.DateField('Fecha de Publicacion', blank=False, null=False)
    cantidad = models.IntegerField(blank=False, null=False)
    precio = models.FloatField()
    autores = models.ManyToManyField(Autor)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    bloque = models.ForeignKey(Bloque, on_delete=models.CASCADE)
    numero_bloque = models.IntegerField()  # Numero donde se ubica el libro en el bloque.
    codigo = models.CharField(max_length=50, blank=False, null=False)  # Codigo unico del material
    edad_restringida = models.IntegerField(default=0)  # Cuando es 0, no tiene ninguna restricción
    fecha_creacion = models.DateField('Fecha de Creacion', blank=False, null=False, auto_now=True, auto_now_add=False)
    estado = models.CharField(max_length=1, choices=ESTADOS, null=False)

    def __str__(self):
        return self.titulo


class Libro(MaterialBibliografico):
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ('titulo',)


class Revista(MaterialBibliografico):
    class Meta:
        verbose_name = 'Revista'
        verbose_name_plural = 'Revistas'
        ordering = ('titulo',)


class Tesis(MaterialBibliografico):
    class Meta:
        verbose_name = 'Tesis'
        verbose_name_plural = 'Tesis'
        ordering = ('titulo',)


class Cliente(models.Model):
    ESTADOS = (
        ('A', 'Activa'),
        ('P', 'Pendiente'),
        ('F', 'Finalizada'),
        ('V', 'Vencida'),
        ('C', 'Cancelada')
    )

    id = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=150, blank=True, null=True)
    correo = models.EmailField(null=False, blank=False)
    password = models.CharField(max_length=150, blank=True, null=True)
    identificacion = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(blank=True, null=True, max_length=20)
    fecha_creacion = models.DateField('Fecha de Creacion', blank=False, null=False, auto_now=True, auto_now_add=False)
    estado = models.CharField(max_length=1, choices=ESTADOS, null=True, blank=True)

    def __str__(self):
        return '%s' % self.nombre_completo


class Reserva(models.Model):
    ESTADOS = (
        ('A', 'Activa'),
        ('P', 'Pendiente'),
        ('F', 'Finalizada'),
        ('V', 'Vencida'),
        ('C', 'Cancelada')
    )

    id = models.AutoField(primary_key=True)
    material = models.ForeignKey(MaterialBibliografico, on_delete=models.CASCADE, null=True)
    observacion = models.TextField(blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    fecha_creacion = models.DateField('Fecha de Creacion', blank=False, null=False, auto_now=True, auto_now_add=False)
    estado = models.CharField(max_length=1, choices=ESTADOS, null=True, blank=True)

    def __str__(self):
        return '%s (%s) %s' % (
            self.material.titulo, self.cliente.nombre_completo, self.fecha_creacion)
