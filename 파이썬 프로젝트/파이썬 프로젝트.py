from graphics import *
import os
import time
from PIL import Image as PILImage

FLOOR_FILES = ["1층.png", "2층.png"]

CHAPTER1_IMAGE_FILE = "챕터1.png"
CHAPTER2_IMAGE_FILE = "챕터2.png"
CHAPTER3_IMAGE_FILE = "챕터3.png"
CHAPTER4_IMAGE_FILE = "챕터4.png"
CHAPTER5_IMAGE_FILE = "챕터5.png"

FLOOR2_CASE1_IMAGE_FILE = "2층전시관1.png"
FLOOR2_CASE2_IMAGE_FILE = "2층전시관2.png"
FLOOR2_CASE3_IMAGE_FILE = "2층전시관3.png"
FLOOR2_CASE4_IMAGE_FILE = "2층전시관4.png"
FLOOR2_CASE5_IMAGE_FILE = "2층전시관5.png"
FLOOR2_CASE6_IMAGE_FILE = "2층전시관6.png"

WINDOW_W, WINDOW_H = 1100, 800
MAX_MAP_W, MAX_MAP_H = WINDOW_W - 60, WINDOW_H - 130

CHAPTER1_X = 265
CHAPTER1_Y = 530

CHAPTER2_X = 95
CHAPTER2_Y = 625

CHAPTER3_X = 250
CHAPTER3_Y = 690

CHAPTER4_X = 480
CHAPTER4_Y = 690

CHAPTER5_X = 480
CHAPTER5_Y = 590

INTERACT_DISTANCE = 70

# =========================
# 2층 전시관 위치 설정
# =========================
# 1층 좌표와 따로 수정할 수 있게 2층 전용 좌표를 따로 만들었습니다.
# X는 좌우 위치, Y는 위아래 위치입니다.
# vertical=False : 가로 전시관 / vertical=True : 세로 전시관

FLOOR2_CASE1_X = 820
FLOOR2_CASE1_Y = 675

FLOOR2_CASE2_X = 940
FLOOR2_CASE2_Y = 550

FLOOR2_CASE3_X = 940
FLOOR2_CASE3_Y = 380

FLOOR2_CASE4_X = 940
FLOOR2_CASE4_Y = 210

FLOOR2_CASE5_X = 820
FLOOR2_CASE5_Y = 150

FLOOR2_CASE6_X = 770
FLOOR2_CASE6_Y = 440

FLOOR2_DISPLAY_CASES = [
    (FLOOR2_CASE1_X, FLOOR2_CASE1_Y, "2층 전시관 1", False),
    (FLOOR2_CASE2_X, FLOOR2_CASE2_Y, "2층 전시관 2", True),
    (FLOOR2_CASE3_X, FLOOR2_CASE3_Y, "2층 전시관 3", True),
    (FLOOR2_CASE4_X, FLOOR2_CASE4_Y, "2층 전시관 4", True),
    (FLOOR2_CASE5_X, FLOOR2_CASE5_Y, "2층 전시관 5", False),
    (FLOOR2_CASE6_X, FLOOR2_CASE6_Y, "2층 전시관 6", True),
]


CHAPTER1_DESCRIPTIONS = [
    {"name": "꽃과 새 그림 속 매화", "desc": "여덟 폭의 꽃과 새 그림 중 첫 번째와 두 번째 폭에 매화와 한 쌍의 새를 그려 넣었다. 꽃과 새 그림은 행복한 가정과 부부의 애정을 상징하며, 매화는 추위 속에서도 먼저 피어나는 꽃으로 절개와 새봄을 상징한다."},
    {"name": "백자 항아리에 그려진 매화", "desc": "청화 백자 항아리에 매화와 새, 대나무가 그려져 있다. 매화는 새로운 시작과 재생을 뜻하며, 대나무와 함께 부부의 화목한 삶을 상징하기도 한다."},
    {"name": "백자 병에 그려진 매화", "desc": "청화 백자 병에 매화와 한 쌍의 새, 대나무가 표현되어 있다. 매화는 추운 날씨에도 가장 먼저 봄을 알리는 꽃으로, 행복한 가정을 상징한다."},
    {"name": "나전 필통에 표현된 매화", "desc": "종이나 붓을 보관하던 필통으로, 표면에는 자개로 매화, 난초, 국화, 대나무가 표현되어 있다. 이는 군자의 인품을 상징하는 사군자와 관련된다."},
    {"name": "문자 그림 속 매화", "desc": "문자 그림은 유교의 덕목을 글자와 그림으로 표현한 작품이다. 매화와 모란, 달 속의 토끼 등이 함께 그려져 교훈적인 의미를 담고 있다."},
    {"name": "두루주머니 등 장신구에 표현된 매화", "desc": "두루주머니와 장신구에는 매화가 화려하게 표현되어 있다. 매화는 절개와 고결함, 새로운 시작과 좋은 기운을 상징한다."},
]

CHAPTER2_DESCRIPTIONS = [
    {"name": "꽃과 새 그림 속 연꽃", "desc": "여덟 폭의 꽃과 새 그림 중 연꽃 그림이다. 연꽃은 진흙 속에서도 맑게 피어나는 꽃으로, 다산과 풍요, 맑은 마음을 상징한다."},
    {"name": "꽃과 새 그림 속 연꽃", "desc": "연꽃 주변에 물총새, 오리, 물고기 등이 함께 표현되어 있다. 부부의 사랑과 화목한 가정을 바라는 마음이 담겨 있다."},
    {"name": "붓집에 수놓은 연꽃", "desc": "붓을 보관하거나 휴대할 때 사용한 붓집이다. 앞면에 연꽃을 수놓았으며, 연꽃은 맑은 품격과 고결한 마음을 상징한다."},
    {"name": "연꽃을 사랑한 주돈이", "desc": "중국 송나라 학자 주돈이의 이야기를 담은 그림이다. 주돈이는 연꽃을 군자의 꽃이라 하였고, 이는 선비의 맑은 품격을 보여준다."},
    {"name": "기와를 장식한 연꽃", "desc": "연꽃무늬가 새겨진 기와이다. 연꽃은 불교미술에서 청정함과 성스러움을 상징하며, 건축 장식에도 자주 사용되었다."},
    {"name": "관음보살과 연봉오리", "desc": "관음보살상이 연봉오리를 들고 있는 모습이다. 연봉오리는 깨달음의 가능성을 상징하며, 자비와 구원의 의미를 담고 있다."},
    {"name": "범종에 표현된 연꽃", "desc": "범종에 연꽃 장식이 표현되어 있다. 연꽃은 불교에서 청정과 깨달음을 상징하며, 범종의 신성한 의미를 더해준다."},
]

