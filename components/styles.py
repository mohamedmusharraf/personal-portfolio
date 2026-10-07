import streamlit as st


def load_styles(light_mode=False):
    if light_mode:
        theme = {
            "bg": "#f0f4ff",
            "surface": "rgba(255, 255, 255, 0.80)",
            "surface_strong": "rgba(255, 255, 255, 0.96)",
            "border": "rgba(15, 23, 42, 0.10)",
            "text": "#0f172a",
            "muted": "#475569",
            "input_bg": "#ffffff",
            "input_text": "#0f172a",
            "input_border": "#cbd5e1",
            "orb1": "rgba(99, 102, 241, 0.25)",
            "orb2": "rgba(236, 72, 153, 0.20)",
            "orb3": "rgba(34, 211, 238, 0.22)",
            "orb4": "rgba(251, 146, 60, 0.18)",
        }
    else:
        theme = {
            "bg": "#04060f",
            "surface": "rgba(10, 15, 35, 0.75)",
            "surface_strong": "rgba(14, 20, 45, 0.94)",
            "border": "rgba(148, 163, 184, 0.12)",
            "text": "#f1f5f9",
            "muted": "#94a3b8",
            "input_bg": "#0d1226",
            "input_text": "#f1f5f9",
            "input_border": "#1e2d4a",
            "orb1": "rgba(99, 102, 241, 0.30)",
            "orb2": "rgba(236, 72, 153, 0.22)",
            "orb3": "rgba(34, 211, 238, 0.25)",
            "orb4": "rgba(251, 146, 60, 0.18)",
        }

    st.markdown(
        f"""
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link
            href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700;800&family=Outfit:wght@300;400;600;700;800&display=swap"
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

            /* Vivid palette */
            --cyan:    #22d3ee;
            --blue:    #60a5fa;
            --indigo:  #818cf8;
            --violet:  #a78bfa;
            --pink:    #f472b6;
            --rose:    #fb7185;
            --orange:  #fb923c;
            --amber:   #fbbf24;
            --green:   #34d399;
            --teal:    #2dd4bf;

            --radius: 24px;
            --radius-sm: 14px;
        }}

        html {{ scroll-behavior: smooth; }}

        *, *::before, *::after {{ box-sizing: border-box; margin: 0; }}

        body {{ font-family: 'Inter', sans-serif; }}

        /* =========================================
           ANIMATED BACKGROUND
        ========================================= */

        .stApp {{
            background: var(--bg);
            color: var(--text);
            overflow-x: hidden;
            transition: background 0.4s ease, color 0.4s ease;
            position: relative;
        }}

        /* Multi-layer aurora background */
        .stApp::before {{
            content: "";
            position: fixed;
            inset: 0;
            z-index: 0;
            pointer-events: none;
            background:
                radial-gradient(ellipse 80% 60% at 10%  10%, {theme["orb1"]}, transparent 55%),
                radial-gradient(ellipse 70% 50% at 90%  15%, {theme["orb2"]}, transparent 50%),
                radial-gradient(ellipse 60% 70% at 50%  85%, {theme["orb3"]}, transparent 55%),
                radial-gradient(ellipse 55% 40% at 80%  70%, {theme["orb4"]}, transparent 48%);
            animation: auroraDrift 18s ease-in-out infinite alternate;
            filter: blur(2px);
        }}

        .stApp > * {{ position: relative; z-index: 1; }}

        /* Animated floating orbs */
        .stApp::after {{
            content: "";
            position: fixed;
            width: 500px;
            height: 500px;
            border-radius: 50%;
            top: -120px;
            right: -150px;
            background: conic-gradient(
                from 0deg,
                rgba(99, 102, 241, 0.18),
                rgba(236, 72, 153, 0.15),
                rgba(34, 211, 238, 0.18),
                rgba(99, 102, 241, 0.18)
            );
            filter: blur(80px);
            animation: orbSpin 25s linear infinite;
            z-index: 0;
            pointer-events: none;
        }}

        .block-container {{
            max-width: 1200px;
            padding-top: 1.5rem;
            padding-bottom: 4rem;
            position: relative;
            z-index: 2;
        }}

        /* =========================================
           GLOBAL TEXT
        ========================================= */

        h1, h2, h3, h4 {{ color: var(--text); font-family: 'Space Grotesk', sans-serif; }}
        p, label {{ color: var(--text); }}

        .stCaption,
        [data-testid="stCaptionContainer"] {{
            color: var(--muted) !important;
        }}

        /* =========================================
           GLASS CARDS — enhanced
        ========================================= */

        .glass-card,
        .hero-card {{
            position: relative;
            overflow: hidden;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            box-shadow:
                0 0 0 1px rgba(255,255,255,0.04) inset,
                0 24px 80px rgba(0, 0, 0, 0.22);
            transition:
                background 0.35s ease,
                border-color 0.35s ease,
                box-shadow 0.4s ease,
                transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
        }}

        /* Shimmering rainbow border on hover via pseudo-element */
        .glass-card::before {{
            content: "";
            position: absolute;
            inset: -1px;
            border-radius: calc(var(--radius) + 1px);
            padding: 1px;
            background: conic-gradient(
                from var(--angle, 0deg),
                var(--cyan), var(--violet), var(--pink), var(--orange), var(--cyan)
            );
            -webkit-mask:
                linear-gradient(#fff 0 0) content-box,
                linear-gradient(#fff 0 0);
            mask:
                linear-gradient(#fff 0 0) content-box,
                linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            opacity: 0;
            transition: opacity 0.35s ease;
            animation: borderSpin 4s linear infinite;
        }}

        .glass-card:hover::before {{
            opacity: 1;
        }}

        .glass-card:hover {{
            transform: translateY(-7px);
            box-shadow:
                0 0 0 1px rgba(255,255,255,0.07) inset,
                0 32px 90px rgba(0, 0, 0, 0.28),
                0 0 40px rgba(99, 102, 241, 0.12);
        }}

        /* =========================================
           HERO
        ========================================= */

        .hero-card {{
            padding: 3rem;
            animation: revealUp 0.9s cubic-bezier(0.16, 1, 0.3, 1) both;
            border-image: none;
            background: linear-gradient(
                135deg,
                rgba(14, 20, 50, 0.85) 0%,
                rgba(10, 15, 38, 0.80) 100%
            );
        }}

        /* Glowing orb inside hero */
        .hero-card .hero-glow {{
            position: absolute;
            width: 320px;
            height: 320px;
            right: -80px;
            top: -100px;
            background: conic-gradient(
                from 0deg,
                var(--cyan),
                var(--violet),
                var(--pink),
                var(--orange),
                var(--cyan)
            );
            filter: blur(80px);
            opacity: 0.20;
            animation: orbSpin 12s linear infinite;
            border-radius: 50%;
        }}

        .hero-card .hero-glow-2 {{
            position: absolute;
            width: 200px;
            height: 200px;
            left: -60px;
            bottom: -60px;
            background: radial-gradient(circle, var(--green), var(--teal), transparent);
            filter: blur(60px);
            opacity: 0.15;
            animation: floatGlow 9s ease-in-out infinite alternate;
            border-radius: 50%;
        }}

        .eyebrow {{
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            color: var(--cyan);
            font-size: 0.75rem;
            font-weight: 800;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            background: linear-gradient(90deg, var(--cyan), var(--violet));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.6rem;
        }}

        .hero-name {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: clamp(2.8rem, 7.5vw, 5.6rem);
            line-height: 0.97;
            font-weight: 800;
            margin: 0 0 1rem;
            background: linear-gradient(
                125deg,
                var(--text) 0%,
                var(--cyan) 25%,
                var(--violet) 50%,
                var(--pink) 75%,
                var(--orange) 100%
            );
            background-size: 300% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientFlow 8s ease-in-out infinite alternate;
        }}

        .hero-role {{
            font-size: 1.15rem;
            font-weight: 600;
            background: linear-gradient(90deg, var(--green), var(--teal), var(--cyan));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }}

        .hero-summary {{
            max-width: 760px;
            color: var(--muted);
            line-height: 1.9;
            font-size: 1.0rem;
        }}

        /* =========================================
           PROFILE IMAGE
        ========================================= */

        .profile-image {{
            position: relative;
        }}

        .profile-image::before {{
            content: "";
            position: absolute;
            inset: -4px;
            border-radius: 24px;
            background: linear-gradient(135deg, var(--cyan), var(--violet), var(--pink), var(--orange));
            filter: blur(12px);
            opacity: 0.55;
            z-index: -1;
            animation: borderSpin 6s linear infinite;
        }}

        .profile-image img {{
            border-radius: 20px;
            border: 2px solid rgba(255,255,255,0.08);
            box-shadow: 0 24px 60px rgba(0, 0, 0, 0.35);
            transition: transform 0.4s ease;
        }}

        .profile-image:hover img {{
            transform: scale(1.03);
        }}

        /* =========================================
           LINKS / SOCIAL BUTTONS
        ========================================= */

        .link-row {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.65rem;
            margin-top: 1.6rem;
        }}

        .icon-link {{
            display: inline-flex;
            align-items: center;
            gap: 0.55rem;
            padding: 0.70rem 1.1rem;
            border-radius: var(--radius-sm);
            border: 1px solid rgba(255,255,255,0.12);
            background: rgba(255, 255, 255, 0.05);
            color: var(--text) !important;
            text-decoration: none !important;
            font-weight: 600;
            font-size: 0.9rem;
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            position: relative;
            overflow: hidden;
        }}

        .icon-link::before {{
            content: "";
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, var(--cyan), var(--violet));
            opacity: 0;
            transition: opacity 0.3s ease;
        }}

        .icon-link:hover {{
            transform: translateY(-4px) scale(1.04);
            border-color: transparent;
            color: #fff !important;
            box-shadow: 0 12px 28px rgba(99, 102, 241, 0.30);
        }}

        .icon-link:hover::before {{
            opacity: 1;
        }}

        .icon-link > * {{
            position: relative;
            z-index: 1;
        }}

        /* =========================================
           SECTION TITLES
        ========================================= */

        .section-title {{
            margin: 3.5rem 0 1.4rem;
            animation: revealUp 0.7s ease both;
        }}

        .section-title h2 {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 2rem;
            font-weight: 800;
            margin: 0 0 0.3rem;
            display: inline-block;
            background: linear-gradient(90deg, var(--text), var(--indigo), var(--pink));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .section-title .title-bar {{
            height: 3px;
            width: 60px;
            border-radius: 4px;
            background: linear-gradient(90deg, var(--cyan), var(--violet), var(--pink));
            margin: 0.5rem 0 0.5rem;
            animation: barGrow 1s ease both;
        }}

        .section-title p {{
            color: var(--muted);
            margin-top: 0.3rem;
            font-size: 0.97rem;
        }}

        /* =========================================
           STATS — colorful accent cards
        ========================================= */

        .stat-card {{
            padding: 1.6rem 1.4rem;
            min-height: 130px;
            animation: revealUp 0.7s ease both;
            text-align: center;
        }}

        .stat-card:nth-child(1) {{ --accent: var(--cyan);   }}
        .stat-card:nth-child(2) {{ --accent: var(--violet); }}
        .stat-card:nth-child(3) {{ --accent: var(--pink);   }}
        .stat-card:nth-child(4) {{ --accent: var(--orange); }}

        .stat-card:hover {{
            transform: translateY(-8px) scale(1.02);
        }}

        .stat-icon {{
            font-size: 1.6rem;
            margin-bottom: 0.65rem;
            filter: drop-shadow(0 0 8px currentColor);
        }}

        /* Each stat card gets a unique icon color */
        .stat-card:nth-child(1) .stat-icon {{ color: var(--cyan);   }}
        .stat-card:nth-child(2) .stat-icon {{ color: var(--violet); }}
        .stat-card:nth-child(3) .stat-icon {{ color: var(--pink);   }}
        .stat-card:nth-child(4) .stat-icon {{ color: var(--orange); }}

        .stat-label {{
            color: var(--muted);
            font-size: 0.74rem;
            text-transform: uppercase;
            letter-spacing: 0.10em;
            font-weight: 700;
        }}

        .stat-value {{
            font-weight: 800;
            font-size: 1.05rem;
            margin-top: 0.4rem;
            background: linear-gradient(90deg, var(--text), var(--text) 60%, var(--accent, var(--cyan)));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        /* =========================================
           SKILLS — colorful pills per category
        ========================================= */

        .skill-card {{
            padding: 1.8rem;
            min-height: 220px;
            animation: revealUp 0.75s ease both;
        }}

        .skill-heading {{
            display: flex;
            align-items: center;
            gap: 0.65rem;
            font-weight: 800;
            font-size: 1rem;
            margin-bottom: 1.1rem;
        }}

        /* Per-category heading colors */
        .skill-card.cat-0 .skill-heading {{ color: var(--cyan);   }}
        .skill-card.cat-0 .skill-heading i {{ color: var(--cyan);   filter: drop-shadow(0 0 6px var(--cyan)); }}
        .skill-card.cat-1 .skill-heading {{ color: var(--violet); }}
        .skill-card.cat-1 .skill-heading i {{ color: var(--violet); filter: drop-shadow(0 0 6px var(--violet)); }}
        .skill-card.cat-2 .skill-heading {{ color: var(--pink);   }}
        .skill-card.cat-2 .skill-heading i {{ color: var(--pink);   filter: drop-shadow(0 0 6px var(--pink)); }}

        /* Per-category pill gradients */
        .skill-card.cat-0 .skill-pill {{
            background: linear-gradient(135deg, rgba(34,211,238,0.18), rgba(34,211,238,0.06));
            border-color: rgba(34,211,238,0.30);
            color: var(--cyan);
        }}
        .skill-card.cat-1 .skill-pill {{
            background: linear-gradient(135deg, rgba(167,139,250,0.18), rgba(167,139,250,0.06));
            border-color: rgba(167,139,250,0.30);
            color: var(--violet);
        }}
        .skill-card.cat-2 .skill-pill {{
            background: linear-gradient(135deg, rgba(244,114,182,0.18), rgba(244,114,182,0.06));
            border-color: rgba(244,114,182,0.30);
            color: var(--pink);
        }}

        .skill-pill {{
            display: inline-block;
            margin: 0.22rem;
            padding: 0.45rem 0.85rem;
            border-radius: 999px;
            font-size: 0.80rem;
            font-weight: 700;
            border: 1px solid var(--border);
            transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
            cursor: default;
        }}

        .skill-pill:hover {{
            transform: translateY(-3px) scale(1.08);
            box-shadow: 0 8px 20px rgba(0,0,0,0.18);
            filter: brightness(1.2);
        }}

        /* =========================================
           EXPERIENCE
        ========================================= */

        .timeline-card {{
            padding: 2rem;
            border-left: 3px solid transparent;
            border-image: linear-gradient(to bottom, var(--cyan), var(--violet), var(--pink)) 1;
            animation: revealLeft 0.8s ease both;
            position: relative;
        }}

        .timeline-card::after {{
            content: "";
            position: absolute;
            left: -1px;
            top: 0;
            bottom: 0;
            width: 3px;
            background: linear-gradient(to bottom, var(--cyan), var(--violet), var(--pink));
            border-radius: 4px;
            filter: drop-shadow(0 0 6px var(--violet));
        }}

        .timeline-card h3 {{
            font-size: 1.15rem;
            font-weight: 700;
            margin-bottom: 0.6rem;
            background: linear-gradient(90deg, var(--text), var(--blue));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .experience-meta {{
            color: var(--muted);
            font-size: 0.88rem;
            margin-bottom: 1rem;
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
            align-items: center;
        }}

        .experience-list {{
            margin: 0;
            padding-left: 1.2rem;
            color: var(--muted);
            line-height: 1.9;
        }}

        .experience-list li {{
            margin-bottom: 0.35rem;
            transition: color 0.2s;
        }}

        .experience-list li::marker {{
            color: var(--cyan);
        }}

        .experience-list li:hover {{
            color: var(--text);
        }}

        /* =========================================
           PROJECTS
        ========================================= */

        .project-card {{
            overflow: hidden;
            margin-bottom: 1.5rem;
            animation: revealUp 0.8s ease both;
        }}

        /* Each project card accent color */
        .project-card:nth-child(1) {{ --proj-accent: var(--cyan);   }}
        .project-card:nth-child(2) {{ --proj-accent: var(--violet); }}
        .project-card:nth-child(3) {{ --proj-accent: var(--pink);   }}
        .project-card:nth-child(4) {{ --proj-accent: var(--orange); }}

        .project-card:hover {{
            transform: translateY(-10px);
            box-shadow:
                0 0 0 1px rgba(255,255,255,0.07) inset,
                0 30px 70px rgba(0,0,0,0.28),
                0 0 50px rgba(99, 102, 241, 0.12);
        }}

        .project-image-wrap {{
            position: relative;
            overflow: hidden;
            height: 225px;
        }}

        .project-image {{
            width: 100%;
            height: 225px;
            object-fit: cover;
            display: block;
            transition: transform 0.7s ease, filter 0.5s ease;
        }}

        .project-card:hover .project-image {{
            transform: scale(1.07);
            filter: saturate(1.3) brightness(0.9);
        }}

        /* Overlay gradient on image */
        .project-image-wrap::after {{
            content: "";
            position: absolute;
            inset: 0;
            background: linear-gradient(
                to bottom,
                transparent 40%,
                rgba(4, 6, 15, 0.6) 100%
            );
        }}

        .project-body {{
            padding: 1.5rem;
        }}

        .project-body h3 {{
            color: var(--text);
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 0.4rem;
        }}

        .project-role {{
            font-size: 0.80rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin-bottom: 0.75rem;
            background: linear-gradient(90deg, var(--cyan), var(--violet));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .project-description {{
            color: var(--muted);
            line-height: 1.75;
            font-size: 0.93rem;
        }}

        /* =========================================
           EDUCATION
        ========================================= */

        .education-card {{
            padding: 1.7rem;
            display: flex;
            gap: 1.1rem;
            align-items: center;
            height: 100%;
            animation: revealUp 0.7s ease both;
        }}

        .education-icon {{
            width: 54px;
            height: 54px;
            display: grid;
            place-items: center;
            flex: 0 0 54px;
            border-radius: 16px;
            font-size: 1.3rem;
            transition: transform 0.3s ease;
        }}

        .education-card:nth-child(1) .education-icon {{
            background: linear-gradient(135deg, rgba(34,211,238,0.20), rgba(99,102,241,0.20));
            color: var(--cyan);
            box-shadow: 0 0 20px rgba(34,211,238,0.18);
        }}

        .education-card:nth-child(2) .education-icon {{
            background: linear-gradient(135deg, rgba(244,114,182,0.20), rgba(167,139,250,0.20));
            color: var(--pink);
            box-shadow: 0 0 20px rgba(244,114,182,0.18);
        }}

        .education-card:hover .education-icon {{
            transform: rotate(10deg) scale(1.1);
        }}

        .education-card h3 {{
            font-size: 1rem;
            font-weight: 700;
            margin: 0 0 0.25rem;
        }}

        /* =========================================
           CONTACT SECTION
        ========================================= */

        .contact-card {{
            padding: 2.2rem;
            margin-top: 3rem;
            margin-bottom: 0;
        }}

        div[data-testid="stForm"] {{
            margin-top: 0 !important;
            padding: 1.8rem !important;
            border: 1px solid var(--border) !important;
            border-radius: 0 0 var(--radius) var(--radius) !important;
            background: var(--surface) !important;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.10) !important;
        }}

        /* INPUTS */
        div[data-testid="stTextInput"] label,
        div[data-testid="stTextArea"] label {{
            color: var(--muted) !important;
            font-weight: 700 !important;
            font-size: 0.85rem !important;
            text-transform: uppercase !important;
            letter-spacing: 0.07em !important;
        }}

        div[data-testid="stTextInput"] input,
        div[data-testid="stTextArea"] textarea {{
            background: var(--input-bg) !important;
            color: var(--input-text) !important;
            border: 1px solid var(--input-border) !important;
            border-radius: var(--radius-sm) !important;
            transition: border-color 0.25s ease, box-shadow 0.25s ease !important;
        }}

        div[data-testid="stTextInput"] input:focus,
        div[data-testid="stTextArea"] textarea:focus {{
            border-color: var(--violet) !important;
            box-shadow: 0 0 0 3px rgba(167, 139, 250, 0.18) !important;
        }}

        div[data-testid="stTextInput"] input::placeholder,
        div[data-testid="stTextArea"] textarea::placeholder {{
            color: var(--muted) !important;
            opacity: 0.6 !important;
        }}

        /* SEND BUTTON */
        div[data-testid="stFormSubmitButton"] button {{
            min-height: 50px !important;
            border-radius: var(--radius-sm) !important;
            border: none !important;
            background: linear-gradient(
                135deg,
                #6366f1, #a855f7, #ec4899
            ) !important;
            color: #ffffff !important;
            font-weight: 800 !important;
            font-size: 1rem !important;
            letter-spacing: 0.03em !important;
            transition: transform 0.25s ease, box-shadow 0.25s ease !important;
        }}

        div[data-testid="stFormSubmitButton"] button:hover {{
            transform: translateY(-3px) scale(1.02) !important;
            box-shadow: 0 16px 40px rgba(168, 85, 247, 0.35) !important;
        }}

        /* =========================================
           DOWNLOAD BUTTON
        ========================================= */

        .stDownloadButton button {{
            border-radius: var(--radius-sm) !important;
            border: 1px solid rgba(34, 211, 238, 0.30) !important;
            background: linear-gradient(
                135deg,
                rgba(34, 211, 238, 0.18),
                rgba(167, 139, 250, 0.18)
            ) !important;
            color: var(--text) !important;
            font-weight: 700 !important;
            transition: transform 0.25s ease, box-shadow 0.25s ease !important;
        }}

        .stDownloadButton button:hover {{
            transform: translateY(-3px) !important;
            box-shadow: 0 12px 30px rgba(34, 211, 238, 0.20) !important;
        }}

        /* =========================================
           FOOTER
        ========================================= */

        .footer {{
            text-align: center;
            padding: 2.5rem 0 0.5rem;
            font-size: 0.85rem;
        }}

        .footer-text {{
            background: linear-gradient(90deg, var(--muted), var(--cyan), var(--violet), var(--muted));
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientFlow 5s ease-in-out infinite alternate;
        }}

        /* =========================================
           ANIMATIONS
        ========================================= */

        @property --angle {{
            syntax: "<angle>";
            initial-value: 0deg;
            inherits: false;
        }}

        @keyframes revealUp {{
            from {{ opacity: 0; transform: translateY(24px); }}
            to   {{ opacity: 1; transform: translateY(0); }}
        }}

        @keyframes revealLeft {{
            from {{ opacity: 0; transform: translateX(-24px); }}
            to   {{ opacity: 1; transform: translateX(0); }}
        }}

        @keyframes floatGlow {{
            0%   {{ transform: translate(0, 0) scale(1); }}
            50%  {{ transform: translate(-20px, 18px) scale(1.08); }}
            100% {{ transform: translate(10px, -10px) scale(0.96); }}
        }}

        @keyframes gradientFlow {{
            0%   {{ background-position: 0% 50%;   }}
            100% {{ background-position: 100% 50%; }}
        }}

        @keyframes auroraDrift {{
            0%   {{ opacity: 1; transform: scale(1) rotate(0deg); }}
            50%  {{ opacity: 0.85; transform: scale(1.05) rotate(3deg); }}
            100% {{ opacity: 1; transform: scale(1) rotate(-2deg); }}
        }}

        @keyframes orbSpin {{
            from {{ transform: rotate(0deg); }}
            to   {{ transform: rotate(360deg); }}
        }}

        @keyframes borderSpin {{
            from {{ --angle: 0deg; }}
            to   {{ --angle: 360deg; }}
        }}

        @keyframes barGrow {{
            from {{ width: 0; opacity: 0; }}
            to   {{ width: 60px; opacity: 1; }}
        }}

        @keyframes pulse {{
            0%, 100% {{ box-shadow: 0 0 0 0 rgba(99, 102, 241, 0.4); }}
            50%       {{ box-shadow: 0 0 0 10px rgba(99, 102, 241, 0); }}
        }}

        /* Staggered animation delays for cards */
        .glass-card:nth-child(1) {{ animation-delay: 0.05s; }}
        .glass-card:nth-child(2) {{ animation-delay: 0.12s; }}
        .glass-card:nth-child(3) {{ animation-delay: 0.19s; }}
        .glass-card:nth-child(4) {{ animation-delay: 0.26s; }}

        /* =========================================
           MOBILE
        ========================================= */

        @media (max-width: 768px) {{
            .block-container {{
                padding: 1rem 1rem 2.5rem !important;
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
                padding: 1.5rem;
            }}

            .hero-name {{
                font-size: clamp(2.2rem, 10vw, 3rem);
                overflow-wrap: anywhere;
            }}

            .hero-role {{ font-size: 1rem; }}
            .hero-summary {{ font-size: 0.95rem; line-height: 1.75; }}
            .link-row {{ gap: 0.5rem; }}
            .icon-link {{ min-height: 44px; padding: 0.65rem 0.85rem; }}

            .profile-image img,
            div[data-testid="stImage"] img {{
                display: block; width: 100%; max-width: 100%; height: auto;
            }}

            .section-title {{ margin-top: 2.5rem; }}
            .section-title h2 {{ font-size: 1.6rem; }}
            .stat-card {{ min-height: 0; }}
            .skill-card {{ min-height: 0; }}
            .experience-meta {{ line-height: 1.7; overflow-wrap: anywhere; }}
            .project-card {{ margin-bottom: 0; }}
            .project-image {{ height: clamp(160px, 55vw, 220px); }}
            .project-image-wrap {{ height: clamp(160px, 55vw, 220px); }}
            .contact-card {{ padding: 1.25rem; }}
            div[data-testid="stForm"] {{ padding: 1rem !important; }}
            .stDownloadButton,
            .stDownloadButton button {{ width: 100% !important; }}
            .footer {{ padding-top: 2rem; line-height: 1.6; }}
        }}

        @media (max-width: 480px) {{
            .block-container {{
                padding-left: 0.75rem !important;
                padding-right: 0.75rem !important;
            }}

            .hero-card {{
                padding: 1.2rem;
                border-radius: 18px;
            }}

            .eyebrow {{ font-size: 0.7rem; letter-spacing: 0.12em; }}

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
            .education-card {{ padding: 1rem; }}

            .stat-label {{ font-size: 0.72rem; }}
            .skill-pill {{ max-width: 100%; overflow-wrap: anywhere; }}
            div[data-testid="stForm"] {{ padding: 0.85rem !important; }}
        }}

        /* =========================================
           REDUCED MOTION
        ========================================= */

        @media (prefers-reduced-motion: reduce) {{
            *, *::before, *::after {{
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