import streamlit as st
from read_pandas_jule import (
    read_activity_csv, 
    compute_power_statistics, 
    plot_pow_HR, 
    add_HR_zones, 
    compute_time_in_zones, 
    compute_power_in_zones
)

# Power-Daten und Herzfrequenzzonen anzeigen
st.header("Power-Data")

# Power-Daten einlesen
df = read_activity_csv()

# Statistiken zu den Power-Daten berechnen
p_mean, p_max, hr_max = compute_power_statistics(df)
st.write("Durchschnittliche Leistung:", p_mean, "W")
st.write("Maximale Leistung:", p_max, "W")

# Manuelle Eingabe der maximalen Herzfrequenz
hr_max_input = st.number_input("Gib die maximale Herzfrequenz ein:", min_value=1, max_value=300, value=int(hr_max))

# Herzfrequenzzonen hinzufügen
df = add_HR_zones(df, hr_max_input)

# Zeit in Herzfrequenzzonen berechnen
time_in_zones = compute_time_in_zones(df)
for zone, time in time_in_zones.items():
    st.write(f"Zeit in {zone}: {time} Sekunden")

# Durchschnittliche Leistung in Herzfrequenzzonen berechnen
power_in_zones = compute_power_in_zones(df)
for zone, power in power_in_zones.items():
    st.write(f"Durchschnittliche Leistung in {zone}: {power} Watt")

# Plot von Leistung und Herzfrequenz über die Zeit anzeigen
fig = plot_pow_HR(df)
st.plotly_chart(fig)