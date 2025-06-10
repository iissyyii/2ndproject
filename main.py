import streamlit as st
import folium
from streamlit_folium import st_folium

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

# 사이드바 관광지 선택
selected_place = st.sidebar.selectbox("📍 관광지를 선택하세요", list(places.keys()))

# 관광지 정보 출력
info = places[selected_place]
st.header(f"📌 {selected_place}")
st.image(info["image"], width=400)
st.write(info["description"])

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
