import streamlit as st
from streamlit_airtable import AirtableConnection

st.markdown("#  Data Catalog 🎈")
st.sidebar.markdown("# Data Catalog 🎈")


# Create connection
conn = st.connection("resilient_air_table", type=AirtableConnection)
baseid=st.secrets.connections.resilient_air_table["base_id"]
tableid=st.secrets.connections.resilient_air_table["table_id"]

# # Retrieve base schema
# base_schema = conn.get_base_schema()
# with st.expander("Base schema"):
#     st.json(base_schema)
# # Get the first table's ID
# first_table = base_schema["tables"][0]
# st.markdown(f"## First table ID: `{first_table['id']}` (named `{first_table['name']}`)")

st.markdown(f"## First 25 records of Data Catalog:")

# Retrieve all records for the first table (pyAirtable paginates automatically)
# (Note you can also pass in parameters supported by pyAirtable
# (https://pyairtable.readthedocs.io/en/stable/api.html#parameters) such as as
# max_records, view, sort, and formula into conn.query() like so:
# table_records = conn.query(first_table["id"], max_records=25, view='viwXXX')
table_records = conn.query(table_id=tableid, max_records=25)
st.markdown(f"{len(table_records)} records retrieved")
st.dataframe(table_records)
