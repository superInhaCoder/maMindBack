from typing import Tuple
from django.db import transaction
from django.core.management.utils import get_random_secret_key
from rest_framework_simplejwt.tokens import RefreshToken
from myapp.models import User, UserCheck, UserGoal, SocialPlatform, TestList, TestItem, GoalList, GoalCategory
from datetime import datetime
from myapp.exceptions import DataTypeIncorrect, ServiceUnavailable
from myapp.serializers import GoalCategorySerializer, GoalListSerializer, UserGoalSerializer

@transaction.atomic
def create_super_user():
    user_create_superuser('e83b320f-afff-4838-ba37-b89743f6cb89', password='0510', name='관리자')

def init_test1():
    s = SocialPlatform(platform='Google')
    s.save()
    create_super_user()
    g = GoalCategory(subject='우울')
    g.save()
    g = GoalCategory(subject='불')
    g.save()
    g = GoalCategory(subject='걱정')
    g.save()
    g = GoalCategory(subject='스트레스')
    g.save()
    g = GoalCategory(subject='불면')
    g.save()

    t = TestList(subject='초기 테스트', content='초기 상태를 테스트합니다.', count=9)
    t.save()
    t = TestList(subject='우울증 마주하기 검사', content='유독 우울했 오늘 하루를 위해', count=20)
    t.save()
    t = TestList(subject='스트레스 환경 발견 테스트', content='내일을 향한 발걸음', count=20)
    t.save()
    t = TestList(subject='불안 환경 발견 검사', content='내일을 향한 발걸음', count=20)
    t.save()
    
