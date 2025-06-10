import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("대한민국 서해 vs 남해 월별 수온 비교 (2024.06 ~ 2025.06)")



# --- 데이터 로드 및 전처리 (실제 데이터는 API로 받아와야 함) ---
# 예시 데이터 생성 (실제 데이터로 대체해야 합니다)
# 현재 시간은 2025년 6월 10일이므로, 요청하신 기간의 데이터는 모두 과거 데이터입니다.
# 실제 데이터를 사용하시려면 해당 기간의 데이터를 API로 조회하여 사용하세요.
months = pd.date_range(start='2024-06-01', periods=13, freq='MS') # 2024년 6월부터 2025년 6월까지 13개월
data = {
    '월': months.strftime('%Y-%m'),
    '서해_수온': [20.1, 22.5, 25.3, 27.8, 24.1, 20.2, 15.0, 10.5, 8.2, 12.0, 16.5, 18.8, 20.0], # 예시 수온
    '남해_수온': [21.5, 23.9, 26.7, 28.9, 25.5, 21.6, 16.2, 12.8, 10.1, 14.3, 17.7, 19.9, 21.1]  # 예시 수온
}
df = pd.DataFrame(data)
df['월'] = pd.to_datetime(df['월']) # '월' 컬럼을 datetime 객체로 변환

# --- 메인 그래프: 월별 평균 수온 변화 ---
st.subheader("월별 평균 수온 변화")

fig1, ax1 = plt.subplots(figsize=(12, 6))

ax1.plot(df['월'], df['서해_수온'], marker='o', label='서해')
ax1.plot(df['월'], df['남해_수온'], marker='o', label='남해')

ax1.set_xlabel("월", fontsize=12)
ax1.set_ylabel("수온 (°C)", fontsize=12)
ax1.set_title("월별 서해 및 남해 평균 수온", fontsize=15)
ax1.legend()
ax1.grid(True)
plt.xticks(rotation=45) # x축 라벨 회전

st.pyplot(fig1)

# --- 전체 수온 데이터 테이블 (펼침/접힘) ---
with st.expander("전체 수온 데이터 테이블 보기"):
    st.subheader("데이터 테이블")
    st.dataframe(df)

# --- 수온 차이 계산 ---
df['수온_차이'] = df['남해_수온'] - df['서해_수온']

# --- 수온 차이 그래프 (고정 표시) ---
st.subheader("남해 vs 서해 월별 수온 차이")
fig2, ax2 = plt.subplots(figsize=(12, 4))
ax2.plot(df['월'], df['수온_차이'], marker='x', color='red', label='수온 차이 (남해 - 서해)')
ax2.set_xlabel("월", fontsize=12)
ax2.set_ylabel("수온 차이 (°C)", fontsize=12)
ax2.set_title("월별 남해-서해 수온 차이 변화", fontsize=15)
ax2.axhline(0, color='gray', linestyle='--', linewidth=0.8) # 0도 기준선 추가
ax2.legend()
ax2.grid(True)
plt.xticks(rotation=45)
st.pyplot(fig2)


# --- 수온 차이 데이터 테이블 (펼침/접힘) ---
with st.expander("남해 vs 서해 월별 수온 차이 데이터 보기"):
    st.subheader("수온 차이 데이터")
    st.write("남해와 서해의 월별 수온 차이 (남해 - 서해):")
    st.dataframe(df[['월', '수온_차이']])

st.markdown("---")
st.markdown("Made with ❤️ by Gemini AI")
