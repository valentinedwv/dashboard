import streamlit as st
import pandas as pd
import plotly.express as px
st.markdown("#  MPOX Charting 🎈")
st.sidebar.markdown("# MPOX Charting 🎈")

st.write("""
# Resilient
Mpox Counts 
""")
mpox = "https://oss.resilientservice.mooo.com/resilientdata/cdc/output/ndss_Mpox_zip.csv"
df = pd.read_csv(mpox)
#df = df[df['Reporting Area'] == 'NEW YORK']
df_gby = df.groupby(['date','Reporting Area','geometry','lat','lon']).sum(["Cumulative YTD Current MMWR Year","Current week"]).reset_index()
#df = pd.read_csv("my_data.csv")
st.map(df)


st.scatter_chart(df, y=["Cumulative YTD Current MMWR Year","Current week"],
                 x="date", y_label="Reporting Area")

fig = px.scatter(
    df_gby,
    x="date",
    y=["Cumulative YTD Current MMWR Year","Current week"],
    color="Reporting Area",
    size="Current week",
    hover_data=["Reporting Area"],
)

event = st.plotly_chart(fig, key="mpox", on_select="rerun")

event.selection





