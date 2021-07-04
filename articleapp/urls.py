from articleapp.models import Article
from articleapp.views import ArticleCreateView, ArticleDeleteView, ArticleDetailView, ArticleListView, ArticleUpdateView
from django.urls import path
from django.views.generic import TemplateView

# 이름 변경 → url에서는 account 이지만, 파이썬 상에서는 accountapp으로 사용
app_name = "articleapp"

urlpatterns = [
    # path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
    path('list/', ArticleListView.as_view(), name='list'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]
