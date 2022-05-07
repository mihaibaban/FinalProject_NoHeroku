from django.db import models, connections, connection
from student.models import Student, Professor

class CustomForeignKey(models.ForeignKey):
    def validate(self, value, model_instance):
        print("functioneaza oke")


class Catalog(models.Model):
    nume_elev = models.CharField(max_length=50)
    private_name = models.CharField(max_length=50)
    nota_elev = models.FloatField()
    materie = models.CharField(choices=Professor.department_choices,max_length=50)
    def get_pk_from_sql(self, tuple):
        return tuple[0]

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        ids = Student.objects.filter(first_name=self.nume_elev).values_list("pk", flat=True)
        self.private_name = self.nume_elev
        nume, prenume = self.nume_elev.strip().split(", ")
        cursor = connections['default'].cursor()
        sql = "SELECT * FROM student_student WHERE first_name = %s AND last_name = %s"
        adr = (nume, prenume, )
        cursor.execute(sql, adr)
        pk = self.get_pk_from_sql(cursor.fetchone())
        self.nume_elev = pk
        super(Catalog, self).save()


