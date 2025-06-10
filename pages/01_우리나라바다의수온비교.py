import streamlit as st
import pandas as pd
import plotly.express as px # Plotly Express 임포트

st.set_page_config(layout="wide")
st.title("대한민국 서해 vs 남해 월별 수온 비교 (2024.06 ~ 2025.06)")



# --- 데이터 로드 및 전처리 (실제 데이터는 API로 받아와야 함) ---
months = pd.date_range(start='2024-06-01', periods=13, freq='MS') # 2024년 6월부터 2025년 6월까지 13개월
data = {
    '월': months.strftime('%Y-%m'),
    '서해_수온': [20.1, 22.5, 25.3, 27.8, 24.1, 20.2, 15.0, 10.5, 8.2, 12.0, 16.5, 18.8, 20.0], # 예시 수온
    '남해_수온': [21.5, 23.9, 26.7, 28.9, 25.5, 21.6, 16.2, 12.8, 10.1, 14.3, 17.7, 19.9, 21.1]  # 예시 수온
}
df = pd.DataFrame(data)
df['월'] = pd.to_datetime(df['월']) # '월' 컬럼을 datetime 객체로 변환

# --- 메인 그래프: 월별 평균 수온 변화 (Plotly 사용) ---
st.subheader("월별 평균 수온 변화")

# Plotly Express를 사용하여 Line Chart 생성
# df를 long format으로 변환하여 Plotly Express에서 label을 쉽게 설정
df_melted = df.melt(id_vars=['월'], value_vars=['서해_수온', '남해_수온'], var_name='해역', value_name='수온')

fig1 = px.line(df_melted,
               x='월',
               y='수온',
               color='해역', # '해역' 컬럼에 따라 색상 구분
               markers=True,
               title='월별 서해 및 남해 평균 수온',
               labels={'월': '월', '수온': '수온 (°C)'}, # 축 라벨 설정
               height=450) # 그래프 높이 설정

# 그래프 레이아웃 업데이트 (옵션)
fig1.update_layout(hovermode="x unified") # 마우스 오버 시 x축 기준으로 정보 통합 표시
fig1.update_xaxes(dtick="M1", tickformat="%Y-%m") # 월별 간격으로 x축 눈금 설정

st.plotly_chart(fig1, use_container_width=True) # Streamlit에 Plotly 그래프 표시

# --- 전체 수온 데이터 테이블 (펼침/접힘) ---
with st.expander("전체 수온 데이터 테이블 보기"):
    st.subheader("데이터 테이블")
    st.dataframe(df)

# --- 수온 차이 계산 ---
df['수온_차이'] = df['남해_수온'] - df['서해_수온']

# --- 수온 차이 그래프 (Plotly 사용, 고정 표시) ---
st.subheader("남해 vs 서해 월별 수온 차이")

fig2 = px.line(df,
               x='월',
               y='수온_차이',
               markers=True,
               color_discrete_sequence=['red'], # 색상 빨간색으로 고정
               title='월별 남해-서해 수온 차이 변화',
               labels={'월': '월', '수온_차이': '수온 차이 (°C)'},
               height=350)

fig2.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="기준선 (0°C)", annotation_position="bottom right") # 0도 기준선 추가
fig2.update_layout(hovermode="x unified")
fig2.update_xaxes(dtick="M1", tickformat="%Y-%m")

st.plotly_chart(fig2, use_container_width=True) # Streamlit에 Plotly 그래프 표시

# --- 수온 차이 데이터 테이블 (펼침/접힘) ---
with st.expander("남해 vs 서해 월별 수온 차이 데이터 보기"):
    st.subheader("수온 차이 데이터")
    st.write("남해와 서해의 월별 수온 차이 (남해 - 서해):")
    st.dataframe(df[['월', '수온_차이']])

st.markdown("---")
st.markdown("Made with ❤️ by Gemini AI")
