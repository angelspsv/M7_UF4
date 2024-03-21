from django.db import models

class Persona(models.Model):
    # el camp ID no esta perque ho afegira Django amb la migracio
    nom = models.CharField(max_length=20)
    cognom = models.CharField(max_length=30)
    edat = models.IntegerField()
    rol = models.CharField(max_length=10)
    email = models.EmailField(max_length=90)
    telefon = models.CharField(max_length=20)

    def __str__(self):
        return f"ID: {self.id}, Nom: {self.nom}, Cognom: {self.cognom}, Edat: {self.edat}, Rol: {self.rol}, Email: {self.email}, Telefon: {self.telefon}"