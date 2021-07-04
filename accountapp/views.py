from django.http.response import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator


from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld
from accountapp.decorators import account_ownership_required

# Create your views here.

has_ownership = [account_ownership_required, login_required]

# 함수형 view
@login_required
def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        hello_world_list = HelloWorld.objects.all()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))  # reverse: 경로 만들기
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={ 'hello_world_list': hello_world_list })



# class 형 view
# CreateView: 장고 기본 제공하는 가입 양식
class AccountCreateView(CreateView):
    model = User                                            # model (내장)
    form_class = UserCreationForm                           # form (내장)
    success_url = reverse_lazy('accountapp:hello_world')    # reverse는 class에서 사용할 수 없음(함수에서 사용). 해당주소로 렌더링
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'         # html에서 사용하는 변수 이름 설정
    template_name = 'accountapp/detail.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')    # reverse는 class에서 사용할 수 없음(함수에서 사용). 해당주소로 렌더링
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