CHAPTER3_DESCRIPTIONS = [
    {"name": "모란 그림", "desc": "여덟 폭의 모란 그림으로 바위 위에 활짝 핀 모란과 그 주위를 날아드는 호랑나비를 각 폭에 그려 넣었다. 모란은 크고 풍성한 꽃송이, 화려한 자태 때문에 부귀와 영화를 상징하며 꽃 중의 왕으로 사랑받았다. 모란과 바위, 나비는 세밀하게 묘사되었고 금칠한 나비 날개가 그림의 화려함을 더한다."},
    {"name": "분청사기 병에 장식된 모란 덩굴", "desc": "입이 나팔처럼 벌어지고 목이 둥글게 말린 분청사기 병이다. 잘록한 목과 아래로 갈수록 풍만해지는 몸체는 조선 초기 병의 특징을 보여준다. 몸체에는 모란 덩굴무늬가 장식되어 있으며, 고려 상감 청자의 전통을 이은 이 병에는 풍요로운 삶이 오래도록 이어지기를 바라는 옛사람들의 마음이 담겨 있다."},
    {"name": "백자에 그려진 모란", "desc": "항아리는 입이 밖으로 벌어졌고 몸통의 중간으로 갈수록 풍만해지다가 다시 좁아진다. 입에는 청화 안료로 두 줄의 선과 아자 무늬를, 어깨 위에는 여의두무늬를, 몸통에는 활짝 핀 모란꽃을 그려 넣었다. 병은 입술이 밖으로 살짝 벌어졌으며 목은 길고 아래로 내려갈수록 몸통이 풍만해지는 조선 후기 백자의 특징을 가지고 있다. 모란은 부귀와 풍요를 상징하는 꽃으로, 이 항아리와 병에는 풍요로운 삶을 바랐던 옛사람들의 마음이 담겨 있다."},
    {"name": "붓집과 귀주머니에 수놓은 모란", "desc": "붓을 보관하거나 휴대할 때 사용한 붓집은 남색 천 바탕 위에 입체적인 구름과 학을, 아래쪽에는 모란을 수놓았다. 돈이나 작은 소지품을 넣어 허리에 차거나 손에 지녔던 귀주머니에도 활짝 핀 모란이 수놓아져 있다. 모란은 부귀와 풍요를 상징하며, 일상생활에 쓰인 붓집과 귀주머니에 모란을 수놓은 것은 행복하고 풍요로운 삶이 함께하기를 바랐던 옛사람들의 소망을 보여준다."},
    {"name": "나전 함을 장식한 모란", "desc": "일상생활에서 여러 물건을 보관하던 상자로 조개껍데기를 이용해 활짝 핀 모란 넝쿨무늬를 화려하게 장식하였다. 식물 줄기와 무늬의 경계를 꾸미며 많은 금속 선으로 장식하여 은은하면서도 화려하게 보이게 하였다. 뚜껑 윗면에는 꽃잎 모양을 품 안에 안고 도는 형태의 모란을 표현하였다. 꽃향은 평안한 삶을, 모란 넝쿨은 끊임없이 이어지는 풍요를 상징한다."},
    {"name": "인두판 등 생활용품에 수놓은 모란", "desc": "인두판은 옷이나 천의 구김을 펼 때 사용한 생활 도구로, 학소나무, 불로초, 모란과 나비, 연꽃과 새가 수놓아져 있다. 이 가운데 중앙에 크게 표현된 모란은 부귀와 풍요를 상징하며, 나비와 어우러져 기쁨 가득한 삶에 대한 바람을 전한다. 자수 베개모와 바늘꽂이에도 모란이 표현되어 있어 옛사람들이 행복하고 풍요로운 삶을 바랐음을 엿볼 수 있다."},
    {"name": "나전 이층 농을 장식한 모란", "desc": "가족들의 옷과 물건을 보관하던 이층 농으로 자개를 이용해 꽃과 새, 물가 풍경을 화려하게 장식하였다. 농은 혼수품으로 마련되던 대표적인 가구였으며 주로 여성들의 생활공간에서 사용되었다. 앞면에는 여러 꽃나무와 넝쿨식물, 팽 등 새를 자개로 장식하였고 특히 어린아이 아래에는 부귀와 풍요를 상징하는 모란을 화려하게 장식하였다. 이 나전 이층 농은 옛사람들이 바랐던 풍요롭고 행복한 삶에 대한 염원을 잘 보여준다."},
]

