# Aufgabe3-5 - Herzfrequenz- und Leistungsanalyse

## 

Dieses Programm ermöglicht die Analyse von Herzfrequenz- und Leistungsdaten aus einer CSV-Datei. Es bietet Funktionen zur Berechnung von Statistiken, zur Visualisierung von Daten und zur Anzeige von Zeit- und Leistungsinformationen in verschiedenen Herzfrequenzzonen.

## Installation
Klone das Repository auf deinem Computer, indem du einen Ordner erstellst und mit cd "dein Speicherort" in diesen navigierst. 
Klone das Repository in Git Bash mit git clone https://github.com/JuleTrotzki/Aufgabe3-5.git
Öffne nun deinen erstellten Ordner in Visual Studio Code.

## Einrichtung der virtuellen Umgebung

Zunächst müssen Sie die virtuelle Umgebung erstellen und aktivieren:
python -m venv .venv

Für Unix/Linux:
source venv/bin/activate

Für Windows:
.\.venv\Scripts\activate

## Abhängigkeiten installieren
Öffne eine Befehlszeile, navigiere zum Projektordner und führe den folgenden Befehl aus, um die erforderlichen Abhängigkeiten zu installieren:

pip install -r requirements.txt

## Verwendung
Öffne eine Befehlszeile, navigiere zum Projektordner und führe den folgenden Befehl aus, um das Programm auszuführen:

streamlit run main.py

Gib die maximale Herzfrequenz über das Eingabefeld ein und bestätige sie.

Analyse der Daten: Das Programm zeigt Statistiken zur Leistung, eine interaktive Visualisierung von Leistung und Herzfrequenz über die Zeit sowie Tabellen mit den Zeiten in den Herzfrequenzzonen und der durchschnittlichen Leistung in diesen Zonen an

![](/Screenshot_streamlit.png)
![](/Screenshot_streamlit2.png)