from django.forms import ModelForm
from django import forms

from routerDetails.models import RouterDetail


class RouterDetailsForm(ModelForm):
    class Meta:
        model  = RouterDetail
        fields = [ 'sap_id','internet_host_names','loopback','mac_address']