def init_test2():
    # 초기 테스트
    t = TestItem(content='평소에는 아무렇지 않던 일들이 괴롭고 귀찮게 느껴졌나요?', type_id=1)
    t.save()
    t = TestItem(content='아무것도 먹고 싶지 않고, 식욕이 사라졌나요?', type_id=1)
    t.save()
    t = TestItem(content='누군가 도와준다고 하더라도 울적한 기분을 떨쳐 낼 수 없을 것 같나요?', type_id=1)
    t.save()
    t = TestItem(content='본인이 다른사람들보다 특별하다고 느끼나요?', type_id=1)
    t.save()
    t = TestItem(content='한번 화가 나면 잘 진정되지 않나요?', type_id=1)
    t.save()
    t = TestItem(content='남들과 대화하거나 속 이야기를 하기 싫어졌나요?', type_id=1)
    t.save()
    t = TestItem(content='요즘 전보다 신경질적이고 불안한가요?', type_id=1)
    t.save()
    t = TestItem(content='공연히 두려움을 느끼나요?', type_id=1)
    t.save()
    t = TestItem(content='사소한 일에 당황하고 어쩔줄을 모르나요?', type_id=1)
    t.save()

    # 우울 테스트
    t = TestItem(content='어떤 일을 하던지 정신을 집중하기가 힘들었나요?', type_id=2)
    t.save()
    t = TestItem(content='상당히 우울한 기분이 들었나요?', type_id=2)
    t.save()
    t = TestItem(content='모든 일들이 힘들게 느껴졌나요?', type_id=2)
    t.save()
    t = TestItem(content='앞으로의 일이 암담하게 느껴졌나요?', type_id=2)
    t.save()
    t = TestItem(content='지금까지의 내 인생이 실패작이라는 생각이 들었나요?', type_id=2)
    t.save()
    t = TestItem(content='적어도 보통 사람들 만큼의 능력은 있었다고 생각했나요?', type_id=2)
    t.save()
    t = TestItem(content='잠을 설치거나 잠에 들기 어려웠나요?', type_id=2)
    t.save()
    t = TestItem(content='두려움을 느꼈나요?', type_id=2)
    t.save()
    t = TestItem(content='평소에 비해 말수가 적었나요?', type_id=2)
    t.save()
    t = TestItem(content='세상에 홀로 있는 듯한 외로움을 느꼈나요?', type_id=2)
    t.save()
    t = TestItem(content='큰 불만 없이 생활했나요?', type_id=2)
    t.save()
    t = TestItem(content='사람들이 나에게 차갑게 대하는 것 같았나요?', type_id=2)
    t.save()
    t = TestItem(content='갑자기 울음이 나왔나요?', type_id=2)
    t.save()
    t = TestItem(content='슬픔을 느꼈나요?', type_id=2)
    t.save()
    t = TestItem(content='사람들이 나를 싫어하는 것 같았나요?', type_id=2)
    t.save()
    t = TestItem(content='도무지 무엇을 시작할 기운이 나지 않았나요?', type_id=2)
    t.save()
    t = TestItem(content='하는 일마다 힘들게 느껴졌나요?', type_id=2)
    t.save()
    t = TestItem(content='하루 중 대부분의 시간동안 울적했나요?', type_id=2)
    t.save()
    t = TestItem(content='즐겁게 생활하지 못했나요?', type_id=2)
    t.save()
    t = TestItem(content='이전보다 집중력이나 의사 결정 능력이 떨어졌나요?', type_id=2)
    t.save()
    
    # 스트레스 테스트
    t = TestItem(content='식욕이 없거나 혹은 폭식을 하나요?', type_id=3)
    t.save()
    t = TestItem(content='만사가 귀찮고 피곤한가요?', type_id=3)
    t.save()
    t = TestItem(content='기억력이 떨어지는 것 같나요?', type_id=3)
    t.save()
    t = TestItem(content='이해할 수 없는 상사나 동료, 혹은 가족이나 친구의 요구에 머리가 아픈가요?', type_id=3)
    t.save()
    t = TestItem(content='평소에 집중이 되지 않고 손에 일이 잘 잡히지 않나요?', type_id=3)
    t.save()
    t = TestItem(content='나에 대한 안좋은 소문을 듣고 시달린 적이 있나요?', type_id=3)
    t.save()
    t = TestItem(content='화를 자주 내고 짜증이 늘었나요?', type_id=3)
    t.save()
    t = TestItem(content='늘 무언가에게 쫓기는 느낌이 드나요?', type_id=3)
    t.save()
    t = TestItem(content='고민과 생각이 많아서 업무가 늦나요?', type_id=3)
    t.save()
    t = TestItem(content='주변사람들이나 가족들에게 요즘 너무 소흘하다는 이야기를 듣나요?', type_id=3)
    t.save()
    t = TestItem(content='일이 너무 지겹고 무료하나요?', type_id=3)
    t.save()
    t = TestItem(content='동료들이 너무 배려심이 없다고 느끼나요?', type_id=3)
    t.save()
    t = TestItem(content='사주풀이를 자주 살펴보게 되나요?', type_id=3)
    t.save()
    t = TestItem(content='일을 하는 도중 탈출의 욕구를 느끼나요?', type_id=3)
    t.save()
    t = TestItem(content='약속시간이 되기 전부터 초조함을 느끼나요?', type_id=3)
    t.save()
    t = TestItem(content='동료와 자주 말다툼을 하나요?', type_id=3)
    t.save()
    t = TestItem(content='내 생각보다 남의 이야기를 들으면 흔들리나요?', type_id=3)
    t.save()
    t = TestItem(content='아침에 눈뜨기가 너무 싫은가요?', type_id=3)
    t.save()
    t = TestItem(content='쉽게 부끄러움을 많이 타고 특정 반응에 민감한 편인가요?', type_id=3)
    t.save()
    t = TestItem(content='주변사람들로부터 리액션이 과하다는 이야기를 자주 듣나요?', type_id=3)
    t.save()
    
    # 불안 테스트
    t = TestItem(content='신경이 극도로 약해져서 몸과 마음을 가눌 수 없나요?', type_id=4)
    t.save()
    t = TestItem(content='손발이 떨리고 안절부절 못하게 되나요?', type_id=4)
    t.save()
    t = TestItem(content='머리가 아프고 목이 뻣뻣한가요?', type_id=4)
    t.save()
    t = TestItem(content='이유없이 몸이 약하고 피곤한가요?', type_id=4)
    t.save()
    t = TestItem(content='편히 오래 앉아 있을 수 없나요?', type_id=4)
    t.save()
    t = TestItem(content='가슴이 두근거리나요?', type_id=4)
    t.save()
    t = TestItem(content='어지러움을 느끼나요?', type_id=4)
    t.save()
    t = TestItem(content='졸도하거나 졸도한 것처럼 느껴질 때가 있나요?', type_id=4)
    t.save()
    t = TestItem(content='가슴이 답답한가요?', type_id=4)
    t.save()
    t = TestItem(content='손에 쥐가 나거나 저리나요?', type_id=4)
    t.save()
    t = TestItem(content='소변을 자주 보나요?', type_id=4)
    t.save()
    t = TestItem(content='얼굴이 쉽게 붉어지고 화끈거리나요?', type_id=4)
    t.save()
    t = TestItem(content='쉽게 잠이 들고 깊이 자나요?', type_id=4)
    t.save()
    t = TestItem(content='좋지 않은 꿈을 자주 꾸나요?', type_id=4)
    t.save()
    t = TestItem(content='이성적으로 참아 보려고 해도 불안을 견디기 힘든가요?', type_id=4)
    t.save()
    t = TestItem(content='걱정하는 것을 조절하거나 멈출 수가 없나요?', type_id=4)
    t.save()
    t = TestItem(content='피곤해서 다른 생각을 할 수 없나요?', type_id=4)
    t.save()
    t = TestItem(content='어떤 것에도 집중 할 수 없나요?', type_id=4)
    t.save()
    t = TestItem(content='주변에서 오는 모든 자극에 신경이 쓰이나요?', type_id=4)
    t.save()
    t = TestItem(content='불안하고 초조해서 직장 생활과 사회생활에 어려움이 있나요?', type_id=4)
    t.save()

