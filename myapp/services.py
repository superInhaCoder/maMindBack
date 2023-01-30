from typing import Tuple
from django.db import transaction
from django.core.management.utils import get_random_secret_key
from rest_framework_simplejwt.tokens import RefreshToken
from myapp.models import User, UserCheck, UserGoal, SocialPlatform, TestList, TestItem, GoalList, GoalCategory
from datetime import datetime
from myapp.exceptions import DataTypeIncorrect

@transaction.atomic
def create_super_user():
    user_create_superuser('e83b320f-afff-4838-ba37-b89743f6cb89', password='0510', name='관리자')

def init_test1():
    s = SocialPlatform(platform='Google')
    s.save()
    create_super_user()
    g = GoalCategory(subject='우울')
    g.save()
    g = GoalCategory(subject='스트레스')
    g.save()
    g = GoalCategory(subject='불안')
    g.save()

    t = TestList(subject='초기 테스트', content='초기 상태를 테스트합니다.', count=9)
    t.save()
    t = TestList(subject='우울 테스트', content='우울을 테스트합니다.', count=3)
    t.save()
    t = TestList(subject='스트레스 테스트', content='스트레스를 테스트합니다.', count=3)
    t.save()
    t = TestList(subject='불안 테스트', content='불안을 테스트합니다.', count=3)
    t.save()
    
def init_test2():
    # 초기 테스트id는 무조건 1
    t = TestItem(content='초기 테스트 1', type_id=1)
    t.save()
    t = TestItem(content='초기 테스트 2', type_id=1)
    t.save()
    t = TestItem(content='초기 테스트 3', type_id=1)
    t.save()
    t = TestItem(content='초기 테스트 4', type_id=1)
    t.save()
    t = TestItem(content='초기 테스트 5', type_id=1)
    t.save()
    t = TestItem(content='초기 테스트 6', type_id=1)
    t.save()
    t = TestItem(content='초기 테스트 7', type_id=1)
    t.save()
    t = TestItem(content='초기 테스트 8', type_id=1)
    t.save()
    t = TestItem(content='초기 테스트 9', type_id=1)
    t.save()
    
    t = TestItem(content='테스트 1', type_id=2)
    t.save()
    t = TestItem(content='테스트 2', type_id=2)
    t.save()
    t = TestItem(content='테스트 3', type_id=2)
    t.save()
    t = TestItem(content='테스트 4', type_id=3)
    t.save()
    t = TestItem(content='테스트 5', type_id=3)
    t.save()
    t = TestItem(content='테스트 6', type_id=3)
    t.save()
    t = TestItem(content='테스트 7', type_id=4)
    t.save()
    t = TestItem(content='테스트 8', type_id=4)
    t.save()
    t = TestItem(content='테스트 9', type_id=4)
    t.save()
    
def init_test3():
    g = GoalList(subject='목표1(우울)', mission1='물 마시기', mission2='일찍 일어나기', mission3='일찍 잠자기', category_id=1)
    g.save()
    g = GoalList(subject='목표2(우울)', mission1='물 마시기', mission2='일찍 일어나기', mission3='일찍 잠자기', category_id=1)
    g.save()
    g = GoalList(subject='목표3(스트레스)', mission1='물 마시기', mission2='일찍 일어나기', mission3='일찍 잠자기', category_id=2)
    g.save()
    
def init_test4():
    u = UserCheck(value='1,2,4,3,0,2,3,1,0', test_list_id=1, user_id='e83b320fafff4838ba37b89743f6cb89')
    u.save()
    
def init_test5():
    u = UserCheck(value='1,2,4,3,0,2,3,1,0,1,2,4,3,0,2,3,1,0,1,2,4,3,0,2,3,1,0,3,2,2', test_list_id=2, user_id='e83b320fafff4838ba37b89743f6cb89')
    u.save()
    
def init_test6():
    for i in range(17):
        t = TestItem(content=f'테스트 {i+4}', type_id=2)
        t.save()

@transaction.atomic
def user_create_superuser(id, password=None, **extra_fields) -> User:
    extra_fields = {
        **extra_fields,
        'is_staff': True,
        'is_superuser': True,
        'id': id
    }

    user = user_create('0', social="Google",
                        password=password, **extra_fields)

    return user

