import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

st.title("글로벌 시총 상위 10개 기업 주가 변화 (최근 3년)")

tickers = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Saudi Aramco': '2222.SR',
    'Alphabet': 'GOOGL',
    'Amazon': 'AMZN',
    'Nvidia': 'NVDA',
    'Berkshire Hathaway': 'BRK-B',
    'Tesla': 'TSLA',
    'Meta Platforms': 'META',
    'Taiwan Semiconductor': 'TSM'
}

start_date = pd.Timestamp.today() - pd.DateOffset(years=3)
end_date = pd.Timestamp.today()

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data['Close']

st.sidebar.header("기업 선택")
selected_companies = st.sidebar.multiselect("기업을 선택하세요", options=list(tickers.keys()), default=list(tickers.keys()))

if not selected_companies:
    st.warning("최소 한 개 이상의 기업을 선택해주세요.")
else:
    all_data = pd.DataFrame()
    for company in selected_companies:
        df = load_data(tickers[company])
        df.name = company
        all_data = pd.concat([all_data, df], axis=1)

    # Normalize 주가 (처음 값 기준 100%)
    normalized_data = all_data / all_data.iloc[0] * 100
    normalized_data.reset_index(inplace=True)

    # plotly용 데이터 프레임 변환 (long format)
    df_melt = normalized_data.melt(id_vars='Date', var_name='Company', value_name='Normalized Price')

    fig = px.line(df_melt, x='Date', y='Normalized Price', color='Company',
                  title='글로벌 시총 상위 10개 기업 주가 변화 (정규화, 최근 3년)',
                  labels={'Normalized Price': '주가 (시작일 대비 %)', 'Date': '날짜'})

    st.plotly_chart(fig, use_container_width=True)

    st.write("### 원본 종가 데이터 샘플")
    st.dataframe(all_data.tail())
