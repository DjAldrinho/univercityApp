# Generated by Django 2.2.6 on 2019-12-11 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('apellidos', models.CharField(max_length=150)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de Creacion')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de Creacion')),
            ],
            options={
                'verbose_name': 'Bloque',
                'verbose_name_plural': 'Bloques',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150)),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], max_length=1)),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de Creacion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ('titulo',),
            },
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], max_length=1)),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de Creacion')),
            ],
            options={
                'verbose_name': 'Editorial',
                'verbose_name_plural': 'Editoriales',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='MaterialBibliografico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150)),
                ('portada', models.FileField(null=True, upload_to='')),
                ('descripcion', models.TextField()),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de Publicacion')),
                ('cantidad', models.IntegerField()),
                ('precio', models.FloatField()),
                ('numero_bloque', models.IntegerField()),
                ('codigo', models.CharField(max_length=50)),
                ('edad_restringida', models.IntegerField(default=0)),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de Creacion')),
                ('estado', models.CharField(choices=[('A', 'Disponible'), ('I', 'No Disponible'), ('E', 'En camino')], max_length=1)),
                ('autores', models.ManyToManyField(to='biblioteca.Autor')),
                ('bloque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Bloque')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de Creacion')),
            ],
            options={
                'verbose_name': 'Seccion',
                'verbose_name_plural': 'Secciones',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('materialbibliografico_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca.MaterialBibliografico')),
            ],
            options={
                'verbose_name': 'Revista',
                'verbose_name_plural': 'Revistas',
                'ordering': ('titulo',),
            },
            bases=('biblioteca.materialbibliografico',),
        ),
        migrations.CreateModel(
            name='Tesis',
            fields=[
                ('materialbibliografico_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca.MaterialBibliografico')),
            ],
            options={
                'verbose_name': 'Tesis',
                'verbose_name_plural': 'Tesis',
                'ordering': ('titulo',),
            },
            bases=('biblioteca.materialbibliografico',),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=150, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=150, null=True)),
                ('identificacion', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de Creacion')),
                ('estado', models.CharField(blank=True, choices=[('A', 'Activa'), ('P', 'Pendiente'), ('F', 'Finalizada'), ('V', 'Vencida'), ('C', 'Cancelada')], max_length=1, null=True)),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.MaterialBibliografico')),
            ],
        ),
        migrations.AddField(
            model_name='bloque',
            name='seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Seccion'),
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('materialbibliografico_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca.MaterialBibliografico')),
                ('editorial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Editorial')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ('titulo',),
            },
            bases=('biblioteca.materialbibliografico',),
        ),
    ]
