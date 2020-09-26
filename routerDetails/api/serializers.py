from rest_framework import serializers

from routerDetails.models import RouterDetail


class RouterDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = RouterDetail
        fields = ('id','sap_id','internet_host_names','loopback','mac_address')
