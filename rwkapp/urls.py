from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', views. login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^eintraege/$', views.eintraege_list, name='eintraege_list'),
    url(r'^eintraege/(?P<pk>\d+)/$', views.eintraege_detail, name='eintraege_detail'),
    url(r'^eintrag/new/$', views.eintrag_new, name='eintrag_new'),
	url(r'^schuetze/$', views.schuetzen_list, name='schuetzen_list'),
    	url(r'^schuetze/(?P<pk>\d+)/$', views.schuetzen_detail, name='schuetzen_detail'),
    url(r'^schuetze/new/$', views.schuetze_new, name='schuetze_new'),
    url(r'^mannschaft/$', views.mannschaft_list, name='mannschaft_list'),
    url(r'^mannschaft/(?P<pk>\d+)/$', views.mannschaft_detail, name='mannschaft_detail'),
    url(r'^mannschaft/new/$', views.mannschaft_new, name='mannschaft_new'),
    url(r'^einzahlung/$', views.einzahlungen_list, name='einzahlungen_list'),
    url(r'^einzahlung/(?P<pk>\d+)/$', views.einzahlung_detail, name='einzahlung_detail'),
    url(r'^einzahlung/new/$', views.einzahlung_new, name='einzahlung_new'),
    url(r'^email/$', views.email, name='email'),
]