import numpy as np
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Візуалізація еліпса", layout="wide")

st.title("🧮 Візуалізація еліпса за вхідними даними")
st.write(
    "Інтерактивний додаток для розрахунку та відображення геометричних параметрів еліпса."
)

# Бічне меню з параметрами
st.sidebar.header("Параметри еліпса")
rx = st.sidebar.slider(
    "Піввісь X (a)", min_value=1.0, max_value=20.0, value=10.0
)
ry = st.sidebar.slider("Піввісь Y (b)", min_value=1.0, max_value=20.0, value=5.0)
angle = st.sidebar.slider(
    "Кут повороту (°)", min_value=0, max_value=360, value=30
)
cx = st.sidebar.slider("Центр X", min_value=-10.0, max_value=10.0, value=0.0)
cy = st.sidebar.slider("Центр Y", min_value=-10.0, max_value=10.0, value=0.0)

# Математичний розрахунок точок
t = np.linspace(0, 2 * np.pi, 300)
rad = np.radians(angle)

# Параметричне рівняння еліпса з поворотом
x_raw = rx * np.cos(t)
y_raw = ry * np.sin(t)

x_rot = cx + x_raw * np.cos(rad) - y_raw * np.sin(rad)
y_rot = cy + x_raw * np.sin(rad) + y_raw * np.cos(rad)

# Побудова інтерактивного графіка через Plotly
fig = go.Figure()

# Сам еліпс
fig.add_trace(
    go.Scatter(
        x=x_rot,
        y=y_rot,
        mode="lines",
        name="Еліпс",
        line=dict(color="#38bdf8", width=3),
    )
)

# Точка центра
fig.add_trace(
    go.Scatter(
        x=[cx],
        y=[cy],
        mode="markers",
        name="Центр",
        marker=dict(color="red", size=8),
    )
)

fig.update_layout(
    xaxis=dict(range=[-25, 25], zeroline=True, title="Ось X"),
    yaxis=dict(range=[-25, 25], zeroline=True, title="Ось Y"),
    scaleanchor="x",
    scaleratio=1,
    height=600,
)

# Вивід графіка та геометричних характеристик
col1, col2 = st.columns([3, 1])

with col1:
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Характеристики:")
    st.metric("Площа", f"{np.pi * rx * ry:.2f}")
    st.metric(
        "Периметр (прибл.)",
        f"{np.pi * (3*(rx+ry) - np.sqrt((3*rx+ry)*(rx+3*ry))):.2f}",
    )
    c = np.sqrt(abs(rx**2 - ry**2))
    st.metric("Фокальна відстань (c)", f"{c:.2f}")