import streamlit as st
import pandas as pd
import plotly.express as px
import states
from datetime import timedelta

@st.cache_data
def get_rsv_data(url):
    rsv_df = pd.read_csv(rsv)
    return rsv_df
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
st.markdown("# Infuenza-like Illnesses 🎈")
st.sidebar.markdown("# Infuenza-like Illnesses 🎈")

st.write("""
# ILI
Weekly Rates 
""")

rsv = "https://oss.resilientservice.mooo.com/resilientdata/cdc/resp_net/Rates_of_Laboratory-Confirmed_RSV__COVID-19__and_Flu_Hospitalizations_from_the_RESP-NET_Surveillance_Systems_20240506.csv"

#rsv_df = pd.read_csv(rsv)
rsv_df=get_rsv_data(rsv)
network=rsv_df['Surveillance Network'].unique().tolist()

selected_location = pills("Location", ["USA","California", "San Diego"], index=0, clearable=True)
st.write(selected_location)

selected_network = st.multiselect("Network", network, default="FluSurv-NET")


rsv_df["Week Ending Date"]=pd.to_datetime(rsv_df["Week Ending Date"], utc=True,  format="ISO8601")
rsv_df["Week Ending Date"]=rsv_df["Week Ending Date"].dt.date


rsv_df = rsv_df[(rsv_df["Surveillance Network"] != "Combined") &  (rsv_df["Site"] != "Overall") ]
rsv_df["State"] = rsv_df["Site"].apply(lambda x: states.us_state_to_abbrev[x])

rsv_gby = rsv_df.groupby(["Surveillance Network","Season","Site","Week Ending Date"], as_index=False).max()
rvs_df2=rsv_gby [["Surveillance Network","Season","Week Ending Date","Weekly Rate", "Cumulative Rate", "Site", "State"]]

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
week = st.slider('Select Week', first_year, last_year, key=date_col)
week_plus6 = week + timedelta(weeks = 9)
rsv_df_map = rvs_df2[(rvs_df2[date_col] >= week) & (rvs_df2[date_col] <= week_plus6) & (rvs_df2['Surveillance Network'].isin(selected_network))]

# max = rsv_df_map[col].max()
# min = rsv_df_map[col].min()

rsv_map = px.choropleth( rsv_df_map,
                        locations="State",
                        locationmode='USA-states' ,
                        scope="usa",
                        color=col,
                        hover_name="Surveillance Network",
                        range_color=(min,max),
                        title="resp_net"
                        )
#col1.plotly_chart(rsv_map)
st.plotly_chart(rsv_map)

st.write("""
# ILI
California 
""")
rsv_df2 = rsv_df[(rsv_df["Surveillance Network"] != "Combined") &  (rsv_df["Site"] == "California") ]
rsv_gby2 = rsv_df2.groupby(["Surveillance Network","Season","Site","Week Ending Date"], as_index=False).max()
rvs_df22=rsv_gby2 [["Surveillance Network","Season","Week Ending Date","Weekly Rate", "Cumulative Rate", "Site", "State"]]
selected_points=rvs_df22[(rvs_df22[date_col] >= week) & (rvs_df22[date_col] <= week_plus6)].index.tolist()
range_x=[5,100000]
range_y=[0,5]
rsv_fig = px.scatter(
    rvs_df22,
    x="Week Ending Date",
    y="Weekly Rate",
    color="Surveillance Network",
    size="Weekly Rate",
    hover_data=["Surveillance Network","Season","Weekly Rate"],
  #  animation_frame="Week Ending Date",
 #    animation_group="Surveillance Network",
 #   range_y=range_y
)

rsv_event = st.plotly_chart(rsv_fig, key="rsv", on_select="rerun")

#rsv_event.selection # renders the data
#col2.plotly_chart(rsv_fig)

