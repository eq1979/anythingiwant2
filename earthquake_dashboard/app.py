import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Global Earthquake Dashboard", layout="wide")

st.title("🌎 Global Earthquake Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file with earthquake data", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(df.head(50))

    st.subheader("Earthquake Locations Map")
    fig = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        color="mag",
        size="mag",
        hover_name="place",
        hover_data=["time", "depth"],
        color_continuous_scale=px.colors.cyclical.IceFire,
        size_max=15,
        zoom=1,
        height=600,
        mapbox_style="carto-positron"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Magnitude Distribution")
    fig2 = px.histogram(df, x="mag", nbins=30, title="Distribution of Earthquake Magnitudes")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Top 10 Strongest Earthquakes")
    st.dataframe(df.sort_values(by="mag", ascending=False).head(10))

else:
    st.info("Please upload a CSV file to begin.")