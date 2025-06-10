import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 설정 (Windows 기준, Mac/Linux는 경로 다를 수 있음)
# 나눔고딕이 설치되어 있지 않다면 다른 폰트명으로 변경하거나 설치해야 합니다.
# fm.fontManager.addfont('NanumGothic.ttf') # 폰트 파일이 현재 디렉토리에 있을 경우
plt.rcParams['font.family'] = 'Malgun Gothic' # Windows 기본 폰트
plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

st.set_page_config(layout="wide")
st.title("대한민국 서해 vs 남해 월별 수온 비교 (2024.06 ~ 2025.06)")

st.sidebar.header("데이터 정보")
st.sidebar.markdown("""
이 앱은 가상의 서해 및 남해 월별 수온 데이터를 사용하여 비교 그래프를 생성합니다.
실제 데이터를 사용하려면 국립수산과학원 또는 기상청 API를 통해 데이터를 수집해야 합니다.
""")

# --- 데이터 로드 및 전처리 (실제 데이터는 API로 받아와야 함) ---
# 예시 데이터 생성 (실제 데이터로 대체해야 합니다)
months = pd.date_range(start='2024-06-01', periods=13, freq='MS') # 2024년 6월부터 2025년 6월까지 13개월
data = {
    '월': months.strftime('%Y-%m'),
    '서해_수온': [20, 22, 25, 27, 24, 20, 15, 10, 8, 12, 16, 18, 20], # 예시 수온
    '남해_수온': [21, 23, 26, 28, 25, 21, 16, 12, 10, 14, 17, 19, 21]  # 예시 수온
}
df = pd.DataFrame(data)
df['월'] = pd.to_datetime(df['월']) # '월' 컬럼을 datetime 객체로 변환

# --- 그래프 생성 ---
st.subheader("월별 평균 수온 변화")

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(df['월'], df['서해_수온'], marker='o', label='서해')
ax.plot(df['월'], df['남해_수온'], marker='o', label='남해')

ax.set_xlabel("월", fontsize=12)
ax.set_ylabel("수온 (°C)", fontsize=12)
ax.set_title("월별 서해 및 남해 평균 수온", fontsize=15)
ax.legend()
ax.grid(True)
plt.xticks(rotation=45) # x축 라벨 회전

st.pyplot(fig)

# --- 데이터 테이블 표시 ---
st.subheader("데이터 테이블")
st.dataframe(df)

# --- 추가 분석 (선택 사항) ---
st.subheader("수온 차이 분석")
df['수온_차이'] = df['남해_수온'] - df['서해_수온']
st.line_chart(df[['월', '수온_차이']].set_index('월'))
st.write("남해와 서해의 월별 수온 차이 (남해 - 서해):")
st.dataframe(df[['월', '수온_차이']])

st.markdown("---")
st.markdown("Made with ❤️ by Gemini AI")
