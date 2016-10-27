from django.conf.urls import url
from semanticquery import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^search_query/$', views.search_query, name='search_query'),
    #url(r'^search_query_results/$', views.search_query_results, name='search_query_results'),
]