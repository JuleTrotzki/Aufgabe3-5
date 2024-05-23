import streamlit as st
import pandas as pd
from read_pandas_jule import (
    read_activity_csv, 
    compute_power_statistics, 
    plot_pow_HR, 
    add_HR_zones, 
    compute_time_in_zones, 
    compute_power_in_zones
)

st.header("Auswertung von Leistung und Herzfrequenz")

df = read_activity_csv()

# Manuelle Eingabe der maximalen Herzfrequenz
p_mean, p_max, hr_max = compute_power_statistics(df)
hr_max_input = st.number_input("Gib die maximale Herzfrequenz ein:", min_value=1, max_value=300, value=int(hr_max))

# Herzfrequenzzonen hinzufügen
df = add_HR_zones(df, hr_max_input)

# Zeit in Herzfrequenzzonen berechnen
time_in_zones = compute_time_in_zones(df)
time_df = pd.DataFrame.from_dict(time_in_zones, orient = 'index', columns = ['Zeit (s)'])
st.write("Zeit pro Zone:")
st.write(time_df)

# Durchschnittliche Leistung in Herzfrequenzzonen berechnen
power_in_zones = compute_power_in_zones(df)
power_df = pd.DataFrame.from_dict(power_in_zones, orient = 'index', columns = ['Leistung (W)'])
st.write("Leistung pro Zone:")
st.write(power_df)

# Plot von Leistung und Herzfrequenz über die Zeit anzeigen
fig = plot_pow_HR(df)
st.plotly_chart(fig)