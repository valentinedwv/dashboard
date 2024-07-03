import streamlit as st

tab1, tab2 = st.tabs(["Influenza Like Illness", "MPOX"])
with tab1:
    #st.switch_page("pages/Influenza_Like.py")
    st.page_link( "pages/Influenza_Like.py",label="Influenza Like Illness",
                   help=None, disabled=False, use_container_width=False)
   # page_ili
with tab2:
   # page_mpox
  # st.switch_page("pages/MPOX_Example.py")
   st.page_link( "pages/MPOX_Example.py",label="MPOX",
                  help=None, disabled=False, use_container_width=False)
