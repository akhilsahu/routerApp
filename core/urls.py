from django.urls import path, include, re_path

from rest_framework.authtoken import views

#from core.api.views import RouterDetailListView
app_name = "core"
urlpatterns = [
        path('', include('core.api.urls') , name="api-login"),
        path('api-token-auth/', views.obtain_auth_token, name='api-tokn-auth'),

    ]