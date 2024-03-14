from django.db import models

class Persona(models.Model):
    ALUMNE = 'alumne'
    PROFESSOR = 'professor'
    ROL_CHOICES = [
        (ALUMNE, 'Alumne'),
        (PROFESSOR, 'Professor'),
    ]

    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20)
    cognom = models.CharField(max_length=30)
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default=ALUMNE)
    email = models.EmailField(max_length=254)
    edat = models.IntegerField()
    sexe = models.CharField(max_length=1, choices=(('H', 'Hombre'), ('M', 'Mujer')))

    def __str__(self):
        return f"ID: {self.id}, Nom: {self.nom}, Cognom: {self.cognom}, Rol: {self.rol}, Email: {self.email}, Edat: {self.edat}, Sexe: {self.sexe}"