from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid
from django.utils.translation import gettext_lazy as _

'''
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
'''
        
class SocialPlatform(models.Model):
    platform = models.CharField(max_length=20, editable=False, null=False, blank=False, verbose_name="가입 경로")
    
    def __str__(self):
        return self.platform

    class Meta:
        db_table = "social_platform"
        verbose_name = '가입 경로'
        verbose_name_plural = '가입 경로'
    
class User(AbstractUser):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, verbose_name="UUID")
    username        = None
    first_name      = None
    last_name       = None
    sub             = models.CharField(max_length=64, db_index=True, null=False, blank=False, verbose_name="SUB") # 현재 sub는 unique=True 아님
    name            = models.CharField(max_length=64, null=False, blank=False, default='', verbose_name="이름")
    social          = models.ForeignKey(SocialPlatform, on_delete=models.CASCADE, verbose_name="가입 경로") # 무조건 social_platform에 1개이상 있어야함.
    date_joined     = models.DateTimeField(default=timezone.now, verbose_name="가입 날짜")
    last_joined     = models.DateTimeField(default=timezone.now, verbose_name="마지막 로그인")

    USERNAME_FIELD  = 'id'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "user"
        swappable = 'AUTH_USER_MODEL'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
        
class Doctor(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, verbose_name="UUID")  
    name            = models.CharField(max_length=64, null=False, blank=False, default='', verbose_name="이름")
    content         = models.TextField(max_length=1000, verbose_name="내용", default='')
    date_joined     = models.DateTimeField(default=timezone.now, verbose_name="가입 날짜")
    last_joined     = models.DateTimeField(default=timezone.now, verbose_name="마지막 로그인")

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "doctor"
        verbose_name = '의사'
        verbose_name_plural = '의사'

class TestList(models.Model):
    subject = models.CharField(max_length=100, editable=False, null=False, blank=False, verbose_name="검사 이름")
    content = models.CharField(max_length=100, editable=False, null=False, blank=False, verbose_name="검사 설명")
    count   = models.IntegerField(default=10, verbose_name="검사 항목 수")
    
    def __str__(self):
        return self.subject

    class Meta:
        db_table = "test_list"
        verbose_name = '검사 목록'
        verbose_name_plural = '검사 목록'
        
class GoalCategory(models.Model):
    subject = models.CharField(max_length=100, editable=False, null=False, blank=False, verbose_name="주제")

    class Meta:
        db_table = "goal_category"
        verbose_name = '목표 카테고리'
        verbose_name_plural = '목표 카테고리'
        
class GoalList(models.Model):
    category        = models.ForeignKey(GoalCategory, on_delete=models.CASCADE, verbose_name="카테고리")
    subject         = models.CharField(max_length=100, editable=False, null=False, blank=False, verbose_name="주제")
    mission1        = models.CharField(max_length=100, editable=False, null=False, blank=False, verbose_name="미션 1")
    mission2        = models.CharField(max_length=100, editable=False, null=False, blank=False, verbose_name="미션 2")
    mission3        = models.CharField(max_length=100, editable=False, null=False, blank=False, verbose_name="미션 3")
    
    def __str__(self):
        return self.subject
    
    class Meta:
        db_table = "goal_list"
        verbose_name = '목표 목록'
        verbose_name_plural = '목표 목록'
        
class UserGoal(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="사용자")
    goal            = models.ForeignKey(GoalList, on_delete=models.CASCADE, verbose_name="카테고리")
    success         = models.BooleanField(default=0, verbose_name="달성 여부")
    
    class Meta:
        db_table = "user_goal"
        verbose_name = '사용자 목표'
        verbose_name_plural = '사용자 목표'
        ordering = ['success']
        
class TestItem(models.Model):
    content         = models.TextField(max_length=200, verbose_name="내용", default='')
    type            = models.ForeignKey(TestList, on_delete=models.CASCADE, verbose_name="검사 종류") # 무조건 social_platform에 1개이상 있어야함.

    def __str__(self):
        return self.content
    
    class Meta:
        db_table = "test_item"
        verbose_name = '검사 종류'
        verbose_name_plural = '검사 종류'
    
class UserCheck(models.Model):
    selected_date   = models.DateField(default=timezone.now, verbose_name="선택 날짜")
    test_list       = models.ForeignKey(TestList, on_delete=models.CASCADE, verbose_name="선택된 질문")
    user            = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="사용자")
    value           = models.TextField(max_length=200, verbose_name="값", default='')

    def __str__(self):
        return self.user.name
    
    class Meta:
        db_table = "user_check"
        verbose_name = '사용자 체크리스트'
        verbose_name_plural = '사용자 체크리스트'
        ordering = ['-selected_date']
        
class Consult(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="사용자")
    Doctor          = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="의사")
    content         = models.TextField(max_length=200, verbose_name="내용", default='')

    class Meta:
        db_table = "consult"
        verbose_name = '상담'
        verbose_name_plural = '상담'