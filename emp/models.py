from django.db import models

# Create your models here.


class Employee(models.Model):
    emp_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=256)
    reporting = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    salary = models.FloatField(default=0)
    # dept_id = models.IntegerField()

    def __str__(self):
        return self.name
