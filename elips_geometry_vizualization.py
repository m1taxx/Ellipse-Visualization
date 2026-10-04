import numpy as np
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Візуалізація еліпса", layout="wide")

st.title("🧮 Візуалізація еліпса за вхідними даними")
st.write(
    "Інтерактивний додаток для розрахунку та відображення геометричних параметрів еліпса."
)

# ---------- Параметри ----------
st.sidebar.header("Параметри еліпса")
rx = st.sidebar.slider("Піввісь X (a)", 1.0, 20.0, 10.0, step=0.5)
ry = st.sidebar.slider("Піввісь Y (b)", 1.0, 20.0, 5.0, step=0.5)
angle = st.sidebar.slider("Кут повороту (°)", 0, 360, 30)
cx = st.sidebar.slider("Центр X", -10.0, 10.0, 0.0, step=0.5)
cy = st.sidebar.slider("Центр Y", -10.0, 10.0, 0.0, step=0.5)
show_foci = st.sidebar.checkbox("Показати фокуси", value=True)
show_axes = st.sidebar.checkbox("Показати півосі", value=True)

rad = np.radians(angle)
cos_a, sin_a = np.cos(rad), np.sin(rad)


def transform(x, y):
    """Поворот на кут angle навколо початку координат + зсув у центр (cx, cy)."""
    return (
        cx + x * cos_a - y * sin_a,
        cy + x * sin_a + y * cos_a,
    )


# ---------- Розрахунок ----------
t = np.linspace(0, 2 * np.pi, 400)
x_rot, y_rot = transform(rx * np.cos(t), ry * np.sin(t))

a_big, b_small = max(rx, ry), min(rx, ry)
c = np.sqrt(a_big**2 - b_small**2)
eccentricity = c / a_big
area = np.pi * rx * ry
# Наближена формула Рамануджана
perimeter = np.pi * (3 * (rx + ry) - np.sqrt((3 * rx + ry) * (rx + 3 * ry)))

# Фокуси лежать на великій осі
if rx >= ry:
    f1 = transform(-c, 0)
    f2 = transform(c, 0)
else:
    f1 = transform(0, -c)
    f2 = transform(0, c)

# ---------- Графік ----------
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=x_rot,
        y=y_rot,
        mode="lines",
        name="Еліпс",
        line=dict(color="#38bdf8", width=3),
    )
)

if show_axes:
    ax1 = transform(np.array([-rx, rx]), np.array([0, 0]))
    ax2 = transform(np.array([0, 0]), np.array([-ry, ry]))
    fig.add_trace(
        go.Scatter(
            x=ax1[0], y=ax1[1], mode="lines", name="Вісь a",
            line=dict(color="#f59e0b", width=1.5, dash="dash"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=ax2[0], y=ax2[1], mode="lines", name="Вісь b",
            line=dict(color="#10b981", width=1.5, dash="dash"),
        )
    )

if show_foci:
    fig.add_trace(
        go.Scatter(
            x=[f1[0], f2[0]], y=[f1[1], f2[1]], mode="markers", name="Фокуси",
            marker=dict(color="#a855f7", size=9, symbol="diamond"),
        )
    )

fig.add_trace(
    go.Scatter(
        x=[cx], y=[cy], mode="markers", name="Центр",
        marker=dict(color="red", size=8),
    )
)

# Автоматичний квадратний діапазон осей, щоб еліпс завжди був у кадрі
x_min, x_max = x_rot.min(), x_rot.max()
y_min, y_max = y_rot.min(), y_rot.max()
mid_x, mid_y = (x_min + x_max) / 2, (y_min + y_max) / 2
half = max(x_max - x_min, y_max - y_min) / 2 * 1.2 + 1

fig.update_layout(
    xaxis=dict(range=[mid_x - half, mid_x + half], zeroline=True, title="Ось X"),
    yaxis=dict(
        range=[mid_y - half, mid_y + half],
        zeroline=True,
        title="Ось Y",
        scaleanchor="x",  
        scaleratio=1,
    ),
    height=650,
    margin=dict(l=10, r=10, t=30, b=10),
    legend=dict(orientation="h", y=1.05),
)

# ---------- Вивід ----------
col1, col2 = st.columns([3, 1])

with col1:
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Характеристики:")
    st.metric("Площа", f"{area:.2f}")
    st.metric("Периметр (прибл.)", f"{perimeter:.2f}")
    st.metric("Фокальна відстань (c)", f"{c:.2f}")
    st.metric("Ексцентриситет (e)", f"{eccentricity:.3f}")
