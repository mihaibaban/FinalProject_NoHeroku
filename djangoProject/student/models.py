from django.db import models

from professor.models import Professor


class Student(models.Model):
    class Meta:
        unique_together = ("first_name", "last_name")

    gender_choices = (('male','Male'),('female','Female'))

    first_name = models.CharField(max_length=30 )
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    is_olympic = models.BooleanField(default=False)
    email = models.EmailField(max_length=40)
    description = models.TextField(max_length=1000)
    start_date = models.DateTimeField()
    end_date  = models.DateField()
    average = models.FloatField()
    gender = models.CharField(max_length=20, choices=gender_choices)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    #campuri auxiliare
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True) # se va salva data si ora cand a fost adaugata inregistrarea
    updated_at = models.DateTimeField(auto_now=True) #se va modifica data si ora cand se vor realiza modificarile pe inregistrare


    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    @property
    def get_full_name(self):
         return str(self)