CHAPTER4_DESCRIPTIONS = [
    {"name": "청자 분합을 장식한 국화", "desc": "고려시대에 화장품 분가루를 담는 데 사용한 청자 합이다. 뚜껑에는 국화무늬를 상감기법으로 장식하고, 가장자리에는 구슬 무늬와 넝쿨무늬를 새겨 넣었다. 작은 그릇 위에도 맑게 피는 꽃으로 여겨졌던 국화를 새겨 넣어 고결함과 절개, 장수를 상징하였다."},
    {"name": "꽃과 새 그림 속 국화", "desc": "여덟 폭으로 이루어진 꽃과 새 그림 가운데 마지막 폭에 국화와 한 쌍의 새를 그렸다. 화면 위쪽에는 활짝 핀 국화를 중심으로 여러 송이의 국화가 그려져 있고, 아래쪽 바위 위에는 다정하게 마주한 새 한 쌍이 앉아 있다. 국화는 늦가을 찬 서리 속에서도 맑은 꽃을 피워 고결한 품격과 장수를 상징하는 그림으로 사랑받았다."},
    {"name": "청자 잔과 받침을 장식한 국화","desc": "청자로 만든 잔과 받침이다. 잔은 꽃잎이 벌어진 듯한 형태로 만들었고, 받침 역시 연꽃잎을 닮은 모습으로 꾸며 전체적으로 화려하면서도 단정한 인상을 준다. 잔의 바깥 면과 받침의 넓은 전에는 국화무늬를 장식하였다. 국화는 늦가을 서리를 맞으면서도 맑게 피는 꽃으로, 예로부터 고결함과 장수를 상징하였다."}, 
    {"name": "벼루함에 새겨진 국화", "desc": "벼루함은 벼루 등 글씨를 쓰는 데 필요한 문방구를 넣어 보관하던 상자이다. 이 벼루함에는 대나무, 매화, 국화와 함께 모란이 새겨져 있다. 국화는 난초와 더불어 사군자라 불리며 선비가 닮고자 한 절개와 고결한 품성을 상징하였다. 상자에 새겨진 국화 문양에는 아름답고 평안한 삶을 바라는 마음이 담겨 있다."},
    {"name": "백자 병에 그려진 국화", "desc": "청화 백자 병으로, 입술은 밖으로 살짝 벌어지고 긴 목에서 풍만한 몸통으로 이어지는 조선 후기 백자 병의 특징을 보인다. 전체에는 푸른빛이 감도는 유약을 입혔으며, 몸통에는 청화 안료로 국화와 박쥐를 그려 넣었다. 국화는 가을의 정취와 장수를, 박쥐는 복을 상징하여 건강하고 행복한 삶을 바라는 마음이 담겨 있다."},
    {"name": "분청사기 대접을 장식한 국화", "desc": "분청사기 대접으로 입술은 밖으로 살짝 벌어지고, 입에서 굽으로 완만하게 내려오다가 점점 좁아진다. 안쪽 면과 바깥에는 도장을 찍듯 인화 기법으로 국화무늬를 장식하였고, 바깥 면에는 연속된 문양이 반복되어 있다. 단정한 형태와 반복적인 무늬가 어우러져 조선 초기 분청사기의 소박하면서도 활달한 장식미를 보여준다."},
    {"name": "뒤꽃이에 장식된 국화", "desc": "뒤꽂이는 조선시대 여인들이 쪽진 머리 뒤에 덧꽂아 장식하던 장신구이다. 한쪽 끝은 뾰족하고 다른 한쪽 끝에는 나비가 꽃을 향해 날아드는 듯한 장면을 표현하였다. 나비와 함께 국화와 매화를 칠보로 화려하게 입히고, 중앙에는 호박을 장식해 은은한 멋을 더하였다. 국화는 가을의 정취와 장수를, 매화는 추위를 이겨 피어나는 절개를 상징한다."},
]

CHAPTER5_DESCRIPTIONS = [
    {"name": "은장도에 새겨진 소나무", "desc": "은장도는 은으로 장식한 작은 휴대용 칼이다. 실용적인 도구이면서 몸에 지니는 장신구의 성격을 지녔으며, 조선시대에는 절개와 바른 몸가짐을 상징하는 물건으로 여겨졌다. 칼집과 손잡이에는 소나무, 사슴, 대나무, 거북이 등 장수를 상징하는 십장생무늬가 새겨져 있다. 특히 사철 푸른 소나무는 변함없는 생명력과 장수를 뜻한다. 은장도에 새겨진 이러한 무늬에는 오래도록 건강하고 평안하게 살기를 바라는 옛사람들의 소망이 담겨 있다."},
    {"name": "백자 병에 그려진 소나무", "desc": "청화 백자 병으로, 입술은 밖으로 살짝 벌어지고 긴 목에서 풍만한 몸통으로 이어지는 조선 후기 백자 병의 특징을 보인다. 몸통에는 소나무, 대나무, 불로초, 사슴, 학, 구름 등 십장생무늬를 그려 넣었다. 특히 생명력과 장수를 상징하는 소나무는 함께 그려진 해, 물, 구름 등과 어우러져 건강하고 오래 살기를 바라는 마음을 담고 있다."},
    {"name": "귀주머니에 수놓은 소나무", "desc": "귀주머니는 위쪽 양옆에 귀처럼 뾰족한 모서리가 있는 주머니이다. 돈이나 작은 소지품을 넣어 허리춤에 차거나 손에 들고 다녔으며, 색실로 화려하게 수놓아 장신구로도 쓰였다. 귀주머니에는 소나무를 중심으로 사슴, 학, 불로초, 바위, 물과 모란을 수놓았다. 소나무는 사철 푸른 모습으로 변치 않는 생명력과 장수를 상징하며, 여러 장생 문양과 함께 건강하고 오래 살기를 바라는 뜻을 담고 있다."},
    {"name": "수저집에 수놓은 소나무", "desc": "숟가락과 젓가락을 보관하던 주머니로, 붉은 바탕의 천에 해, 구름, 사슴, 소나무 등 십장생을 수놓고 술을 달아 장식하였다. 특히 소나무는 사철 푸른 잎과 오래 사는 특징 때문에 장수와 변치 않는 생명력을 상징하였다. 수저를 담는 주머니에 소나무와 여러 십장생무늬를 수놓은 것은 가족의 건강과 장수, 행복한 삶을 바라는 마음을 담은 것이다."},
    {"name": "도시락 통(찬합)에 새겨진 소나무", "desc": "나무로 만든 도시락 통, 곧 찬합으로 전체를 옻칠로 마무리하였다. 앞면에는 네 개의 서랍이 들어가 있으며, 소나무를 배경으로 불로초와 사슴을 새겼다. 사철 푸른 소나무는 변치 않는 절개와 장수를 상징하였으며, 사슴과 불로초 역시 오래 살기를 바라는 뜻을 지닌 길상문으로 여겨졌다."},
    {"name": "나무 베개에 새겨진 소나무", "desc": "나무로 만든 베개는 시원하여 주로 여름철에 사용하였다. 이 베개는 나무판 네 개로 겉 틀을 만들고, 그 안에 소나무와 사슴을 새긴 나무판을 끼워 넣은 것이다. 소나무는 추운 겨울에도 푸른 잎을 지녀 변치 않는 생명력과 장수를 상징하며, 사슴은 신선과 장수를 떠올리게 하는 동물이다."},
    {"name": "팔걸이에 새겨진 소나무", "desc": "나무로 만든 팔걸이로, 앉을 때 팔을 얹거나 몸을 기대어 편하게 사용하는 받침대이다. 위아래의 나무판은 가운데를 파내어 타원형으로 만들고, 그 사이에 소나무와 사슴을 새긴 판을 끼워 넣었다. 소나무는 변치 않는 생명력과 장수를 상징하며, 사슴은 오래 산다고 여겨진 길상 동물이다."},
    {"name": "십장생 그림 속 소나무", "desc": "오래 산다고 여겨지는 해, 구름, 학, 소나무, 대나무, 사슴, 불로초, 물, 거북, 바위 등을 한 폭에 그린 십장생 그림이다. 이 가운데 소나무는 사철 푸른 잎을 지녀 변치 않는 생명력과 장수를 상징하는 대표적인 나무이다. 십장생 그림에서 소나무는 학, 사슴, 불로초 등 장수를 뜻하는 동물과 식물 사이에 함께 그려져 오래도록 건강하게 살기를 바라는 마음을 드러낸다."},
]

