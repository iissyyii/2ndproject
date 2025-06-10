import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

st.set_page_config(page_title="베트남 남부 관광 가이드", layout="wide")

st.title("🇻🇳 베트남 남부 관광지 가이드")
st.markdown("아래에서 베트남 남부의 아름다운 관광지를 소개하고, 지도에서 위치도 확인해보세요!")

# 관광지 데이터
places = {
    "호치민 시티": {
        "lat": 10.7769,
        "lon": 106.7009,
        "description": "베트남 최대 도시로 쇼핑, 역사, 음식 문화가 발달한 곳입니다. 벤탄 시장, 전쟁 박물관, 노틀담 대성당 등이 유명합니다.",
        "image": "https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcRx4xRc2D5_z6cGu3cFbFN_Nhd76ulKhEt1r8kmZc9YkcR_QKthMhm8t60SVE6j3njfROAOSSjFVco6HM-XDNW0q00xIi9pIzdTuLDkEg"
    },
    "무이네 (Mui Ne)": {
        "lat": 10.9333,
        "lon": 108.2500,
        "description": "무이네는 베트남의 유명한 해변 휴양지로, 사막(화이트 샌듄), 카이트서핑, 신선한 해산물로 유명합니다.",
        "image": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcSqOjvDIn3ZxkaHRLkm-KImoOCoKvK6UU_lRo-fTa6lfT27kQuK44WhYL3ZdOxdHZAYmSXGNd5NLEcjouKiX9uT6mTWnOcxFOJwjZ_HNw"
    },
    "껀터 (Can Tho)": {
        "lat": 10.0333,
        "lon": 105.7833,
        "description": "메콩 델타의 중심지로, 플로팅 마켓과 강 문화로 유명합니다. 깔락 플로팅 마켓을 꼭 방문해보세요.",
        "image": "https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcSapRppMy7RJzopVhMRL43hkV9JzDGZTXUlChB_2DZUaSJAWy6MF4PakWaimgg50eKTFYWLj_ACUVlMmHWWoKDLMVcWOAiD-LoXEJbfUg"
    },
    "붕따우 (Vung Tau)": {
        "lat": 10.3450,
        "lon": 107.0843,
        "description": "호치민에서 가까운 해변 도시로, 휴양지로 인기가 높습니다. 예수상과 해변 산책로가 인상적입니다.",
        "image": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcTWpgkTwVm50ew4RSHUvDeMLv14t86DfeD5veetxosJTsxQX8JbVRTeLJZkj4pDv_NawPS2HjTMwZhMQsBiXuKfJ97jIvq-97dP824zTtc"
    },
    "푸꾸옥 섬 (Phu Quoc)": {
        "lat": 10.2899,
        "lon": 103.9840,
        "description": "맑은 바다와 고급 리조트로 유명한 베트남 최대의 섬. 다이빙, 스노클링, 후옥 국립공원 등 자연 체험도 풍부합니다.",
        "image": "https://lh3.googleusercontent.com/gps-cs-s/AC9h4np0camunvBmjJ-GxqMqnBlXaErEG-0Gvly8RuqC1js8JwyxxR_VrdvL7E-BQgS_tc4BrfvWvjVoP6kAjWi-0KzXLFyQcDyiLdijRgU8oU2cIQCTRMidUIHP4SXkYuRpom2z8IMn=w675-h390-n-k-no"
    },
    "달랏 (Da Lat)": {
    "lat": 11.9404,
    "lon": 108.4583,
    "description": "베트남 고원에 위치한 아름다운 도시로, 시원한 기후와 꽃, 호수, 프랑스풍 건축으로 유명합니다. 사랑의 계곡, 달랏 기차역, 밤시장 등을 즐길 수 있어요.",
    "image": "https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcSgtN0ffSt8KIULEKF0B5EGPa-NU_bvVGNEGH363mH_bRex_Yo_2TXNDioCdGVg2MaVbn7Sx_DwXMCrf_aloLrdghLlGp4UCUCishBzXA"
}

}

# 장소별 관광 명소
sights = {
    "호치민 시티": [
        ["벤탄 시장", "전통 시장과 기념품 쇼핑의 명소", "1~2시간"],
        ["노틀담 대성당", "프랑스 식민지 양식의 대표 성당", "30분"],
        ["전쟁 박물관", "베트남 전쟁 관련 전시", "1시간"],
        ["사이공 스카이덱", "시내 전경을 볼 수 있는 전망대", "30분"]
    ],
    "달랏 (Da Lat)": [
        ["사랑의 계곡", "자연과 로맨틱한 풍경", "1~2시간"],
        ["달랏 기차역", "프랑스풍 역사 건물", "30분"],
        ["쭈옌람 사원", "고요한 호수와 함께하는 사찰", "45분"],
        ["달랏 야시장", "현지 음식과 쇼핑", "1~2시간"]
    ],
    "무이네 (Mui Ne)": [
        ["화이트 샌듄", "사막 같은 하얀 모래 언덕", "1시간"],
        ["레드 샌듄", "붉은빛 모래언덕에서 썰매 체험", "1시간"],
        ["요정의 개울", "붉은 흙과 계곡이 독특한 경관", "30분~1시간"],
        ["무이네 해변", "카이트서핑과 해수욕", "2~3시간"]
    ],
    "껀터 (Can Tho)": [
        ["깔락 플로팅 마켓", "배 위에서 열리는 전통 시장", "1~2시간 (이른 아침)"],
        ["빈뚜이 사원", "불교 사찰", "30분"],
        ["껀터 다리", "강을 잇는 랜드마크 대교", "20분"],
        ["껀터 야시장", "먹거리와 공연", "1~1.5시간"]
    ],
    "붕따우 (Vung Tau)": [
        ["예수상", "산 정상의 거대한 예수 동상", "1시간"],
        ["백사장 해변", "인기 있는 해변", "2시간 이상"],
        ["등대 전망대", "전망 좋은 포인트", "30~45분"],
        ["호 세네탄 사원", "불교 문화 유산", "30분"]
    ],
    "푸꾸옥 섬 (Phu Quoc)": [
        ["사오 해변", "하얀 모래와 에메랄드빛 바다", "2시간 이상"],
        ["푸꾸옥 야시장", "해산물과 기념품 쇼핑", "1~2시간"],
        ["딘까우 사원", "해안 절벽 위 사원", "30분"],
        ["빈펄 사파리", "동물원 및 수족관", "2~3시간"]
    ]
}








# 사이드바 관광지 선택
selected_place = st.sidebar.selectbox("📍 관광지를 선택하세요", list(places.keys()))

# 관광지 정보 출력
info = places[selected_place]
st.header(f"📌 {selected_place}")
st.image(info["image"], width=400)
st.write(info["description"])


st.subheader("📌 주요 명소 리스트")

st.subheader("📌 주요 명소 리스트")

if selected_place in sights:
    df = pd.DataFrame(sights[selected_place], columns=["명소", "설명", "소요시간"])
    st.table(df)
else:
    st.info("이 지역에 대한 관광 명소 정보가 아직 없습니다.")



# 지도 표시
m = folium.Map(location=[info["lat"], info["lon"]], zoom_start=10)

# 마커 추가
for name, data in places.items():
    folium.Marker(
        location=[data["lat"], data["lon"]],
        popup=f"<b>{name}</b><br>{data['description']}",
        tooltip=name,
        icon=folium.Icon(color="blue" if name == selected_place else "gray")
    ).add_to(m)

# 지도 출력
st.subheader("🗺 지도에서 위치 확인")
st_folium(m, width=900, height=500)
