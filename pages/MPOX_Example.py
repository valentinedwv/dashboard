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


st.write("""
# ILI
Counts 
""")

rsv = "https://oss.resilientservice.mooo.com/resilientdata/cdc/resp_net/Rates_of_Laboratory-Confirmed_RSV__COVID-19__and_Flu_Hospitalizations_from_the_RESP-NET_Surveillance_Systems_20240506.csv"
rsv_df = pd.read_csv(rsv)
rsv_df["Week Ending Date"]=pd.to_datetime(rsv_df["Week Ending Date"], utc=True,  format="ISO8601")
rsv_df["Week Ending Date"]=rsv_df["Week Ending Date"].dt.date
rsv_df = rsv_df[(rsv_df["Surveillance Network"] != "Combined") &  (rsv_df["Site"] == "California") ]

rsv_gby = rsv_df.groupby(["Surveillance Network","Season","Site","Week Ending Date"], as_index=False).max()
rvs_df2=rsv_gby [["Surveillance Network","Season","Week Ending Date","Weekly Rate", "Cumulative Rate", "Site"]]

col1, col2 = st.columns(2)

col="Weekly Rate"
max = rvs_df2[col].max()
min = rvs_df2[col].min()
# rsv_map = px.choropleth(rvs_df2,
#                     locations="Site",
#                     color=col,
#                     hover_name="Surveillance Network",
#                     range_color=(min,max),
#                         title="resp_net"
#                     )
date_col='Week Ending Date'
first_year = rvs_df2[date_col].min()
last_year = rvs_df2[date_col].max()
year = st.slider('Select Week',first_year,last_year, key=date_col)

rsv_map = px.choropleth(rvs_df2[rvs_df2[date_col]==year],
                    locations="Site",
                 #   scope='US',
                    color=col,
                    hover_name="Surveillance Network",
                    range_color=(min,max),
                        title="resp_net"
                    )
#col1.plotly_chart(rsv_map)
st.plotly_chart(rsv_map)
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
#col2.plotly_chart(rsv_fig)