FLOOR2_CASE1_DESCRIPTIONS = [
    {"name": "전석길 교수 기증 화폐", "desc": "행소박물관은 2001년 의과대학 전석길 교수로부터 한국과 중국의 옛날 화폐 3,000여 점을 기증받았다. 이를 통해 행소박물관은 다양한 화폐 소장 박물관으로 도약하는 계기를 마련하였다"},
    {"name": "청자 상감 여지 국화무늬 대접", "desc": "청자 대접으로 바깥쪽 면에는 풍요로운 삶을 상징하는 모란꽃과 넝쿨무늬를, 안쪽 면에는 넝쿨무늬와 여지무늬를 흑백 상감하였다. 여지(荔枝)는 중국 남부지역이 원산지인 열대과일로 고려시대 관리나 왕세자의 허리띠를 장식했던 문양이기도 하다.."},
    {"name": "백자 청화 구름과 용무늬 항아리", "desc": "구름 사이로 꿈틀거리는 용을 그려 넣은 청화 백자 항아리이다. 항아리의 입은 곱게 올라가고 어깨는 풍만하며 몸통으로 내려갈수록 서서히 좁아지다가 살짝 벌어진다. 굽은 안쪽으로 서서히 좁아진다. 따껑과 입에는 구름을, 어깨 위에는 여의두무늬를, 몸통에는 구름과 약동하는 네 개의 발톱을 가진 용을 그려 넣었다. 조선시대 궁중 의례를 그린 그림이나 1795년 정조가 혜경궁 홍씨의 회갑을 기념하여 화성 행차 시 행사의 절차를 기록한 『원행을묘정리의궤(園幸乙卯整理儀軌)』를 통해 볼 때 이 항아리의 용도는 의례 때 꽃을 꽂아 사용하거나 술을 담았던 도자기로 추정된다. 곧고 긴 목과 긴 계란 모양의 몸통으로 볼 때 19세기에 만들어진 것으로 볼 수 있다."},
    {"name": "두 귀 달린 토기 단지", "desc": "김천 송죽리유적에서 출토된 신석기시대 토기 단지이다. 토기의 저부는 둥근 모습이고 몸체의 중앙부에서 상부 일부까지 새 날개모양의 기하학문이 새겨져 있다. 토기의 중앙부에서 약간 상부측에 두 개의 귀가 달려 있고 그 귀에는 구멍을 뚫었다. 두 개의 구멍을 뚫어 놓은 것은 무언가를 매달 수 있도록 한 것으로 보인다. 이러한 토기에 표현된 다양한 문양과 구멍을 뚫은 손잡이 등을 통해 당시 김천에 거주한 신석기인들의 유행과 개성을 엿볼 수 있다."},
    {"name": "대나무 필통", "desc": "대나무로 만들어진 필통으로 붓 등을 담아 놓기 위한 도구이다. 세 개의 대나무를 서로 높이가 다르게 잘라 나무 바닥판에 끼워 넣어 만들었다. 필통의 표면에는 학과 매화, 번개무늬 등이 조각되어 있다. 학은 신선이 사는 세상의 새로 천 년을 장수한다고 믿어 왔으며 오래 사는 몇 가지인 십장생 중 하나이다. 매화는 얼어붙은 땅속에 뿌리를 내려 추위를 이겨내고 제일 먼저 꽃을 피워 곧은 선비정신을 상징한다."},
    {"name": "오래 살고 싶은 마음, 십장생", "desc": "십장생이란 세상에서 가장 오래 산다고 여겨지는 열 가지인 해, 구름, 산, 물, 소나무, 학, 거북, 사슴, 바위, 불로초를 말한다."},
    {"name": "고령 지산동 고분 출토 유물", "desc": "계명대학교 행소박물관이 1977~87년에 조사한 고령 지산동 45호분과 32~35호분에서 출토된 유물들이다. 45호분에 대한 발굴은 고령 지산동고분군에 대한 해방 이후 최초의 공식적인 발굴조사라고 할 수 있다. 고령 지산동 고분 발굴조사를 통해 대가야 고분의 성격과 순장문화 등 대가야의 문화를 이해하는데 많은 도움이 되었다. 또한 금동관 및 갑옷 등의 출토유물들을 통해 화려한 대가야의 금속공예를 엿볼 수 있는 계기가 되었다."},
    ]

FLOOR2_CASE2_DESCRIPTIONS = [
    {"name": "주먹도끼", "desc": ""},
    {"name": "찍개", "desc": ""},
    {"name": "주먹찌르개", "desc": ""},
    {"name": "긁개", "desc": ""},
    {"name": "돌망치", "desc": ""},
    {"name": "낙동강 유역", "desc": "경상북도 성주 관화리·취곡리 일대에서 채집한 구석기시대 유물이다."},
    {"name": "남강 유역", "desc": "경상남도 진주 내촌리의 남강 유역 일대에서 채집한 구석기시대 유물이다."},
    {"name": "섬진강·보성강 유역", "desc": "전라남도 순천, 보성 등 섬진강·보성강 유역 일대에서 채집한 구석기시대 유물이다."},
    ]

FLOOR2_CASE6_DESCRIPTIONS = [
    {"name": "빗살무늬토기", "desc": "빗살무늬토기는 주로 강가나 해안가 등에 위치하고 있는 신석기시대 유적지에서 출토되는데 대표적인 사례로 서울 암사동유적, 김천 송죽리유적, 양양 오산리유적, 부산 동삼동유적이 있다. 신석기시대의 대표적인 빗살무늬토기는 아랫부분이 둥글거나 뾰족한 형태를 이루는데 당시에는 어떻게 고정시키고 사용하였을까. 이러한 토기를 고정시키기 위해서 토기 바닥 부분을 모래나 흙 속에 일부 묻고 사용하거나 여러 개의 돌을 이용하여 토기를 고정시켰을 것으로 추정된다."},
    {"name": "빗살무늬토기 단지", "desc": ""},
    {"name": "토기 감상법", "desc": ""},
    {"name": "빗살무늬토기 바리", "desc": ""},
    {"name": "병형토기", "desc": ""},
    {"name": "주머니모양 구멍뚫린 토기", "desc": ""},
    ]

