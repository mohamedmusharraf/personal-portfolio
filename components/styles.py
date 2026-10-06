import streamlit as st


def load_styles(light_mode=False):
    if light_mode:
        theme = {
            "bg": "#f1f5f9",
            "surface": "rgba(255, 255, 255, 0.82)",
            "surface_strong": "rgba(255, 255, 255, 0.96)",
            "border": "rgba(15, 23, 42, 0.10)",
            "text": "#0f172a",
            "muted": "#64748b",
            "input_bg": "#ffffff",
            "input_text": "#0f172a",
            "input_border": "#cbd5e1",
        }
    else:
        theme = {
            "bg": "#070b16",
            "surface": "rgba(16, 24, 43, 0.72)",
            "surface_strong": "rgba(20, 30, 53, 0.92)",
            "border": "rgba(148, 163, 184, 0.16)",
            "text": "#f8fafc",
            "muted": "#94a3b8",
            "input_bg": "#111827",
            "input_text": "#f8fafc",
            "input_border": "#334155",
        }

    st.markdown(
        f"""
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

        <link
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap"
            rel="stylesheet"
        >

        <link
            rel="stylesheet"
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"
        >

        <style>

        :root {{
            --bg: {theme["bg"]};
            --surface: {theme["surface"]};
            --surface-strong: {theme["surface_strong"]};
            --border: {theme["border"]};
            --text: {theme["text"]};
            --muted: {theme["muted"]};

            --input-bg: {theme["input_bg"]};
            --input-text: {theme["input_text"]};
            --input-border: {theme["input_border"]};

            --cyan: #22d3ee;
            --blue: #60a5fa;
            --violet: #a78bfa;
            --pink: #f472b6;

            --radius: 22px;
        }}

        html {{
            scroll-behavior: smooth;
        }}

        *,
        *::before,
        *::after {{
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Inter', sans-serif;
        }}

        .stApp {{
            background:
                radial-gradient(
                    circle at 10% 10%,
                    rgba(34, 211, 238, 0.10),
                    transparent 28%
                ),
                radial-gradient(
                    circle at 90% 20%,
                    rgba(167, 139, 250, 0.10),
                    transparent 30%
                ),
                var(--bg);

            color: var(--text);
            overflow-x: hidden;
            transition:
                background 0.35s ease,
                color 0.35s ease;
        }}

        .block-container {{
            max-width: 1180px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }}

        /* --------------------------------
           GLOBAL TEXT
        -------------------------------- */

        h1, h2, h3, h4, p, label {{
            color: var(--text);
        }}

        .stCaption,
        [data-testid="stCaptionContainer"] {{
            color: var(--muted) !important;
        }}

        /* --------------------------------
           GLASS CARDS
        -------------------------------- */

        .glass-card,
        .hero-card {{
            position: relative;
            overflow: hidden;

            background: var(--surface);

            border: 1px solid var(--border);
            border-radius: var(--radius);

            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);

            box-shadow:
                0 20px 70px rgba(0, 0, 0, 0.12);

            transition:
                background 0.35s ease,
                border-color 0.35s ease,
                box-shadow 0.35s ease,
                transform 0.3s ease;
        }}

        /* --------------------------------
           HERO
        -------------------------------- */

        .hero-card {{
            padding: 2.5rem;
            animation: reveal 0.8s ease both;
        }}

        .hero-card::before {{
            content: "";

            position: absolute;

            width: 280px;
            height: 280px;

            right: -100px;
            top: -120px;

            background:
                linear-gradient(
                    135deg,
                    var(--cyan),
                    var(--violet),
                    var(--pink)
                );

            filter: blur(70px);
            opacity: 0.18;

            animation: floatGlow 7s ease-in-out infinite;
        }}

        .eyebrow {{
            color: var(--cyan);

            font-size: 0.78rem;
            font-weight: 800;

            letter-spacing: 0.16em;
            text-transform: uppercase;
        }}

        .hero-name {{
            font-family: 'Space Grotesk', sans-serif;

            font-size: clamp(2.7rem, 7vw, 5.4rem);
            line-height: 0.98;

            font-weight: 700;

            margin: 0.45rem 0 1rem;

            background:
                linear-gradient(
                    90deg,
                    var(--text),
                    var(--cyan),
                    var(--violet),
                    var(--pink)
                );

            background-size: 220% auto;

            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;

            animation: gradientText 7s linear infinite;
        }}

        .hero-role {{
            font-size: 1.12rem;
            color: var(--muted);
            font-weight: 600;
        }}

        .hero-summary {{
            max-width: 760px;

            color: var(--muted);

            line-height: 1.85;
            font-size: 1rem;
        }}

        /* --------------------------------
           PROFILE IMAGE
        -------------------------------- */

        .profile-image img {{
            border-radius: 20px;

            border: 1px solid var(--border);

            box-shadow:
                0 20px 50px rgba(0, 0, 0, 0.25);
        }}

        /* --------------------------------
           LINKS
        -------------------------------- */

        .link-row {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.7rem;
            margin-top: 1.4rem;
        }}

        .icon-link {{
            display: inline-flex;

            align-items: center;
            gap: 0.55rem;

            padding: 0.72rem 1rem;

            border: 1px solid var(--border);
            border-radius: 12px;

            background: rgba(255, 255, 255, 0.04);

            color: var(--text) !important;

            text-decoration: none !important;

            transition: 0.25s ease;
        }}

        .icon-link:hover {{
            transform: translateY(-3px);

            border-color: rgba(34, 211, 238, 0.5);

            background: rgba(34, 211, 238, 0.08);

            box-shadow:
                0 10px 25px rgba(34, 211, 238, 0.10);
        }}

        /* --------------------------------
           SECTION TITLES
        -------------------------------- */

        .section-title {{
            margin: 3rem 0 1.2rem;
        }}

        .section-title h2 {{
            font-family: 'Space Grotesk', sans-serif;

            font-size: 1.8rem;

            margin: 0;
        }}

        .section-title p {{
            color: var(--muted);
            margin-top: 0.35rem;
        }}

        /* --------------------------------
           STATS
        -------------------------------- */

        .stat-card {{
            padding: 1.35rem;
            min-height: 125px;

            animation: reveal 0.7s ease both;
        }}

        .stat-card:hover {{
            transform: translateY(-6px);

            border-color:
                rgba(96, 165, 250, 0.38);
        }}

        .stat-icon {{
            font-size: 1.2rem;

            color: var(--cyan);

            margin-bottom: 0.7rem;
        }}

        .stat-label {{
            color: var(--muted);

            font-size: 0.8rem;

            text-transform: uppercase;

            letter-spacing: 0.08em;
        }}

        .stat-value {{
            color: var(--text);

            font-weight: 700;

            font-size: 1rem;

            margin-top: 0.35rem;
        }}

        /* --------------------------------
           SKILLS
        -------------------------------- */

        .skill-card {{
            padding: 1.5rem;
            min-height: 210px;
        }}

        .skill-heading {{
            display: flex;

            align-items: center;

            gap: 0.6rem;

            color: var(--text);

            font-weight: 700;

            margin-bottom: 1rem;
        }}

        .skill-heading i {{
            color: var(--violet);
        }}

        .skill-pill {{
            display: inline-block;

            margin: 0.25rem;

            padding: 0.42rem 0.72rem;

            border-radius: 999px;

            font-size: 0.78rem;

            font-weight: 600;

            color: var(--text);

            background:
                linear-gradient(
                    135deg,
                    rgba(34, 211, 238, 0.10),
                    rgba(167, 139, 250, 0.12)
                );

            border: 1px solid var(--border);

            transition: 0.25s ease;
        }}

        .skill-pill:hover {{
            transform: translateY(-2px) scale(1.03);

            border-color:
                rgba(34, 211, 238, 0.4);
        }}

        /* --------------------------------
           EXPERIENCE
        -------------------------------- */

        .timeline-card {{
            padding: 1.7rem;

            border-left: 3px solid transparent;

            border-image:
                linear-gradient(
                    var(--cyan),
                    var(--violet),
                    var(--pink)
                ) 1;
        }}

        .timeline-card h3 {{
            color: var(--text);
        }}

        .experience-meta {{
            color: var(--muted);

            font-size: 0.88rem;

            margin-bottom: 1rem;
        }}

        .experience-list {{
            margin: 0;

            padding-left: 1.15rem;

            color: var(--muted);

            line-height: 1.8;
        }}

        /* --------------------------------
           PROJECTS
        -------------------------------- */

        .project-card {{
            overflow: hidden;

            margin-bottom: 1.5rem;
        }}

        .project-card:hover {{
            transform: translateY(-8px);

            border-color:
                rgba(34, 211, 238, 0.32);

            box-shadow:
                0 24px 60px rgba(0, 0, 0, 0.20);
        }}

        .project-image {{
            width: 100%;
            height: 220px;

            object-fit: cover;

            display: block;

            transition:
                transform 0.6s ease,
                filter 0.6s ease;
        }}

        .project-card:hover .project-image {{
            transform: scale(1.045);
            filter: saturate(1.15);
        }}

        .project-body {{
            padding: 1.4rem;
        }}

        .project-body h3 {{
            color: var(--text);
        }}

        .project-role {{
            color: var(--cyan);

            font-size: 0.82rem;

            font-weight: 700;

            margin-bottom: 0.7rem;
        }}

        .project-description {{
            color: var(--muted);

            line-height: 1.7;
        }}

        /* --------------------------------
           EDUCATION
        -------------------------------- */

        .education-card {{
            padding: 1.5rem;

            display: flex;

            gap: 1rem;

            align-items: center;

            height: 100%;
        }}

        .education-icon {{
            width: 48px;
            height: 48px;

            display: grid;

            place-items: center;

            flex: 0 0 48px;

            border-radius: 14px;

            background:
                linear-gradient(
                    135deg,
                    rgba(34, 211, 238, 0.15),
                    rgba(167, 139, 250, 0.18)
                );

            color: var(--cyan);
        }}

        /* --------------------------------
           CONTACT SECTION
        -------------------------------- */

        .contact-card {{
            padding: 2rem;

            margin-top: 3rem;
            margin-bottom: 0;
        }}

        div[data-testid="stForm"] {{
            margin-top: 0 !important;

            padding: 1.8rem !important;

            border:
                1px solid var(--border) !important;

            border-radius:
                0 0 var(--radius) var(--radius) !important;

            background:
                var(--surface) !important;

            box-shadow:
                0 20px 50px rgba(0, 0, 0, 0.08) !important;
        }}

        /* INPUTS */

        div[data-testid="stTextInput"] label,
        div[data-testid="stTextArea"] label {{
            color: var(--muted) !important;

            font-weight: 600 !important;
        }}

        div[data-testid="stTextInput"] input,
        div[data-testid="stTextArea"] textarea {{
            background:
                var(--input-bg) !important;

            color:
                var(--input-text) !important;

            border:
                1px solid var(--input-border) !important;

            border-radius:
                12px !important;

            transition:
                border-color 0.25s ease,
                box-shadow 0.25s ease,
                background 0.25s ease !important;
        }}

        div[data-testid="stTextInput"] input:focus,
        div[data-testid="stTextArea"] textarea:focus {{
            border-color:
                var(--cyan) !important;

            box-shadow:
                0 0 0 3px rgba(34, 211, 238, 0.12) !important;
        }}

        div[data-testid="stTextInput"] input::placeholder,
        div[data-testid="stTextArea"] textarea::placeholder {{
            color:
                var(--muted) !important;

            opacity: 0.7 !important;
        }}

        /* SEND BUTTON */

        div[data-testid="stFormSubmitButton"] button {{
            min-height: 48px !important;

            border-radius: 12px !important;

            border:
                1px solid rgba(34, 211, 238, 0.30) !important;

            background:
                linear-gradient(
                    135deg,
                    #0891b2,
                    #6366f1
                ) !important;

            color:
                #ffffff !important;

            font-weight:
                700 !important;

            transition:
                transform 0.25s ease,
                box-shadow 0.25s ease !important;
        }}

        div[data-testid="stFormSubmitButton"] button:hover {{
            transform:
                translateY(-2px) !important;

            box-shadow:
                0 12px 30px rgba(34, 211, 238, 0.20) !important;
        }}

        /* --------------------------------
           DOWNLOAD BUTTON
        -------------------------------- */

        .stDownloadButton button {{
            border-radius: 12px !important;

            border:
                1px solid rgba(34, 211, 238, 0.28) !important;

            background:
                linear-gradient(
                    135deg,
                    rgba(34, 211, 238, 0.16),
                    rgba(167, 139, 250, 0.16)
                ) !important;

            color:
                var(--text) !important;

            font-weight:
                700 !important;
        }}

        /* --------------------------------
           THEME TOGGLE
        -------------------------------- */

        .theme-control {{
            display: flex;

            justify-content: flex-end;

            margin-bottom: 1rem;
        }}

        /* --------------------------------
           FOOTER
        -------------------------------- */

        .footer {{
            text-align: center;

            color: var(--muted);

            padding: 2.5rem 0 0.5rem;

            font-size: 0.85rem;
        }}

        /* --------------------------------
           ANIMATIONS
        -------------------------------- */

        @keyframes reveal {{
            from {{
                opacity: 0;
                transform: translateY(18px);
            }}

            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        @keyframes floatGlow {{
            0%, 100% {{
                transform:
                    translate(0, 0) scale(1);
            }}

            50% {{
                transform:
                    translate(-20px, 20px) scale(1.08);
            }}
        }}

        @keyframes gradientText {{
            0% {{
                background-position: 0% 50%;
            }}

            100% {{
                background-position: 220% 50%;
            }}
        }}

        /* --------------------------------
           MOBILE
        -------------------------------- */

        @media (max-width: 768px) {{

            .block-container {{
                padding: 1rem 1rem 2rem !important;
            }}

            div[data-testid="stHorizontalBlock"] {{
                flex-direction: column !important;
                align-items: stretch !important;
                gap: 1rem !important;
            }}

            div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {{
                width: 100% !important;
                min-width: 0 !important;
                flex: 1 1 100% !important;
            }}

            .hero-card,
            .timeline-card,
            .skill-card,
            .education-card {{
                min-width: 0;
                overflow-wrap: anywhere;
            }}

            .hero-card {{
                padding: 1.4rem;
            }}

            .hero-name {{
                font-size: clamp(2.25rem, 10vw, 3rem);
                overflow-wrap: anywhere;
            }}

            .hero-role {{
                font-size: 1rem;
            }}

            .hero-summary {{
                font-size: 0.95rem;
                line-height: 1.7;
            }}

            .link-row {{
                gap: 0.55rem;
            }}

            .icon-link {{
                min-height: 44px;
                padding: 0.65rem 0.8rem;
            }}

            .profile-image img,
            div[data-testid="stImage"] img {{
                display: block;
                width: 100%;
                max-width: 100%;
                height: auto;
            }}

            .section-title {{
                margin-top: 2.2rem;
            }}

            .section-title h2 {{
                font-size: 1.55rem;
            }}

            .stat-card {{
                min-height: 0;
            }}

            .skill-card {{
                min-height: 0;
            }}

            .experience-meta {{
                line-height: 1.7;
                overflow-wrap: anywhere;
            }}

            .project-card {{
                margin-bottom: 0;
            }}

            .project-image {{
                height: clamp(160px, 55vw, 220px);
            }}

            .contact-card {{
                padding: 1.25rem;
            }}

            div[data-testid="stForm"] {{
                padding: 1rem !important;
            }}

            .stDownloadButton,
            .stDownloadButton button {{
                width: 100% !important;
            }}

            .footer {{
                padding-top: 2rem;
                line-height: 1.6;
            }}
        }}

        @media (max-width: 480px) {{

            .block-container {{
                padding-left: 0.75rem !important;
                padding-right: 0.75rem !important;
            }}

            .hero-card {{
                padding: 1.1rem;
                border-radius: 18px;
            }}

            .eyebrow {{
                font-size: 0.7rem;
                letter-spacing: 0.12em;
            }}

            .link-row {{
                display: grid;
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }}

            .icon-link {{
                justify-content: center;
                min-width: 0;
                padding: 0.65rem 0.5rem;
                font-size: 0.85rem;
            }}

            .stat-card,
            .skill-card,
            .timeline-card,
            .project-body,
            .education-card {{
                padding: 1rem;
            }}

            .stat-label {{
                font-size: 0.72rem;
            }}

            .skill-pill {{
                max-width: 100%;
                overflow-wrap: anywhere;
            }}

            div[data-testid="stForm"] {{
                padding: 0.85rem !important;
            }}
        }}

        /* --------------------------------
           REDUCED MOTION
        -------------------------------- */

        @media (prefers-reduced-motion: reduce) {{

            *,
            *::before,
            *::after {{
                animation-duration: 0.01ms !important;

                animation-iteration-count: 1 !important;

                scroll-behavior: auto !important;

                transition-duration: 0.01ms !important;
            }}
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )