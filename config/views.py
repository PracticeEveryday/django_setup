# 뷰: 기능을 담당한다.(페이지 단위)
# 화면이 나타나는 뷰(템플릿 존재), 화면이 없는 뷰 <- 화면을 보느냐 안 보느냐에 따라 다르다
# 화면이 있건 없건 주소 URL은 있어야 한다.

# 뷰 내용(함수, 클래스), URL이 있으면 동작한다.

# 뷰의 코드 형식: 함수형, 클래스형
# 함수형: request 매개 변수로 받고(추가 매개 변수 가능) <- 모양은 함수다
#       내가 원하는 데로 동작들을 설계하고 만들고 싶을 떄

# 클래스형: CRUD 기존에 많이 사용하는 기능을 클래스로 만들어 두고 상속 받아서 사용하자

# 장고의 제네릭 뷰를 많이 사용 <- 읽기 뷰 쓰기 뷰 지우기 뷰

# 함수의 모양을 띄며 request라는 매개변수를 갖는다.
# 웹 브라우저를 통해 요청 값이 들어있다. session, cookie, headers ...

from django.http import HttpResponse
from django.shortcuts import render

# 이 View를 보기 위한 URL 주소가 필요하다.
def index(request):
    # 계산이나 데이터베이스 조회 수정 등록 등의 로직이 들어간다
    # 응답 메시지를 만들어서 반환한다.

    html = "<html><body>Hello Django</body></html>"
    return HttpResponse(html)

# 뷰의 이름은: welcome
# 뷰의 접속 주소: welcome/
# 내용: Welcome to Django.
def welcome(request):
    html = "<html><body>Welcome to Django</body></html>"
    return HttpResponse(html)


def template_test(request):
    # 기본 템플릿 폴더
    # 1. admin 앱
    # 2. 각 앱의 폴더에 있는 templates 폴더
    # 3. 우리가 설정할 폴더
    return render(request, 'test.html')