FLOOR2_CASE3_DESCRIPTIONS = [
    {"name": "빗살무늬토기 깊은 바리", "desc": "김천 송죽리유적에서 출토된 신석기시대 후기의 빗살무늬토기 깊은 바리이다. 전체적인 기형은 바닥부분이 둥근 포탄형이며 토기의 몸체 중에서 가장 넓은 부위가 윗부분에 위치하고 있다. 신석기시대 후기에는 토기의 전면에 걸쳐 다양한 문양이 새겨지다가 신석기시대 후기로 오면서 기형이 다소 작아지고 문양도 점점 줄어드는 양상을 보인다. 입술부분에만 한정되어 문양이 새겨져 있어 신석기시대 후기 토기의 모습을 잘 보여주고 있다. 문양은 두 줄의 물결무늬를 자연스럽고 경쾌하게 표현하였는데 신석기시대 후기 김천 송죽리에 살았던 사람들의 예술적 감각을 엿볼 수 있다."},
    {"name": "토기를 이용한 먹거리", "desc": "신석기시대에 등장한 토기는 불을 이용한 조리를 가능하게 하여 음식을 삶거나 쪄서 먹는 새로운 조리법을 가능하게 하였다. 이전에는 날로 먹을 때 질기거나 일부 독성이 있는 먹거리를 끓은 물에서는 연해지거나 중화되어 먹을 수 있게 되었다. 유적에서 확인되는 탄화 유물들을 통해 보면, 곡물의 조리는 주로 가루를 내어 죽을 끓여 먹었던 것으로 판단된다. 이러한 불과 토기를 이용한 조리법의 개발로 인해 먹거리의 영역이 넓어지고 삶은 먹거리를 섭취함으로써 질병예방을 가져와 수명도 연장되는 등 여러 혜택을 누리게 되었다. 나아가 안정된 먹거리의 확보는 정주마을을 이루는 기틀을 마련하게 되었다."},
    {"name": "토기 바닥에서 확인된 나뭇잎", "desc": ""},
    ]

FLOOR2_CASE4_DESCRIPTIONS = [
    {"name": "민무늬토기 항아리·단지","desc": ""},
    {"name": "민무늬토기 단지", "desc": "김천 송죽리 유적의 제6호 주거지에서 출토된 문양이 없는 작은 단지 형태의 무문토기이다. 바닥은 평평하고 동체부는 약간 볼록한 타원형을 하고 있으며 구연부는 짧게 외반하고 있다. 6호 주거지는 화재에 의해 폐기된 주거지로 바닥전면에 걸쳐 다양한 토기와 마제석기, 지석 등 석기제작과 관련된 유물들이 많이 출토되었다. 이러한 양상으로 보아 공공작업장이나 대가족 단위의 주거로 추정되며 출토 단지는 실생활에 사용하던 토기로 추정된다."},
    {"name": "돌대문토기편", "desc": "김천 송죽리 제7호 주거지 출토 돌대문토기 도안과 함께 한반도 남부 돌대문토기 출토유적 지도가 포함되어 있습니다. 손으로 눌러 띠를 만든 흔적(손으로 누른 흔적)이 있는 토기 조각 유물입니다."},
    {"name": "청동기시대 토기", "desc": ""},
    {"name": "민무늬토기 바리·깊은바리", "desc": ""},
    {"name": "붉은간토기 항아리", "desc": ""},
    {"name": "붉은간토기 바리", "desc": ""},
    {"name": "붉은 간토기", "desc": "김천 송죽리유적의 청동기시대 18호 지석묘에서 출토된 붉은 간토기이다. 붉은 간토기는 토기의 표면에 산화철을 바르고 반들거리게 문질러서 구운 토기이다. 주로 청동기시대의 고인돌·돌널무덤 등에서 주로 발견되며, 고운 흙으로 만들어졌고 기형은 둥근 바닥의 긴목단지 형태이다. 붉은 간토기는 종래 고인돌에서 발견되는 점과 토기의 질 등을 통해 생활용이 아닌 특수 토기라고 생각했으나 최근 집자리에서도 발견되고 있어 일부 실생활에서도 사용된 것으로 보인다."},
    {"name": "그물추", "desc": ""},
    {"name": "자귀·홈자귀", "desc": ""},
    {"name": "가락바퀴", "desc": ""},
    {"name": "반달돌칼 제작과정", "desc": ""},
    {"name": "돌화살촉", "desc": ""},
    {"name": "반월형석도 및 방추자 사용법 모식도", "desc": ""}
    ]

FLOOR2_CASE5_DESCRIPTIONS = [
    {"name": "세형동검·투겁창", "desc": ""},
    {"name": "바퀴날 도끼", "desc": ""},
    {"name": "홈자귀 제작과정", "desc": ""},
    {"name": "쇠뿔모양석기", "desc": ""},
    {"name": "둥근옥", "desc": ""},
    {"name": "가락바퀴", "desc": ""},
    {"name": "대구 연암산유적", "desc": "대구광역시 산격동에 위치하고 있는 철기시대 유물산포지로 금호강과 신천이 합류하는 동쪽의 낮은 구릉에 위치하고 있다. 1962년에 처음 발견되었고 여러 번 지표조사를 통해 다량의 석기와 토기편이 발견되었다. 석기로는 돌검(石劍), 화살촉(石鏃), 돌칼(石刀), 대팻날, 끌(石鑿), 도끼(石斧), 자귀(手斧), 숫돌(砥石), 칼자루끝장식(劍把頭飾)이 채집되었는데, 특히 홈자귀(有溝石斧)는 완성품과 함께 미완성품 조각을 합치면 수백 개가 넘는 많은 양이 발견되었다. 이를 통해 이곳이 홈자귀를 전문적으로 제조한 곳으로 추정되고 있다. 토기는 적갈색무문토기, 붉은간토기(紅陶), 검은간토기(黑陶) 등이 발견되었다. 무문토기는 가장 많은 양을 차지하며 굽다리접시(豆形土器), 점토띠토기(粘土帶土器), 쇠뿔잡이항아리(牛角形把手附壺), 시루 등이 있다."},
    {"name": "돌도끼", "desc": ""},
    {"name": "돌화살촉과 석기재료", "desc": ""},
    {"name": "돌도끼 제작과정", "desc": ""},
    {"name": "돌끌", "desc": ""},
    {"name": "반달돌칼", "desc": ""},
    {"name": "돌칼", "desc": ""},
    {"name": "숫돌", "desc": ""},
    {"name": "돌망치", "desc": ""},
    {"name": "바퀴날 도끼", "desc": ""},
    {"name": "두귀달린토기 바리", "desc": ""},
    {"name": "초기철기시대 묘제", "desc": "초기철기시대의 대표 묘제로 적석목관묘와 목관묘를 들 수 있다. 적석목관묘는 대전 괴정동, 아산 남성리, 예산 동서리, 부여 연화리, 화순 대곡리, 함평 초포리 유적이 대표적이다. 구조는 토광을 깊이 파고 매장주체부를 석관 혹은 목관으로 조영하며, 옥관과 묘광 사이에 할석을 채운다. 묘광 상부에 목개의 존재 가능성이 높으며 그 위에 다시 적석이 이루어진 것으로 보고 있다. 대구 팔달동유적에서는 16기의 적석목관묘가 확인되었다."},
    {"name": "쇠뿔손잡이 항아리", "desc": ""},
    {"name": "민무늬토기 바리", "desc": ""},
    {"name": "쇠투겁창", "desc": ""},
    ]


