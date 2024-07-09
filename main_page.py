import streamlit as st
from streamlit_auth import add_auth, get_logged_in_user, require_auth

add_auth(required=False, show_sidebar=True )

user_info= get_logged_in_user()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if user_info is not None:
    st.session_state.logged_in = True

def login():
    # if st.button("Log in"):
    #     st.session_state.logged_in = True
    #     st.rerun()
    require_auth()
    st.rerun()
# def logout():
#     if st.button("Log out"):
#         st.session_state.logged_in = False
#         st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
# logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

page_ili=st.Page("pathogens/Influenza_Like.py",  title="Influenza Like Illness", icon=":material/dashboard:")
page_mpox=st.Page("pathogens/MPOX_Example.py",  title="MPOX", icon=":material/dashboard:")


dashboards= [page_ili, page_mpox]
dashboard_page=st.Page("pages/dashboards.py",  title="Pathogens", icon=":material/dashboard:")

catalog_page=st.Page("other/RSDataCatalog.py", title="Catalog", icon=":material/dataset:")
ai_page=st.Page("other/z_generativeAI.py", title="AI", icon=":material/school:")
network_page=st.Page("pages/network.py", title="Network", icon=":material/school:")
if st.session_state.logged_in:
    pg = st.navigation({
            #"Account": [logout_page],
        "Resilent": [network_page],
            "Dashboards": dashboards,
        #"Dashboards_bad": [dashboard_page],
            "Tools": [catalog_page, ai_page],
        }
        #, position="hidden",
    )
else:
    pg = st.navigation([login_page])

pg.run()
