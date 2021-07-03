from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from accountapp.models import HelloWorld
from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# 함수형 view
def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        hello_world_list = HelloWorld.objects.all()

        # return render(request, 'accountapp/hello_world.html', context={ 'hello_world_list': hello_world_list })
        return HttpResponseRedirect(reverse('accountapp:hello_world'))  # reverse: 경로 만들기
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={ 'hello_world_list': hello_world_list })


# class 형 view
# CreateView: 장고 기본 제공하는 가입 양식
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')    # reverse는 class에서 사용할 수 없음(함수에서 사용). 해당주소로 렌더링
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'         # html에서 사용하는 변수 이름 설정
    template_name = 'accountapp/detail.html'