def resize_map_to_fit(source_path, output_path):
    img = PILImage.open(source_path).convert("RGBA")
    ratio = min(MAX_MAP_W / img.width, MAX_MAP_H / img.height)

    new_w = max(1, int(img.width * ratio))
    new_h = max(1, int(img.height * ratio))

    resized = img.resize((new_w, new_h), PILImage.Resampling.LANCZOS)
    resized.save(output_path)

    return resized, new_w, new_h


def resize_popup_image(source_path, output_path, width=760):
    img = PILImage.open(source_path).convert("RGBA")
    ratio = width / img.width

    new_w = width
    new_h = int(img.height * ratio)

    if new_h > 400:
        ratio = 400 / img.height
        new_w = int(img.width * ratio)
        new_h = 400

    resized = img.resize((new_w, new_h), PILImage.Resampling.LANCZOS)
    resized.save(output_path)

    return new_w, new_h


def wrap_text(text, limit=48):
    lines = []
    current = ""

    for word in text.split():
        if len(current) + len(word) + 1 > limit:
            lines.append(current)
            current = word
        else:
            if current:
                current += " "
            current += word

    if current:
        lines.append(current)

    return "\n".join(lines)


def is_stair_pixel(img, x, y):
    if x < 0 or y < 0 or x >= img.width or y >= img.height:
        return False

    r, g, b, a = img.getpixel((x, y))

    if a < 10:
        return False

    brightness = 0.299 * r + 0.587 * g + 0.114 * b
    color_diff = max(abs(r - g), abs(g - b), abs(r - b))

    return brightness > 70 and brightness < 230 and color_diff < 18


