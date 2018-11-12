from django.conf.urls import url
from django.urls import path
from app import views
from django.conf.urls import include

app_name = 'app'
urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    url(r'^.*a_test\.html', views.get_list_Lib, name='get_list_Lib'),
    path('<int:Lib_id>/', views.detail, name='detail'),
    path('<int:Lib_id>/Choix_Lib/', views.Choix_Lib, name='Choix_Lib'),
    url(r'^.*\.html', views.gentella_html, name='gentella'),
    # The home page
    url(r'^$', views.index, name='index'),
    url(r'^api/Catalogue/Libs/$', views.Catalogue_des_formations.as_view(), name='api-catalogue-libs'),

]
