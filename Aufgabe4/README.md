# Aufgabe 4 - Powercurve

## 

Dieses Programm ermöglicht die Analyse von Leistungsdaten aus einer CSV-Datei. Es bietet Funktionen zur Visualisierung von Daten und zur Anzeige von Leistungsinformationen über die Zeit.

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

Wähle die zeitliche Auflösung deiner Daten aus.

Das Programm zeigt eine interaktive Power Curve Visualisierung sowie eine Tabelle mit den Zeit- und Leistungsinformationen an.

![](/Screenshot_Powercurve1.png)
![](/Screenshot_Powercurve2.png)