from django.db import models
from softdelete.models import SoftDeleteModel

# Create your models here.
SAP_ID = (('AGI1', "AG1"),
          ("CSS", "CSS"))


class RouterDetail(SoftDeleteModel):
    #sap_id = models.CharField(max_length=255)
    sap_id = models.CharField(max_length=6, choices=SAP_ID, default='AGI1')
    internet_host_names = models.CharField(max_length=255)
    loopback = models.GenericIPAddressField(max_length=255)
    mac_address = models.CharField(max_length=255)

    class Meta:
        unique_together = ('internet_host_names', 'loopback' )