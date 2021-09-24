from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    # path('', views.HomeView.as_view()),
    path('api', views.ChartData.as_view()),
]
