from django.db import models

# Create your models here.
# 모델: 데이터베이스를 SQL 없이 다루기 위해 모델을 사용한다.
# 우리가 데이터를 객체화하여 다루겠다!
# 모델 = 테이블
# 모델의 필드 = 테이블의 컬럼
# 인스턴스 = 테이블의 레코드 (행)
# 인스턴스의 필드의 값 = 레코드의 컬럼(열) 데이터 값

# 어떤 정보를 데이터 베이스에 저장해야 될 거같은데? -> 모델 만들기

class Bookmark(models.Model):
    # 테이블에 저장할 열 => 프로퍼티
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    # 필드의 종류가 결정하는 것
    # 1. 데이터 베이스의 컬럼 종류(글자? 숫자?)
    # 2. 제약 사항 (몇 글자까지?)
    # 3. Form의 종류
    # 4. Form에서 제약 사항

    # 인스턴스를 출력했을 떄 나오는 내용을 정의하는 메서드
    # 용도가 정해져 있는 애들은 앞뒤로 __가 붙어 있다.
    def __str__(self):
        return "이름: " + self.site_name + ", 주소: " + self.url


# 모델을 만들었다. => 데이터 베이스에 어떤 데이터들을 어떤 형태로 넣을지 결정
# 마이그레이션 => DB의 모델의 내용을 반영(테이블 생성)
# makemigrations => 모델의 변경사항을 추적해 기록해 놓는다.