import html

import streamlit as st
from streamlit_auth import add_auth, get_logged_in_user, require_auth
from streamlit_elements import elements, mui, html, dashboard
import streamlit.components.v1 as components


#require_auth()
#st.rerun()

with elements("dashboard"):
    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        dashboard.Item("first_item", 0, 0, 2, 2),
        dashboard.Item("second_item", 2, 0, 2, 2, isDraggable=False, moved=False),
        dashboard.Item("third_item", 0, 2, 1, 1, isResizable=False),
    ]

    # with dashboard.Grid(layout):
    #     mui.Paper("First item", key="first_item")
    #     mui.Paper("Second item (cannot drag)", key="second_item")
    #     mui.Paper("Third item (cannot resize)", key="third_item")
    def handle_layout_change(updated_layout):
        # You can save the layout in a file, or do anything you want with it.
        # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
        print(updated_layout)


    mui.Toolbar()
    components.iframe("https://resilient.ucsd.edu")
    with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
        h = html.loadHtml("""<iframe src="https://www.w3schools.com" title="W3Schools Free Online Web Tutorials"></iframe>""")
        mui.Paper(h, key="first_item")

        mui.Paper("Second item (cannot drag)", key="second_item")
        mui.Paper("Third item (cannot resize)", key="third_item")

