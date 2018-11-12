from django.shortcuts import get_object_or_404,render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
import pandas as pd
from django.conf import settings
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Ligne_Creesp_Lib
from django.urls import reverse
from rest_framework.views import APIView
import math





class Catalogue_des_formations(APIView):
# you can these two variables down the road to enhance security, but for now just leave them blank
    def get(self, request, format=None):
        List_lib_catalogue = []
        print("////////////param////////////")
        df_catalogue = pd.read_csv(settings.STATIC_DATA+'Catalogue_Lib_Formation.csv')
        df_catalogue = df_catalogue.fillna('')
        lib_catalogue = df_catalogue['Libellé AF (Fr)'].drop_duplicates()
        for elem in lib_catalogue:
            List_lib_catalogue.append(elem)
        return Response([List_lib_catalogue])

def my_Connection_view(request):
    username = request.POST['username']
    password = request.POST['password']
    print("################")
    print(username)
    print("################")
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            template = loader.get_template('app/form_Correction_Lib.html')
            return HttpResponse(template.render(context, request))
        else:
            template = loader.get_template('app/login.html')
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('app/login.html')
        return HttpResponse(template.render(context, request))


def index(request):
    context = {}
    template = loader.get_template('app/form_Correction_Lib.html')
    return HttpResponse(template.render(context, request))


def logoutView(request):
    context = {}
    template = loader.get_template('registration/logged_out.html')
    return HttpResponse(template.render(context, request))


def get_list_Lib(request):
    print("################# get libs #######################")
    print(type(Ligne_Creesp_Lib.objects))
    latest_Lib_list = Ligne_Creesp_Lib.objects.all()
    context = {'latest_Lib_list': latest_Lib_list}
    return render(request, 'app/a_test.html', context)

def Choix_Lib(request, Lib_id):
    Lib_Courant = get_object_or_404(Ligne_Creesp_Lib, pk=Lib_id)

    selected_choice = request.POST['choice']
    print("#################")
    print(selected_choice)
    print("#################")

    Lib_Courant.Lib_Choisi = selected_choice
    Lib_Courant.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('app:get_list_Lib'))


def detail(request, Lib_id):
    Libelle = get_object_or_404(Ligne_Creesp_Lib, pk=Lib_id)
    return render(request, 'app/detail.html', {'Libelle': Libelle})

def gentella_html(request):
    print("################# gentella_html #######################")
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))