def init_test3():
    g = GoalCategory(subject='우울')
    g.save()
    g = GoalCategory(subject='불')
    g.save()
    g = GoalCategory(subject='걱')
    g.save()
    g = GoalCategory(subject='스트레스')
    g.save()
    g = GoalCategory(subject='불면')
    g.save()
    
def init_test4():
    g = GoalList(subject='미라클 모닝 30', content='유독 우울했던 오늘 하루를 위해', step='BEGGINER', mission1='잠자리 정리하기', mission2='명상', mission3='러닝 또는 산책', category_id=1)
    g.save()
    g = GoalList(subject='여유로운 외출 준비 30분', content='우울하지 않을 오늘 하루', step='BEGGINER', mission1='일기 예보 확인', mission2='샤워', mission3='향수 뿌리기', category_id=1)
    g.save()
    g = GoalList(subject='미라클 모닝 30', content='유독 우울했던 오늘 하루를 위해', step='BEGGINER', mission1='잠자리 정리하기', mission2='명상', mission3='러닝 또는 산책', category_id=1)
    g.save()
    g = GoalList(subject='여유로운 외출 준비 30분', content='우울하지 않을 오늘 하루', step='BEGGINER', mission1='일기 예보 확인', mission2='샤워', mission3='향수 뿌리기', category_id=2)
    g.save()
    g = GoalList(subject='미라클 모닝 30', content='유독 우울했던 오늘 하루를 위해', step='BEGGINER', mission1='잠자리 정리하기', mission2='명상', mission3='러닝 또는 산책', category_id=2)
    g.save()
    g = GoalList(subject='여유로운 외출 준비 30분', content='우울하지 않을 오늘 하루', step='BEGGINER', mission1='일기 예보 확인', mission2='샤워', mission3='향수 뿌리기', category_id=2)
    g.save()
    g = GoalList(subject='미라클 모닝 30', content='유독 우울했던 오늘 하루를 위해', step='BEGGINER', mission1='잠자리 정리하기', mission2='명상', mission3='러닝 또는 산책', category_id=3)
    g.save()
    g = GoalList(subject='여유로운 외출 준비 30분', content='우울하지 않을 오늘 하루', step='BEGGINER', mission1='일기 예보 확인', mission2='샤워', mission3='향수 뿌리기', category_id=3)
    g.save()
    g = GoalList(subject='미라클 모닝 30', content='유독 우울했던 오늘 하루를 위해', step='BEGGINER', mission1='잠자리 정리하기', mission2='명상', mission3='러닝 또는 산책', category_id=3)
    g.save()
    g = GoalList(subject='여유로운 외출 준비 30분', content='우울하지 않을 오늘 하루', step='BEGGINER', mission1='일기 예보 확인', mission2='샤워', mission3='향수 뿌리기', category_id=4)
    g.save()
    g = GoalList(subject='미라클 모닝 30', content='유독 우울했던 오늘 하루를 위해', step='BEGGINER', mission1='잠자리 정리하기', mission2='명상', mission3='러닝 또는 산책', category_id=4)
    g.save()
    g = GoalList(subject='여유로운 외출 준비 30분', content='우울하지 않을 오늘 하루', step='BEGGINER', mission1='일기 예보 확인', mission2='샤워', mission3='향수 뿌리기', category_id=4)
    g.save()
    g = GoalList(subject='미라클 모닝 30', content='유독 우울했던 오늘 하루를 위해', step='BEGGINER', mission1='잠자리 정리하기', mission2='명상', mission3='러닝 또는 산책', category_id=5)
    g.save()
    g = GoalList(subject='여유로운 외출 준비 30분', content='우울하지 않을 오늘 하루', step='BEGGINER', mission1='일기 예보 확인', mission2='샤워', mission3='향수 뿌리기', category_id=5)
    g.save()
    g = GoalList(subject='미라클 모닝 30', content='유독 우울했던 오늘 하루를 위해', step='BEGGINER', mission1='잠자리 정리하기', mission2='명상', mission3='러닝 또는 산책', category_id=5)
    g.save()
    g = GoalList(subject='여유로운 외출 준비 30분', content='우울하지 않을 오늘 하루', step='BEGGINER', mission1='일기 예보 확인', mission2='샤워', mission3='향수 뿌리기', category_id=5)
    g.save()
    
