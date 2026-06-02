import streamlit as st

st.set_page_config(
    page_title="Purplle Store Intelligence",
    layout="wide"
)

st.title("🏪 Purplle Store Intelligence Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total NMV", "₹34,831.74")

with col2:
    st.metric("Peak Sales Hour", "19:00")

with col3:
    st.metric("Busiest Camera", "CAM 2")

with col4:
    st.metric("Peak Occupancy", "9")

st.divider()

st.subheader("Camera Occupancy")

camera_data = {
    "CAM 1": 3.06,
    "CAM 2": 5.21,
    "CAM 3": 0.95,
    "CAM 4": 0.01,
    "CAM 5": 1.24,
}

st.bar_chart(camera_data)

st.divider()

st.subheader("Top Brands")

st.write("""
1. Faces Canada (32)

2. Good Vibes (14)

3. Purplle (10)
""")

st.divider()

st.subheader("Top Departments")

st.write("""
1. Makeup (54)

2. Skin (27)

3. Bath-and-body (9)
""")

st.divider()

st.subheader("Business Insights")

st.success("""
• CAM 2 is the busiest area.

• Makeup is the strongest department.

• Sales peak at 19:00.

• Consider allocating more staff near CAM 2.
""")