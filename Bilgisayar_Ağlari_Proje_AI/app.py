import streamlit as st
import pandas as pd
from pt_analysis.analyzer import get_analysis_results 

st.set_page_config(page_title="AI Network IDS", layout="wide")

st.title("Yapay Zeka Destekli Saldırı Tespit Sistemi")
st.markdown("Analiz motoru: `analyzer.py` | Model: `Random Forest`")

uploaded_file = st.file_uploader("Packet Tracer CSV Dosyasını Seçin", type=['csv'])

if uploaded_file is not None:
    with open("temp_pt_data.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner('Analiz motoru çalışıyor...'):
        result_df = get_analysis_results("temp_pt_data.csv")

    attacks = len(result_df[result_df['DURUM'] == "🚨 SALDIRI"])
    total = len(result_df)

    col1, col2 = st.columns(2)
    col1.metric("Toplam Paket", total)
    col2.metric("Tespit Edilen Saldırı", attacks, delta=attacks, delta_color="inverse")

    st.subheader("📋 Analiz Raporu")
    
    def color_status(val):
        color = '#ff4b4b' if val == "🚨 SALDIRI" else '#28a745'
        return f'background-color: {color}; color: white; font-weight: bold'

    st.dataframe(result_df.style.map(color_status, subset=['DURUM']), use_container_width=True)

else:
    st.info("Lütfen bir Cisco Packet Tracer CSV çıktısı yükleyin.")