from django.urls import path, include
from . import views

app_name = "routerdetails"

urlpatterns = [

     path('', views.RouterListView.as_view(), name="list"),
     path('n-data', views.RouterAddNData.as_view(), name="nData"),
     path('view-query', views.RouterList.as_view(), name="viewQuery"),
     path('list-auth', views.RouterAuthListView.as_view(), name="list"),

]
