from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    # 대학 병원 -> 접수 하는 information 접수 -> 저쪽 어디 외과로 가세요 -> 간호사 앞에서 문진
    # 1차 -> 2차 -> 3차 타고 들어간다.

    # http://127.0.0.1/중앙창구/내과
    # http://127.0.0.1/중앙창구/외과

    # http://127.0.0.1/bookmark/list 입력
    # 1차 -> http://127.0.0.1/bookmark/ 여기까지만 찾아줌
    path('bookmark/', include('bookmark.urls')),

    path('admin/', admin.site.urls),
    path("welcome/", welcome),
    path('test/', template_test),


    # index라는 뷰를 보게할 거야
    # path(주소, 뷰, 주소의 별명)
    # path("", index)

]
