import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
    '서해_수온': [20.1, 22.5, 25.3, 27.8, 24.1, 20.2, 15.0, 10.5, 8.2, 12.0, 16.5, 18.8, 20.0], # 예시 수온
    '남해_수온': [21.5, 23.9, 26.7, 28.9, 25.5, 21.6, 16.2, 12.8, 10.1, 14.3, 17.7, 19.9, 21.1]  # 예시 수온
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