@transaction.atomic
def user_create(sub: str, social: str, password: str = None, **extra_fields) -> User:
    extra_fields = {
        'is_staff': False,
        'is_superuser': False,
        **extra_fields
    }

    user = User(sub=sub,
                social=SocialPlatform.objects.get(platform=social), 
                **extra_fields)

    if password:
        user.set_password(password)
    else:
        user.set_unusable_password()

    user.full_clean()
    user.save()

    return user

@transaction.atomic
def jwt_login(user: User):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh':  str(refresh),
        'access':   str(refresh.access_token),
    }

@transaction.atomic
def user_get_or_create(*, sub: str, social: str, **extra_data ) -> Tuple[User, bool]: # bool : 생성했으면 true 아니면 false
    # 나중에 필터에 소셜도 필요할 수 있음
    user = User.objects.filter(sub=sub).first()
    if user:
        user.last_login = datetime.now()
        user.save()
        return user, False
    return user_create(sub=sub, social=social, **extra_data), True

@transaction.atomic
def set_user_profile(*, user: User, **data):
    try:
        if 'is_active' in data['update']:
            user.is_active = data['update']['is_active']
        if 'name' in data['update']:
            user.name = data['update']['name']
    except: raise DataTypeIncorrect
    user.save()


@transaction.atomic
def get_test_item(**data):
    testListSet = TestItem.objects.filter(type=data['type'])
    return testListSet

@transaction.atomic
def get_test_list():
    testListSet = TestList.objects.all()
    return testListSet

@transaction.atomic
def get_goal_list(**data):
    if (data['category'] == -1):
        goalListSet = GoalList.objects.all()
    else:
        goalListSet = GoalList.objects.filter(category=data['category'])
    return goalListSet

@transaction.atomic
def get_goal_category():
    return GoalCategory.objects.all()

@transaction.atomic
def create_user_check(user: User, **data):
    userCheck = UserCheck(user=user, **data)
    return userCheck

@transaction.atomic
def create_user_goal(user: User, **data):
    userGoal = UserGoal(user=user, **data)
    userGoal.save()

@transaction.atomic
def get_user_check(user: User):
    userCheckSet = UserCheck.objects.filter(user=user)
    return userCheckSet

@transaction.atomic
def get_user_check_cal(user: User):
    userCheckSet = UserCheck.objects.filter(user=user).select_related('test_list')
    cal = {'우울 테스트': 0, '스트레스 테스트': 0, '불안 테스트': 0}
    cnt = {'우울 테스트': 0, '스트레스 테스트': 0, '불안 테스트': 0}
    for f in userCheckSet:
        v = list(map(int, f.value.split(',')))
        if f.test_list.id == 1:
            cal['우울 테스트'] += (v[0] + v[1] + v[2]) * 10
            cnt['우울 테스트'] += 1
            cal['스트레스 테스트'] += (v[3] + v[4] + v[5]) * 10
            cnt['스트레스 테스트'] += 1
            cal['불안 테스트'] += (v[6] + v[7] + v[8]) * 10
            cnt['불안 테스트'] += 1
        else:
            if f.test_list.subject not in cal:
                cal[f.test_list.subject] = 0
                cnt[f.test_list.subject] = 0
            cnt[f.test_list.subject] += 1
            for va in v:
                cal[f.test_list.subject] += va
    for key, value in cal.items():
        print(key, cal[key], cnt[key])
        cal[key] /= cnt[key]
    return cal

@transaction.atomic
def get_user_goal_cal(user: User):
    userGoalSet = UserGoal.objects.filter(user=user, success=1).select_related('goal')
    cnt = {}
    for f in userGoalSet:
        if f.subject not in cnt:
            cnt[f.subject] = 0
        cnt[f.subject] += 1
    return cnt

@transaction.atomic
def set_user_check(user: User, **data):
    userGoal = UserGoal(id=data['id'])
    try:
        if 'value' in data['update']:
            userGoal.success = data['update']['value']
    except: raise DataTypeIncorrect
    userGoal.save()

@transaction.atomic
def get_user_goal(user: User) -> bool:
    UserGoalSet = UserGoal.objects.filter(user_id=user)
    return UserGoalSet

@transaction.atomic
def get_user_goal_with_success(user: User, success) -> bool:
    UserGoalSet = UserGoal.objects.filter(user_id=user, success=success)
    return UserGoalSet

@transaction.atomic
def set_user_goal(user: User, **data):
    userGoal = UserGoal.objects.get(id=data['id'])
    try:
        if 'success' in data['update']:
            userGoal.success = data['update']['success']
    except: raise DataTypeIncorrect
    userGoal.save()