from django.urls import path
from .views import *

urlpatterns = [
    # http://127.0.0,1/bookmark/???

    # ??? 만 남아있음. 1차에서 앞에 다 걸러짐
    # as_view -> 내부적으로 클래스형 뷰를 함수형 뷰로 고쳐줌
    # 클래스에서 as_view 꼭 필요하다.
    # urlpattenr의 이름이 3번째 매개변수의 name이다.
    path("", BookmarkListView.as_view(), name='list'),
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update')
]