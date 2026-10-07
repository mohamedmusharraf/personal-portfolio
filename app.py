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

# ── Theme state ────────────────────────────────────────────────────────────────
if "light_mode" not in st.session_state:
    st.session_state.light_mode = False

# Hidden Streamlit checkbox — toggled by the JS button below
light_mode = st.checkbox(
    "light_mode",
    value=st.session_state.light_mode,
    key="light_mode",
    label_visibility="hidden",
)

# ── Load theme styles ──────────────────────────────────────────────────────────
load_styles(light_mode=light_mode)

# ── Floating theme toggle button (HTML/JS) ─────────────────────────────────────
# Hides the native checkbox and renders a gorgeous floating pill instead.
is_light = light_mode
icon      = "☀️" if is_light else "🌙"
label     = "Light" if is_light else "Dark"
btn_bg    = "linear-gradient(135deg,#fbbf24,#f59e0b)" if is_light else "linear-gradient(135deg,#6366f1,#a855f7)"
tip_color = "#78350f" if is_light else "#c4b5fd"

st.markdown(
    f"""
    <style>
    /* Hide the native checkbox Streamlit renders */
    div[data-testid="stCheckbox"] {{
        position: fixed !important;
        top: -9999px !important;
        left: -9999px !important;
        opacity: 0 !important;
        pointer-events: none !important;
    }}

    /* ── Floating toggle pill ────────────────────────────────────────────── */
    #theme-btn {{
        position: fixed;
        top: 18px;
        right: 22px;
        z-index: 9999;

        display: flex;
        align-items: center;
        gap: 0.45rem;

        padding: 0.55rem 1.1rem 0.55rem 0.8rem;
        border-radius: 999px;
        border: none;
        cursor: pointer;

        background: {btn_bg};
        box-shadow: 0 4px 20px rgba(0,0,0,0.28), 0 0 0 1px rgba(255,255,255,0.12);

        font-family: 'Inter', sans-serif;
        font-size: 0.88rem;
        font-weight: 700;
        color: #fff;
        letter-spacing: 0.03em;

        transition: transform 0.25s cubic-bezier(0.34,1.56,0.64,1),
                    box-shadow 0.25s ease;

        user-select: none;
        -webkit-user-select: none;
    }}

    #theme-btn:hover {{
        transform: translateY(-3px) scale(1.06);
        box-shadow: 0 10px 30px rgba(0,0,0,0.30), 0 0 0 1px rgba(255,255,255,0.18);
    }}

    #theme-btn:active {{
        transform: scale(0.97);
    }}

    .theme-icon {{
        font-size: 1.1rem;
        line-height: 1;
        transition: transform 0.4s ease;
    }}

    #theme-btn:hover .theme-icon {{
        transform: rotate(20deg) scale(1.15);
    }}

    /* Tooltip */
    #theme-btn::after {{
        content: "Switch to {'dark' if is_light else 'light'} mode";
        position: absolute;
        top: calc(100% + 8px);
        right: 0;
        background: rgba(15,20,40,0.85);
        color: {tip_color};
        font-size: 0.72rem;
        font-weight: 600;
        padding: 0.3rem 0.6rem;
        border-radius: 8px;
        white-space: nowrap;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.2s ease;
        backdrop-filter: blur(8px);
    }}

    #theme-btn:hover::after {{
        opacity: 1;
    }}
    </style>

    <button id="theme-btn" onclick="toggleTheme()" title="Switch theme">
        <span class="theme-icon">{icon}</span>
        <span>{label} mode</span>
    </button>

    <script>
    function toggleTheme() {{
        // Find the hidden Streamlit checkbox input and click it
        const inputs = window.parent.document.querySelectorAll('input[type="checkbox"]');
        for (const inp of inputs) {{
            inp.click();
            break;
        }}
    }}
    </script>
    """,
    unsafe_allow_html=True,
)

# ── Page sections ──────────────────────────────────────────────────────────────
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
