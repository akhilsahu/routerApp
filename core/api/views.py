import django_filters
from django.http import QueryDict
from django.views.generic import ListView
from rest_framework import viewsets, generics, mixins, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.views import APIView

from routerDetails.api.serializers import RouterDetailSerializer
from routerDetails.models import RouterDetail
from .filters import RouterFilter
from .serializers import userSerializers, LoginSerializer, RouterDetailsSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token


# class userviewsets(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = (TokenAuthentication, SessionAuthentication)
#     queryset = User.objects.all()
#     serializer_class = userSerializers


class RouterDetailAuthViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'head', 'put', 'delete', 'post', 'patch']
    serializer_class = RouterDetailsSerializer
    queryset = RouterDetail.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = RouterFilter

    def delete(self, request, *args, **kwargs):
        print(request, *args, **kwargs)

        value = request.GET.get('loopback')
        if value is None:
            value= request.data.get('loopback')
        str = ""
        q = RouterDetail.objects.filter(loopback=value).delete()
        print(q)
        # if value is None:
        #     q = RouterDetail.objects.delete()
        #my_filter = {}
        # for i in request.GET:
        #     print("i", request.GET.get(i))
        #     if request.GET.get(i) and i != "loopback":
        #         my_filter[i] = request.GET.get(i)
        #
        #         # q = q.filter( i=request.GET.get(i))
        #         # str+= i +"="+ request.GET.get(i)+","
        #
        # q = RouterDetail.objects.filter(**my_filter)
        #
        # if value:
        #     is_range = "," in value
        #     if is_range:
        #         ip_list = value.split(",")
        #         num = ip_list[0].rsplit(".", 1)
        #         num2 = ip_list[1].rsplit(".", 1)
        #         print(ip_list, num, num2)
        #         regex = num[0] + "\.[" + num[1] + "-" + num2[1] + "]{0,20}"
        #
        #
        #         range1 = int(num[1])
        #         range2 = int(num2[1])
        #
        #         q = q.filter(loopback__iregex=regex)
        #         str += "loopback__iregex=" + regex
        #         for qs in q:
        #             print(qs.id)
        #             r = qs.loopback.rsplit(".", 1)
        #
        #             if int(r[1]) not in range(range1, range2 + 1):
        #                 print(r)
        #                 q = q.exclude(id=qs.id)
        #     else:
        #         str += "loopback__contains=" + value
        #         q = q.filter(loopback__contains=value)

        return Response(data='delete success')

    def put(self, request, *args, **kwargs):
        print(*args, **kwargs)
        put = request.data
        print(request.data)
        value = put.get('loopback')

        q = RouterDetail.objects
        my_filter = {}
        for i in put:
            print("i", put.get(i))
            if put.get(i) and i != "loopback":
                my_filter[i] = put.get(i)

        q = RouterDetail.objects.filter(loopback=value).update(**my_filter)

        return Response(data=q)
        # if value:
        #     is_range = "," in value
        #     if is_range:
        #         ip_list = value.split(",")
        #         num = ip_list[0].rsplit(".", 1)
        #         num2 = ip_list[1].rsplit(".", 1)
        #         print(ip_list, num, num2)
        #
        #         regex = num[0] + "\.[" + num[1] + "-" + num2[1] + "]"
        #         q = q.filter(loopback__iregex=regex)
        #
        #         range1 = int(num[1])
        #         range2 = int(num2[1])
        #         for qs in q:
        #             print(qs.id)
        #             r = qs.loopback.rsplit(".", 1)
        #
        #             if int(r[1]) not in range(range1, range2 + 1):
        #                 q = q.exclude(id=qs.id)
        #     else:
        #         str += "loopback__contains=" + value
        #         q = q.filter(loopback__contains=value)
        # if not my_filter:
        #     return Response(data='No Data passed to be updated')
        # else:
        #     q.update(**my_filter)

    #
    # def patch(self, request, *args, **kwargs):
    #     print(*args, **kwargs)
    #     put = request.data
    #     print(request.data)
    #     value = put.get('loopback')
    #
    #     q = RouterDetail.objects
    #     my_filter = {}
    #     for i in put:
    #         print("i", put.get(i))
    #         if put.get(i) and i != "loopback":
    #             my_filter[i] = put.get(i)
    #
    #     q = RouterDetail.objects
    #     str = ""
    #     if value:
    #         is_range = "," in value
    #         if is_range:
    #             ip_list = value.split(",")
    #             num = ip_list[0].rsplit(".", 1)
    #             num2 = ip_list[1].rsplit(".", 1)
    #             print(ip_list, num, num2)
    #
    #             regex = num[0] + "\.[" + num[1] + "-" + num2[1] + "]"
    #             q = q.filter(loopback__iregex=regex)
    #
    #             range1 = int(num[1])
    #             range2 = int(num2[1])
    #             for qs in q:
    #                 print(qs.id)
    #                 r = qs.loopback.rsplit(".", 1)
    #
    #                 if int(r[1]) not in range(range1, range2 + 1):
    #
    #                     q = q.exclude(id=qs.id)
    #         else:
    #             str += "loopback__contains=" + value
    #             q = q.filter(loopback__contains=value)
    #     if not my_filter:
    #         return Response(data='No Data passed to be updated')
    #     else:
    #         q.update(**my_filter)
    #
    #     return Response(data=q)


# class RouterDetailListView(APIView):
#     http_method_names = ['get', 'head','put','delete','post']
#     queryset = RouterDetail.objects.all()
#     serializer_class = RouterDetailsSerializer
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
#
#     def filter_queryset(self, queryset):
#
#         for backend in list(self.filter_backends):
#             queryset = backend().filter_queryset(self.request, queryset, self)
#         return queryset
#
#     def get(self, request, format=None):
#         snippets = RouterDetail.objects.all()
#         serializer = RouterDetailsSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class LoginViewSet(GenericViewSet):
    serializer_class = LoginSerializer

    def create(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutViewSet(ViewSet):
    authentication_classes = (TokenAuthentication,)

    def create(self, request):
        django_logout(request)
        return Response(status=204)
