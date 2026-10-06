import streamlit as st
import html


def _esc(value):
    return html.escape(str(value))


def render_hero(profile, photo_path):
    left, right = st.columns([2.15, 1], gap="large")

    with left:
        links = f"""
        <div class="link-row">
            <a class="icon-link" href="mailto:{profile['email']}">
                <i class="fa-solid fa-envelope"></i> Email
            </a>
            <a class="icon-link" href="tel:0722561060">
                <i class="fa-solid fa-phone"></i> {profile['phone']}
            </a>
            <a class="icon-link" href="{profile['github']}" target="_blank">
                <i class="fa-brands fa-github"></i> GitHub
            </a>
            <a class="icon-link" href="{profile['linkedin']}" target="_blank">
                <i class="fa-brands fa-linkedin"></i> LinkedIn
            </a>
        </div>
        """

        st.markdown(
            f"""
            <div class="hero-card">
                <div class="eyebrow">Software Developer Portfolio</div>
                <div class="hero-name">{_esc(profile['name'])}</div>
                <div class="hero-role">{_esc(profile['role'])}</div>
                <p class="hero-summary">{_esc(profile['summary'])}</p>
                {links}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown('<div class="profile-image">', unsafe_allow_html=True)
        st.image(str(photo_path), width="stretch")
        st.markdown("</div>", unsafe_allow_html=True)


def render_section_title(title, subtitle):
    st.markdown(
        f"""
        <div class="section-title">
            <h2>{_esc(title)}</h2>
            <p>{_esc(subtitle)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_stats(stats):
    columns = st.columns(len(stats))
    for col, (label, value, icon) in zip(columns, stats):
        with col:
            st.markdown(
                f"""
                <div class="glass-card stat-card">
                    <div class="stat-icon"><i class="{icon}"></i></div>
                    <div class="stat-label">{_esc(label)}</div>
                    <div class="stat-value">{_esc(value)}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_skills(skills):
    columns = st.columns(3)
    icons = ["fa-solid fa-code", "fa-solid fa-layer-group", "fa-solid fa-database"]

    for col, ((category, items), icon) in zip(columns, zip(skills.items(), icons)):
        pills = "".join(
            f'<span class="skill-pill">{_esc(item)}</span>' for item in items
        )

        with col:
            st.markdown(
                f"""
                <div class="glass-card skill-card">
                    <div class="skill-heading">
                        <i class="{icon}"></i>
                        <span>{_esc(category)}</span>
                    </div>
                    {pills}
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_experience(experience):
    for item in experience:
        points = "".join(f"<li>{_esc(point)}</li>" for point in item["points"])

        st.markdown(
            f"""
            <div class="glass-card timeline-card">
                <h3><i class="{item['icon']}"></i> {_esc(item['role'])} @ {_esc(item['company'])}</h3>
                <div class="experience-meta">
                    <i class="fa-regular fa-calendar"></i> {_esc(item['period'])}
                    &nbsp;&nbsp;·&nbsp;&nbsp;
                    <i class="fa-solid fa-location-dot"></i> {_esc(item['location'])}
                </div>
                <ul class="experience-list">{points}</ul>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_projects(projects):
    columns = st.columns(2, gap="large")

    for index, project in enumerate(projects):
        with columns[index % 2]:
            tags = "".join(
                f'<span class="skill-pill">{_esc(tag)}</span>' for tag in project["tags"]
            )

            st.markdown(
                f"""
                <div class="glass-card project-card">
                    <img class="project-image" src="{_esc(project['image'])}" alt="{_esc(project['title'])}">
                    <div class="project-body">
                        <h3>{_esc(project['title'])}</h3>
                        <div class="project-role">{_esc(project['role'])}</div>
                        <div class="project-description">{_esc(project['description'])}</div>
                        <div style="margin-top: .9rem;">{tags}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_education(education, cv_text):
    columns = st.columns(2)

    for col, item in zip(columns, education):
        with col:
            st.markdown(
                f"""
                <div class="glass-card education-card">
                    <div class="education-icon">
                        <i class="{item['icon']}"></i>
                    </div>
                    <div>
                        <h3 style="margin:0">{_esc(item['title'])}</h3>
                        <p style="color:#94a3b8;margin:.35rem 0 0">
                            {_esc(item['institution'])} · {_esc(item['year'])}
                        </p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.download_button(
        label="Download Full Resume",
        data=cv_text,
        file_name="Mohamed_Musharraf_CV.txt",
        mime="text/plain",
        width="content",
    )


def render_contact_form():
    with st.container(border=True):
        st.markdown(
            """
            <div class="eyebrow">Get In Touch</div>
            <h2 style="margin-bottom:.35rem">Let's build something together.</h2>
            <p style="color:var(--muted); margin-top:0">
                Have a project, idea, or opportunity? Send me a message.
            </p>
            """,
            unsafe_allow_html=True,
        )

        with st.form("contact_form", clear_on_submit=False):
            name = st.text_input("Your Name", placeholder="Enter your name")
            email = st.text_input("Your Email", placeholder="you@example.com")
            message = st.text_area(
                "Your Message",
                placeholder="Tell me a little about your project or idea.",
                height=130,
            )
            submitted = st.form_submit_button("Send Message", width="stretch")

            if submitted:
                if name.strip() and email.strip() and message.strip():
                    st.success(f"Thank you, {name}. Your message has been received.")
                else:
                    st.error("Please complete all fields before sending.")


def render_footer():
    st.markdown(
        """
        <div class="footer">
            © 2026 Mohamed Musharraf · Built with Python & Streamlit
        </div>
        """,
        unsafe_allow_html=True,
    )
