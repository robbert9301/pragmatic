from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('create/', AccountCreateView.as_view(), name='create') #class는 accountcrateview를 써야한다
]