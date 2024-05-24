import streamlit as st
from read_pandas import read_activity_csv, create_power_curve, plot_power_curve


st.title('Power Curve')

# Daten einlesen
df = read_activity_csv()

# Benutzereingabe für zeitliche Auflösung
resolution = st.slider("Select resolution (samples per second):", min_value=1, max_value=10, value=1)

# Power-Kurve erstellen
power_curve_df = create_power_curve(df, resolution)

# Plot der Power-Kurve
st.plotly_chart(plot_power_curve(power_curve_df), use_container_width=True)

# Optional: DataFrame anzeigen
st.write("Power Curve Data:")
st.write(power_curve_df)