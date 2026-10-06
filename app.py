import streamlit as st

from config import PAGE_TITLE, PAGE_ICON, PHOTO_PATH
from data.portfolio_data import (
    PROFILE, STATS, SKILLS, EXPERIENCE, PROJECTS, EDUCATION, CV_TEXT,
)
from components.styles import load_styles
from components.ui import (
    render_hero, render_section_title, render_stats, render_skills,
    render_experience, render_projects, render_education,
    render_contact_form, render_footer,
)

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)

if "light_mode" not in st.session_state:
    st.session_state.light_mode = False

# Theme control
_, theme_col = st.columns([8, 1])
with theme_col:
    st.toggle("Light mode", key="light_mode", help="Switch between dark and light themes")

# Load the selected theme. The toggle triggers Streamlit's rerun automatically.
load_styles()

render_hero(PROFILE, PHOTO_PATH)
render_section_title("Developer Profile", "A quick overview of my professional focus.")
render_stats(STATS)

render_section_title("Technical Skills", "Technologies and tools I work with.")
render_skills(SKILLS)

render_section_title("Professional Experience", "My current development experience.")
render_experience(EXPERIENCE)

render_section_title("Featured Projects", "Selected projects and technical work.")
render_projects(PROJECTS)

render_section_title("Education & Qualifications", "Academic and professional qualifications.")
render_education(EDUCATION, CV_TEXT)

render_contact_form()
render_footer()
