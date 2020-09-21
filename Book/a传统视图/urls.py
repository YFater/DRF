from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^books/$', views.BookInfoView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views.BookInfoDetailView.as_view())
]
