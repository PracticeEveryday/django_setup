from django.shortcuts import render

# Create your views here.
# CRUD: Create, Read, Update, Delete
# List

# Class View, Function View
# 웹 페이지에 접속한다 -> 페이지를 본다.
# URL 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다. -> 응답을 진행한다.
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Bookmark
from django.views.generic.detail import DetailView


class BookmarkListView(ListView):
    # 어떤 모델을 리브트 뷰로 보여줄 것인지 지정하는 것
    # ListView에 프로퍼티로 되어있다.
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']

    # url 패턴의 이름을 알려주면됨!
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
