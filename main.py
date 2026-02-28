import streamlit as st

st.set_page_config(page_title="E-Modul Interaktif", layout="wide", initial_sidebar_state="expanded")



# =========================
# PAGE OBJECT (PATH AKURAT)
# =========================

cover = st.Page(
    "pages/cover.py",
    title="Home",
    icon=":material/home:"
)


# --- Bab 1
b1_1 = st.Page(
    "pages/bab_1/b1_1.py",
    title="Latihan 1 - Fundamental of Management"
)

b1_2 = st.Page(
    "pages/bab_1/b1_2.py",
    title="Latihan 2 - Leadership"
)

b2_1 = st.Page(
    "pages/bab_2/b2_1.py",
    title="Latihan 1"
)

b2_2 = st.Page(
    "pages/bab_2/b2_2.py",
    title="Latihan 2"
)

# =========================
# NAVIGATION (HIDDEN)
# =========================

contents = {
    "": [cover],
    "_materi": [b1_1, b1_2, b2_1, b2_2]
}

pg = st.navigation(contents, position="hidden")

# =========================
# SIDEBAR CUSTOM
# =========================

with st.sidebar:
    st.page_link(cover, label="Home", icon=":material/home:")

    st.divider()
    st.markdown("### Table of Contents")

    with st.container(border=False):
        with st.expander("Management", expanded=True):
            st.page_link(b1_1)
            st.page_link(b1_2)

        with st.expander("Marketing"):
            st.page_link(b2_1)
            st.page_link(b2_2)

# =========================
# RUN PAGE
# =========================

pg.run()


