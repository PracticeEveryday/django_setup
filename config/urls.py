from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("welcome/", welcome),
    path('test/', template_test),

    # index라는 뷰를 보게할 거야
    # path(주소, 뷰, 주소의 별명)
    path("", index)

]
