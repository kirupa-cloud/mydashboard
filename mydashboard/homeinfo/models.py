from django.db import models


class HomeInfo(models.Model):
    memberName = models.CharField(max_length=100, editable=False)
    dob = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "homeinfo"