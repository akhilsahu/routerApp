import random

from faker import Faker
from faker.providers import internet

from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormMixin

# from django_seed import Seed


from routerDetails.forms import RouterDetailsForm
from routerDetails.models import RouterDetail


class RouterListView(FormMixin, TemplateView):
    form_class = RouterDetailsForm
    template_name = "routerDetails/routerdetail_list.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for visible in form:
            visible.field.widget.attrs['class'] = 'form-control'
        return form


class RouterAuthListView(FormMixin, TemplateView):
    form_class = RouterDetailsForm
    template_name = "routerDetails/routerdetail_list.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for visible in form:
            visible.field.widget.attrs['class'] = 'form-control'
        return form


class RouterList(ListView):
    queryset = RouterDetail.objects.order_by('-sap_id')
    context_object_name = 'router_list'
    template_name = 'routerDetails/router_list.html'


class RouterAddNData(TemplateView):
    template_name = "routerDetails/insertNMoreData.html"

    def post(self, request, *args, **kwargs):
        n = request.POST.get('num')

        if n.isnumeric():
            fake = Faker()
            fake.add_provider(internet)
            objs = RouterDetail.objects.bulk_create([RouterDetail(sap_id=random.choice(['AGI1', "CSS"]),
                                                                  loopback=fake.ipv4_private(),
                                                                  internet_host_names=fake.hostname(),

                                                                  mac_address=fake.mac_address())
                                                     for _ in range(int(n))])

        return redirect('/')
