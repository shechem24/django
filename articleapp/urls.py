from django.urls import path
from django.views.generic import TemplateView

# 이름 변경 → url에서는 account 이지만, 파이썬 상에서는 accountapp으로 사용
app_name = "articleapp"

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
]
