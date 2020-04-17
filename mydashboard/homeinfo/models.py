from django.db import models
import datetime


class HomeInfo(models.Model):
    memberName = models.CharField(max_length=100, editable=True)
    dob = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "homeinfo"


class PlaceInfo(models.Model):
    infoName = models.CharField(max_length=100, editable=True)
    infoValue = models.CharField(max_length=100, editable=True)
    updatedDate = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "placeinfo"

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.updatedDate = datetime.datetime.now()
