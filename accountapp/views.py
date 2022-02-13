from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.views.generic import CreateView

from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":

        tmp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = tmp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all() #helloworld의 모든 객체를 다 긁어올수 있다

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') #account creation에 성공했다면 그이후에 어디로 연결할 것인지에 대한 구문 & class에서는 reverse를 쓰지 못한다
    template_name = 'accountapp/create.html'