import streamlit as st
import pandas as pd
import plotly.express as px


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


st.write("""
# ILI
Counts 
""")

rsv = "https://oss.resilientservice.mooo.com/resilientdata/cdc/resp_net/Rates_of_Laboratory-Confirmed_RSV__COVID-19__and_Flu_Hospitalizations_from_the_RESP-NET_Surveillance_Systems_20240506.csv"
rsv_df = pd.read_csv(rsv)
rsv_df = rsv_df[(rsv_df["Surveillance Network"] != "Combined") &  (rsv_df["Site"] == "California") ]

rsv_gby = rsv_df.groupby(["Surveillance Network","Season","Site","Week Ending Date"], as_index=False).max()
rvs_df2=rsv_gby [["Surveillance Network","Season","Week Ending Date","Weekly Rate", "Cumulative Rate"]]

rsv_fig = px.scatter(
    rvs_df2,
    x="Week Ending Date",
    y="Weekly Rate",
    color="Surveillance Network",
    size="Weekly Rate",
    hover_data=["Surveillance Network","Season"],
)

rsv_event = st.plotly_chart(rsv_fig, key="rsv", on_select="rerun")

rsv_event.selection