def is_wall_pixel(img, x, y, floor_index):
    if x < 0 or y < 0 or x >= img.width or y >= img.height:
        return True

    r, g, b, a = img.getpixel((x, y))

    if a < 10:
        return True

    if is_stair_pixel(img, x, y):
        return True

    return r < 40 and g < 40 and b < 40


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    win = GraphWin("층별 지도 보기", WINDOW_W, WINDOW_H)
    win.setCoords(0, 0, WINDOW_W, WINDOW_H)

    guide = Text(
        Point(WINDOW_W / 2, WINDOW_H - 20),
        "1=1층   2=2층   방향키/WASD=이동   E=상호작용   설명 넘기기=←/→   ESC=닫기   q=종료"
    )
    guide.setSize(14)
    guide.draw(win)

    player_x = WINDOW_W / 2
    player_y = WINDOW_H / 2

    player = Circle(Point(player_x, player_y), 10)
    player.setFill("red")
    player.setOutline("white")
    player.setWidth(2)
    player.draw(win)

    current_floor = 1
    current_image = None
    map_img = None
    pressed_keys = set()

    interaction_text = None
    popup_objects = []
    relic_desc_objects = []
    display_case_objects = []

    popup_open = False
    player_visible = True

    current_relic_index = 0
    current_descriptions = CHAPTER1_DESCRIPTIONS

    def draw_player():
        nonlocal player, player_visible

        if popup_open:
            return

        if player_visible:
            player.undraw()

        player = Circle(Point(player_x, player_y), 10)
        player.setFill("red")
        player.setOutline("white")
        player.setWidth(2)
        player.draw(win)
        player_visible = True

    def hide_player():
        nonlocal player_visible

        if player_visible:
            player.undraw()
            player_visible = False

    def draw_display_case(x, y, label_text, vertical=False):
        objects = []

        if vertical:
            # 세로형 얇은 유리 전시장
            case_bottom = y - 55
            case_top = y + 55

            case = Rectangle(Point(x - 12, case_bottom), Point(x + 12, case_top))
            case.setFill("#c9f2ff")
            case.setOutline("#2f6f85")
            case.setWidth(2)
            case.draw(win)
            objects.append(case)

            # 세로형 받침대: 유리 아래에 딱 붙임
            stand = Rectangle(Point(x - 16, y - 70), Point(x + 16, case_bottom))
            stand.setFill("#dddddd")
            stand.setOutline("#555555")
            stand.setWidth(2)
            stand.draw(win)
            objects.append(stand)

            # 유리 반사선
            shine = Line(Point(x - 6, y + 38), Point(x + 6, y - 38))
            shine.setFill("white")
            shine.setWidth(2)
            shine.draw(win)
            objects.append(shine)


        else:
            # 가로형 얇은 유리 전시장
            case_bottom = y - 16
            case_top = y + 16

            case = Rectangle(Point(x - 48, case_bottom), Point(x + 48, case_top))
            case.setFill("#c9f2ff")
            case.setOutline("#2f6f85")
            case.setWidth(2)
            case.draw(win)
            objects.append(case)

            # 가로형 받침대: 유리 아래에 딱 붙임
            stand = Rectangle(Point(x - 50, y - 30), Point(x + 50, case_bottom))
            stand.setFill("#dddddd")
            stand.setOutline("#555555")
            stand.setWidth(2)
            stand.draw(win)
            objects.append(stand)

            # 유리 반사선
            shine = Line(Point(x - 30, y + 10), Point(x - 12, y - 10))
            shine.setFill("white")
            shine.setWidth(2)
            shine.draw(win)
            objects.append(shine)

        return objects

    def near_point(x, y):
        distance = ((player_x - x) ** 2 + (player_y - y) ** 2) ** 0.5
        return distance <= INTERACT_DISTANCE

    def near_chapter1():
        return current_floor == 1 and near_point(CHAPTER1_X, CHAPTER1_Y)

    def near_chapter2():
        return current_floor == 1 and near_point(CHAPTER2_X, CHAPTER2_Y)

    def near_chapter3():
        return current_floor == 1 and near_point(CHAPTER3_X, CHAPTER3_Y)

    def near_chapter4():
        return current_floor == 1 and near_point(CHAPTER4_X, CHAPTER4_Y)

    def near_chapter5():
        return current_floor == 1 and near_point(CHAPTER5_X, CHAPTER5_Y)

    def get_near_floor2_case():
        if current_floor != 2:
            return None

        for index, (x, y, _, _) in enumerate(FLOOR2_DISPLAY_CASES):
            if near_point(x, y):
                return index

        return None

    def update_interaction_text():
        nonlocal interaction_text

        if interaction_text is not None:
            interaction_text.undraw()
            interaction_text = None

        if popup_open:
            return

        if near_chapter1():
            interaction_text = Text(Point(WINDOW_W / 2, 60), "E키를 눌러 챕터 1 유물 설명 보기")
            interaction_text.setSize(15)
            interaction_text.draw(win)

        elif near_chapter2():
            interaction_text = Text(Point(WINDOW_W / 2, 60), "E키를 눌러 챕터 2 유물 설명 보기")
            interaction_text.setSize(15)
            interaction_text.draw(win)

        elif near_chapter3():
            interaction_text = Text(Point(WINDOW_W / 2, 60), "E키를 눌러 챕터 3 유물 설명 보기")
            interaction_text.setSize(15)
            interaction_text.draw(win)

        elif near_chapter4():
            interaction_text = Text(Point(WINDOW_W / 2, 60), "E키를 눌러 챕터 4 유물 설명 보기")
            interaction_text.setSize(15)
            interaction_text.draw(win)

        elif near_chapter5():
            interaction_text = Text(Point(WINDOW_W / 2, 60), "E키를 눌러 챕터 5 유물 설명 보기")
            interaction_text.setSize(15)
            interaction_text.draw(win)

        else:
            floor2_case_index = get_near_floor2_case()
            if floor2_case_index is not None:
                label = FLOOR2_DISPLAY_CASES[floor2_case_index][2]
                interaction_text = Text(Point(WINDOW_W / 2, 60), f"E키를 눌러 {label} 유물 설명 보기")
                interaction_text.setSize(15)
                interaction_text.draw(win)

    def show_relic_desc(index):
        nonlocal relic_desc_objects, current_relic_index

        current_relic_index = index % len(current_descriptions)
        relic = current_descriptions[current_relic_index]

        for obj in relic_desc_objects:
            obj.undraw()
        relic_desc_objects = []

        box = Rectangle(Point(150, 60), Point(950, 320))
        box.setFill("#fff8dc")
        box.setOutline("black")
        box.setWidth(2)
        box.draw(win)

        title = Text(Point(550, 290), relic["name"])
        title.setSize(14)
        title.setStyle("bold")
        title.draw(win)

        desc_text = Text(Point(550, 190), wrap_text(relic["desc"], 56))
        desc_text.setSize(10)
        desc_text.draw(win)

        arrow_text = Text(
            Point(550, 95),
            f"← / → 설명 넘기기    {current_relic_index + 1} / {len(current_descriptions)}"
        )
        arrow_text.setSize(12)
        arrow_text.setTextColor("gray")
        arrow_text.draw(win)


        relic_desc_objects = [box, title, desc_text, arrow_text]

    def open_chapter_popup(image_file, title_text, descriptions):
        nonlocal popup_open, popup_objects, interaction_text
        nonlocal current_relic_index, current_descriptions

        if popup_open:
            return

        chapter_path = os.path.join(base_dir, image_file)

        if not os.path.exists(chapter_path):
            print(f"이미지 파일을 찾을 수 없습니다: {chapter_path}")
            return

        if interaction_text is not None:
            interaction_text.undraw()
            interaction_text = None

        popup_open = True
        hide_player()
    
        current_relic_index = 0
        current_descriptions = descriptions

        temp_popup_path = os.path.join(base_dir, "_tmp_chapter_popup.png")
        resize_popup_image(chapter_path, temp_popup_path, width=760)

        bg = Rectangle(Point(120, 45), Point(980, 730))
        bg.setFill("white")
        bg.setOutline("black")
        bg.setWidth(3)
        bg.draw(win)

        title = Text(Point(WINDOW_W / 2, 705), title_text)
        title.setSize(18)
        title.setStyle("bold")
        title.draw(win)

        popup_img = Image(Point(WINDOW_W / 2, 485), temp_popup_path)
        popup_img.draw(win)

        close_text = Text(Point(WINDOW_W / 2, 270), "← / → 방향키로 유물 설명 넘기기   E 또는 ESC=닫기")
        close_text.setSize(12)
        close_text.draw(win)

        popup_objects = [bg, title, popup_img, close_text]

        show_relic_desc(0)


    def close_popup():
        nonlocal popup_open, popup_objects, relic_desc_objects

        for obj in relic_desc_objects:
            obj.undraw()
        relic_desc_objects = []

        for obj in popup_objects:
            obj.undraw()
        popup_objects = []

        popup_open = False
        draw_player()

    def load_floor(index):
        nonlocal current_floor, current_image, map_img
        nonlocal player_x, player_y

        if popup_open:
            close_popup()

        current_floor = index + 1
        map_path = os.path.join(base_dir, FLOOR_FILES[index])

        if not os.path.exists(map_path):
            raise FileNotFoundError(f"지도 파일을 찾을 수 없습니다: {map_path}")

        if current_image is not None:
            current_image.undraw()

        for obj in display_case_objects:
            obj.undraw()
        display_case_objects.clear()

        temp_path = os.path.join(base_dir, f"_tmp_{index}.png")
        map_img, _, _ = resize_map_to_fit(map_path, temp_path)

        current_image = Image(Point(WINDOW_W / 2, WINDOW_H / 2), temp_path)
        current_image.draw(win)

        if current_floor == 1:
            display_case_objects.extend(draw_display_case(CHAPTER1_X, CHAPTER1_Y, "챕터 1", vertical=False))
            display_case_objects.extend(draw_display_case(CHAPTER2_X, CHAPTER2_Y, "챕터 2", vertical=True))
            display_case_objects.extend(draw_display_case(CHAPTER3_X, CHAPTER3_Y, "챕터 3", vertical=False))
            display_case_objects.extend(draw_display_case(CHAPTER4_X, CHAPTER4_Y, "챕터 4", vertical=False))
            display_case_objects.extend(draw_display_case(CHAPTER5_X, CHAPTER5_Y, "챕터 5", vertical=False))

        elif current_floor == 2:
            # 2층에는 1층과 같은 모양의 전시관만 배치합니다.
            # 유물 설명 팝업은 1층 챕터에만 작동합니다.
            for x, y, label, vertical in FLOOR2_DISPLAY_CASES:
                display_case_objects.extend(draw_display_case(x, y, label, vertical=vertical))

        player_x = WINDOW_W / 2
        player_y = WINDOW_H / 2

        draw_player()

    def on_key_press(event):
        pressed_keys.add(event.keysym.lower())

    def on_key_release(event):
        pressed_keys.discard(event.keysym.lower())

    win.bind_all("<KeyPress>", on_key_press)
    win.bind_all("<KeyRelease>", on_key_release)

    load_floor(0)

    while True:
        if "q" in pressed_keys:
            break

        if popup_open:
            if "e" in pressed_keys or "escape" in pressed_keys:
                pressed_keys.discard("e")
                pressed_keys.discard("escape")
                close_popup()

            if "right" in pressed_keys:
                pressed_keys.discard("right")
                next_index = (current_relic_index + 1) % len(current_descriptions)
                show_relic_desc(next_index)

            if "left" in pressed_keys:
                pressed_keys.discard("left")
                next_index = (current_relic_index - 1) % len(current_descriptions)
                show_relic_desc(next_index)

            time.sleep(0.05)
            win.update()
            continue

        if "e" in pressed_keys:
            pressed_keys.discard("e")

            if near_chapter1():
                open_chapter_popup(
                    CHAPTER1_IMAGE_FILE,
                    "챕터 1 : 매화, 눈 속에 피는 절개",
                    CHAPTER1_DESCRIPTIONS
                )

            elif near_chapter2():
                open_chapter_popup(
                    CHAPTER2_IMAGE_FILE,
                    "챕터 2 : 연꽃, 청정과 군자의 품격",
                    CHAPTER2_DESCRIPTIONS
                )

            elif near_chapter3():
                open_chapter_popup(
                    CHAPTER3_IMAGE_FILE,
                    "챕터 3 : 모란, 꽃 중의 왕",
                    CHAPTER3_DESCRIPTIONS
                )

            elif near_chapter4():
                open_chapter_popup(
                    CHAPTER4_IMAGE_FILE,
                    "챕터 4 : 국화, 고결함과 장수의 꽃",
                    CHAPTER4_DESCRIPTIONS
                )

            elif near_chapter5():
                open_chapter_popup(
                    CHAPTER5_IMAGE_FILE,
                    "챕터 5 : 소나무, 세월을 이겨낸 장수와 지조",
                    CHAPTER5_DESCRIPTIONS
                )
            else:
                floor2_case_index = get_near_floor2_case()
                if floor2_case_index is not None:
                    floor2_case_images = [
                        FLOOR2_CASE1_IMAGE_FILE,
                        FLOOR2_CASE2_IMAGE_FILE,
                        FLOOR2_CASE3_IMAGE_FILE,
                        FLOOR2_CASE4_IMAGE_FILE,
                        FLOOR2_CASE5_IMAGE_FILE,
                        FLOOR2_CASE6_IMAGE_FILE,
                    ]
                    floor2_case_titles = [
                        "2층 전시관 1 : 전석길 교수 기증 화폐와 도자기",
                        "2층 전시관 2 : 구석기시대 도구와 생활",
                        "2층 전시관 3 : 신석기시대 토기와 먹거리",
                        "2층 전시관 4 : 청동기시대 토기와 석기",
                        "2층 전시관 5 : 철기시대 유물과 생활",
                        "2층 전시관 6 : 빗살무늬토기와 신석기 문화",
                    ]
                    floor2_case_descriptions = [
                        FLOOR2_CASE1_DESCRIPTIONS,
                        FLOOR2_CASE2_DESCRIPTIONS,
                        FLOOR2_CASE3_DESCRIPTIONS,
                        FLOOR2_CASE4_DESCRIPTIONS,
                        FLOOR2_CASE5_DESCRIPTIONS,
                        FLOOR2_CASE6_DESCRIPTIONS,
                    ]
                    open_chapter_popup(
                        floor2_case_images[floor2_case_index],
                        floor2_case_titles[floor2_case_index],
                        floor2_case_descriptions[floor2_case_index],
                    )

        if "1" in pressed_keys:
            pressed_keys.discard("1")
            load_floor(0)

        if "2" in pressed_keys:
            pressed_keys.discard("2")
            load_floor(1)

        next_x = player_x
        next_y = player_y

        if "w" in pressed_keys or "up" in pressed_keys:
            next_y += 10
        if "s" in pressed_keys or "down" in pressed_keys:
            next_y -= 10
        if "a" in pressed_keys or "left" in pressed_keys:
            next_x -= 10
        if "d" in pressed_keys or "right" in pressed_keys:
            next_x += 10

        next_x = max(10, min(WINDOW_W - 10, next_x))
        next_y = max(10, min(WINDOW_H - 10, next_y))

        if map_img is not None:
            left = WINDOW_W / 2 - map_img.width / 2
            bottom = WINDOW_H / 2 - map_img.height / 2

            sample_points = [
                (next_x, next_y),
                (next_x + 8, next_y),
                (next_x - 8, next_y),
                (next_x, next_y + 8),
                (next_x, next_y - 8),
            ]

            blocked = False

            for sx, sy in sample_points:
                pix_x = int(sx - left)
                pix_y = int(map_img.height - 1 - (sy - bottom))

                if 0 <= pix_x < map_img.width and 0 <= pix_y < map_img.height:
                    if is_wall_pixel(map_img, pix_x, pix_y, current_floor - 1):
                        blocked = True
                        break
                else:
                    blocked = True
                    break

            if not blocked:
                player_x = next_x
                player_y = next_y

        draw_player()
        update_interaction_text()

        time.sleep(0.05)
        win.update()

    win.close()


if __name__ == "__main__":
    main()