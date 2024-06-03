import streamlit as st
import json
from person_jule import Person
from ekgdata_jule import EKGdata
import pandas as pd

# Laden der Personendaten
person_data = Person.load_person_data()
person_list = Person.get_person_list(person_data)

# Titel der App
st.title("EKG Data Analysis App")

# Auswahl der Person
selected_person_name = st.selectbox("Wähle eine Person aus:", person_list)
selected_person_data = Person.find_person_data_by_name(selected_person_name)

# Anzeige der Personendaten
if selected_person_data:
    person = Person(selected_person_data)
    st.write(f"Name: {person.firstname} {person.lastname}")
    st.write(f"Alter: {person.calc_age()} Jahre")
    st.write(f"Maximale Herzfrequenz: {person.calc_max_heart_rate()} bpm")

    # Auswahl des EKG-Tests
    ekg_test_list = [f"Test ID: {test['id']} - Datum: {test['date']}" for test in selected_person_data["ekg_tests"]]
    selected_ekg_test = st.selectbox("Wähle einen EKG-Test aus:", ekg_test_list)
    
    if selected_ekg_test:
        selected_test_id = int(selected_ekg_test.split()[2])
        ekg_test_data = EKGdata.load_by_id(selected_test_id)
        
        if ekg_test_data:
            ekg = EKGdata(ekg_test_data)
            st.write("EKG Daten:")
            st.dataframe(ekg.df.head())

            # Eingabe des Schwellenwerts für die Peaks
            threshold = st.slider("Wähle den Schwellenwert für die Peaks:", min_value=0, max_value=1000, value=300)
            
            # Berechnung der Peaks
            peaks = EKGdata.find_peaks(ekg.df['EKG in mV'], threshold)
            st.write(f"Gefundene Peaks: {len(peaks)}")
            
            # Berechnung der Herzfrequenz
            heart_rates_df = EKGdata.calculate_HR(peaks)
            st.write("Geschätzte Herzfrequenz:")
            st.dataframe(heart_rates_df)
            
            # Plot der EKG-Daten und Peaks
            st.write("EKG-Daten und Peaks:")
            start_index = st.number_input("Startindex:", min_value=0, max_value=len(ekg.df)-1, value=0)
            end_index = st.number_input("Endindex:", min_value=0, max_value=len(ekg.df), value=len(ekg.df))
            EKGdata.plot_time_series(ekg.df, peaks, start_index, end_index)
else:
    st.write("Keine Daten für die ausgewählte Person gefunden.")