from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form): #profile form에서 user를 사용하지 않았는데 이미지의 주인이 누구인지 알게하기 위해서 서버내에서 구현하기 위함
        temp_profile = form.save(commit=False) #임시로 form 을 저장
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)