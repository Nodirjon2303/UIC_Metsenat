from django.db import models
from Ariza.models import Ariza

class University(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Student(models.Model):
    t_turi_choices = (
        ("bakalavr", "Bakalavr daraja"),
        ('magistr', "Magistratura talabasi")
    )
    otm = models.ForeignKey(University, models.SET_NULL, null=True)
    fish = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    t_turi = models.CharField(max_length=25, choices=t_turi_choices)
    kontrakt = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fish


class Homiy(models.Model):
    homiy = models.ForeignKey(Ariza, models.CASCADE)
    student = models.ForeignKey(Student, models.CASCADE)
    amount = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.homiy.fish}      {self.student.fish}"


