from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accountapp.views import AccountCreateView, hello_world

# 이름 변경 → url에서는 account 이지만, 파이썬 상에서는 accountapp으로 사용
app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),   # 함수형

    # 장고 기본 제공하는 login/logout view 바로 사용 가능
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create')   # 클래스 베이스 형 → 이름 뒤에 .as_view() 붙여야함

]
