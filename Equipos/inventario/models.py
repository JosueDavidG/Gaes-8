from django.db import models
from django.utils.text import slugify

class productos(models.Model):
    nombreproducto =models.CharField(max_length=50)
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.nombreproducto)
        super(productos, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombreproducto
   




class Ropa(models.Model):
    producto = models.ForeignKey(productos,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='prenda', null=True, blank=True)
    descripcion= models.TextField(max_length=540)
    precio = models.FloatField()
    slug = models.SlugField(null=False, blank=False, unique=True)
    TALLA_CHOICES=[
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('X','X'),
        ('XL','XL'),
    ]
    talla =models.CharField(max_length=4, choices=TALLA_CHOICES, help_text='Seleccione  una talla')

    def save(self,*args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Ropa, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class productosImplementos(models.Model):
    ImplementoDeportivo =models.CharField(max_length=50)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.ImplementoDeportivo)
        super(productosImplementos, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.ImplementoDeportivo
    
class tamaños(models.Model):
    tamaño = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
            return self.tamaño

class ImplementosDeportivos(models.Model):
    producto = models.ForeignKey(productosImplementos,on_delete=models.CASCADE)
    tamaños = models.ForeignKey(tamaños,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=40)
    foto = models.ImageField(upload_to='Deportivo', null=True, blank=True)
    descripcion= models.TextField(max_length=540)
    precio = models.FloatField
    slug = models.SlugField(null=False, blank=False, unique=True)
   
    def save(self,*args, **kwargs):
        self.slug = slugify(self.nombre)
        super(ImplementosDeportivos, self).save(*args, **kwargs)

    def __str__(self):
            return self.nombre
  

