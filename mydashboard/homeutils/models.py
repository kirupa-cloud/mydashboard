from django.db import models
from uuid import uuid4


def generic_id():
    return uuid4().hex


class UtilityInfo(models.Model):
    id = models.CharField(max_length=32, primary_key=True, default=generic_id(), unique=True, editable=False)
    name = models.CharField(max_length=100)
    service_company = models.CharField(max_length=100)
    start_date = models.DateTimeField(blank=True, editable=True, null=True)
    end_date = models.DateTimeField(blank=True, editable=False, null=True)

    class Meta:
        db_table = "utility_info"


class UtilityPayments(models.Model):
    id = models.CharField(max_length=32, primary_key=True, default=generic_id(), unique=True, editable=False)
    utility_id = models.ForeignKey(UtilityInfo, related_name="utility_detail", on_delete=False)
    status = models.CharField(max_length=15, editable=True)
    service_start_date = models.DateTimeField(blank=True, editable=True, null=True)
    service_end_date = models.DateTimeField(blank=True, editable=True, null=True)
    amount = models.FloatField(blank=False)

    class Meta:
        db_table = "utility_payments"
