# Mohamed Musharraf — Modern Streamlit Portfolio

A clean, animated and responsive developer portfolio built with Python + Streamlit.

## Design changes

- Removed all emojis from the UI.
- Added Font Awesome icons.
- Added animated gradient typography and subtle glow effects.
- Added glassmorphism cards with hover animations.
- Added responsive mobile styling.
- Added working Dark / Light mode with Streamlit session state.
- Fixed contact form colors, labels, focus states, textarea and submit button.
- Added reduced-motion accessibility support.
- Separated portfolio data from UI components.
- Separated styling from application logic.
- Centralized configuration.
- Escaped dynamic HTML values before rendering.
- Kept the existing portfolio information and project content.

## Project structure

```text
musharraf_portfolio/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
├── assets/
│   └── images/
│       └── my_photo.png
├── components/
│   ├── __init__.py
│   ├── styles.py
│   └── ui.py
└── data/
    ├── __init__.py
    └── portfolio_data.py
```

## Setup

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run app.py
```

## Important

Place your existing `my_photo.png` inside:

```text
assets/images/my_photo.png
```

The project images currently use remote Unsplash URLs. For production, local project images are recommended.
