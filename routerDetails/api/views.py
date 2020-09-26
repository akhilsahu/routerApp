from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from routerDetails.api.serializers import RouterDetailSerializer
from routerDetails.models import RouterDetail


class RouterDetailViewSet(viewsets.ModelViewSet):
    serializer_class = RouterDetailSerializer
    queryset = RouterDetail.objects.all()

