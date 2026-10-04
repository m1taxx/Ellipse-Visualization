# Ellipse-Visualization
An interactive Python web application to calculate and visualize ellipses in real-time using Streamlit, Plotly, and NumPy.
<div align="center">

# 🧮 Ellipse Visualizer

**An interactive web app for calculating and plotting an ellipse from custom parameters**

[![Open App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ellipse-visualization-jvpmaqvdo7wanf3vw96zcq.streamlit.app/)

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white)

</div>

---

## 🌐 Live Demo

👉 **[Open the app online](https://ellipse-visualization-jvpmaqvdo7wanf3vw96zcq.streamlit.app/)**

No installation required — just open the link in your browser.

## ✨ Features

- 🎛️ Slider controls: semi-axes **a** and **b**, rotation angle, center coordinates
- 📈 Interactive Plotly chart (zoom, pan, hover tooltips)
- 🔄 Rotate the ellipse by any angle (0–360°)
- 🟣 Optional display of foci and semi-axes (toggle in the sidebar)
- 📐 Automatic calculation of geometric properties
- 🔍 Auto-fitting chart bounds — the ellipse always stays in view with correct proportions

## 📐 What Is Calculated

| Property | Formula |
|---|---|
| Area | `S = π · a · b` |
| Perimeter (Ramanujan approximation) | `P ≈ π · (3(a + b) − √((3a + b)(a + 3b)))` |
| Focal distance | `c = √(\|a² − b²\|)` |
| Eccentricity | `e = c / max(a, b)` |

Ellipse points are generated from the parametric equation with rotation:

```
x = cx + a·cos(t)·cos(φ) − b·sin(t)·sin(φ)
y = cy + a·cos(t)·sin(φ) + b·sin(t)·cos(φ),   t ∈ [0, 2π]
```

## 🚀 Run Locally

```bash
# 1. Clone the repository
git clone https://m1taxx/Ellipse-Visualization.git
cd Ellipse-Visualization

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run elips_geometry_vizualization.py
```

The app will open at `http://localhost:8501`.

## 📁 Project Structure

```
├── elips_geometry_vizualization.py   # main app code
├── requirements.txt                  # dependencies
└── README.md
```

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) — UI
- [Plotly](https://plotly.com/python/) — interactive charts
- [NumPy](https://numpy.org/) — numerical computations

---

<div align="center">
Made with ❤️ and Python
</div>
