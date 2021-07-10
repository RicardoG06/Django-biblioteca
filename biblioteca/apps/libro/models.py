from django.db import models

class Autors(models.Model):
        id = models.AutoField(primary_key = True)
        # in SQL -> id AUTO INCREMENT PRIMARY KEY
        nombre = models.CharField(max_length = 200 , blank = False , null = False)
        # in SQL -> nombre char(200) not null
        apellidos = models.CharField(max_length = 220 , blank = False , null = False)
        nacionalidad = models.CharField(max_length = 100 , blank = False , null = False)
        #Mas tipos para campos -> IntegerField , JSONField , URLField , ImageField , FileField
        fecha_creacion = models.DateField('Fecha de creacion' , auto_now = True , auto_now_add = False)

        class Meta:
            verbose_name = 'Autor'
            verbose_name_plural = 'Autores'
            ordering = ['nombre']

        def __str__(self):
            return self.nombre

class Libros(models.Model):
        id = models.AutoField(primary_key = True)
        titulo = models.CharField('Titulo' , max_length = 255 , blank = False , null = False)
        fecha_publicacion = models.DateField('Fecha de Publicacion' , blank = False , null = False )
        autor_id = models.ManyToManyField(Autors)
        #uno a uno : OneToOneField
        #uno a muchos: ForeignKey
        #muchos a muchos: ManyToManyField
        fecha_creacion = models.DateField('Fecha de creacion' , auto_now = True , auto_now_add = False)

        class Meta:
            verbose_name = 'Libros'
            verbose_name_plural = 'Libros'
            ordering = ['titulo']

        def __str__(self):
            return self.titulo
