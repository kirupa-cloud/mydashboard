from django.db import models


class HomeInfo(models.Model):
    memberName = models.CharField(max_length=100, editable=True)
    dob = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "homeinfo"