def init_test5():
    u = UserCheck(value='1,2,4,3,0,2,3,1,0', test_list_id=1, user_id='e83b320fafff4838ba37b89743f6cb89')
    u.save()
    u = UserCheck(value='1,2,4,3,0,2,3,1,0,1,2,4,3,0,2,3,1,0,1,2,4,3,0,2,3,1,0,3,2,2', test_list_id=2, user_id='e83b320fafff4838ba37b89743f6cb89')
    u.save()

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
    try:
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
    except:
        raise ServiceUnavailable

@transaction.atomic
def get_user_goal_cal(user: User):
    try:
        userGoalSet = UserGoal.objects.filter(user=user, success=1).select_related('goal')
        category = GoalCategorySerializer(GoalCategory.objects.all(), many=True).data
        to = {}
        for c in category:
            print(c)
            to[c['id']] = c['subject']
        cnt = {}
        cnt2 = {'우울': 0, '스트레스': 0, '불안': 0}
        for f in userGoalSet:
            if f.goal.category_id not in cnt:
                cnt[f.goal.category_id] = 0
            cnt[f.goal.category_id] += 1
        for key in cnt:
            cnt2[to[key]] = cnt[key]
        return cnt2
    except:
        raise ServiceUnavailable

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
    
def get_goal_list_with_now(user: User, **data):
    d = GoalListSerializer(get_goal_list(**data), many=True).data
    lst = UserGoalSerializer(get_user_goal_with_success(user, 0), many=True).data
    now = {}
    try:
            for l in lst:
                    now[l['goal']] = 1
            for x in d:
                    if x['id'] in now:
                            x['now'] = 1
                    else:
                            x['now'] = 0
    except:
            raise ServiceUnavailable
    return now