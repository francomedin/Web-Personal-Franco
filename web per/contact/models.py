from django.db import models

# Create your models here.


class Contact(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    content = models.TextField()
    email=models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contacto'
        ordering = ['-created']

    def __str__(self):
        return self.name
