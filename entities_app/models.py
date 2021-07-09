from django.db import models


class Entities(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=256, unique=True)


class Engagements(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=256)
    user_name = models.ForeignKey(Entities, to_field='name', null=False, on_delete=models.CASCADE)
    current_status = models.BooleanField(default=False)




