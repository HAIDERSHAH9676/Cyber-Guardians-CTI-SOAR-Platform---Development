import streamlit as st

from app.core.config import settings

st.set_page_config(page_title=settings.app_name, page_icon="🛡️")
st.title(settings.app_name)
st.write("Threat intelligence and SOAR development dashboard.")
st.info(
    "Dashboard starter is ready. Threat data views will be added with the application features."
)
