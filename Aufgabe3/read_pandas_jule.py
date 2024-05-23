# %%

# Paket für Bearbeitung von Tabellen
import pandas as pd

# Paket
## zuvor !pip install plotly
## ggf. auch !pip install nbformat
import plotly.express as px
import plotly.graph_objects as go




# %%

# Daten einlesen
def read_activity_csv():
    path = 'C:/code/programmieruebung2/Aufgabe3-5/data/activities/activity.csv'
    df = pd.read_csv(path)
    df['time'] = df['Duration'].cumsum()
    
    return df


# Wichtige Werte ermitteln
def compute_power_statistics(df):
    p_mean = df['PowerOriginal'].mean()
    p_max = df['PowerOriginal'].max()
    hr_max = df['HeartRate'].max()
 
    return p_mean, p_max, hr_max

# Plot erstellen
def plot_pow_HR(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['time'], y=df['PowerOriginal'], mode='lines', name='Leistung'))
    fig.add_trace(go.Scatter(x=df['time'], y=df['HeartRate'], mode='lines', name='Herzfrequenz', yaxis='y2'))

    fig.update_layout(
        title='Leistung und Herzfrequenz über die Zeit',
        xaxis=dict(title='Zeit (s)'),
        yaxis=dict(title='Leistung [W]'),
        yaxis2=dict(title='Herzfrequenz [bpm]', overlaying='y', side='right'))

    return fig


# HeartRate in Zonen einteilen
def add_HR_zones(df, hr_max):
    zone1_min = 0.50 * hr_max
    zone1_max = 0.60 * hr_max
    zone2_min = 0.60 * hr_max
    zone2_max = 0.70 * hr_max
    zone3_min = 0.70 * hr_max
    zone3_max = 0.80 * hr_max
    zone4_min = 0.80 * hr_max
    zone4_max = 0.90 * hr_max
    zone5_min = 0.90 * hr_max
    zone5_max = 1.00 * hr_max
    
    df['zone 1'] = (df['HeartRate'] > zone1_min) & (df['HeartRate'] < zone1_max)
    df['zone 2'] = (df['HeartRate'] > zone2_min) & (df['HeartRate'] < zone2_max)
    df['zone 3'] = (df['HeartRate'] > zone3_min) & (df['HeartRate'] < zone3_max)
    df['zone 4'] = (df['HeartRate'] > zone4_min) & (df['HeartRate'] < zone4_max)
    df['zone 5'] = (df['HeartRate'] > zone5_min) & (df['HeartRate'] < zone5_max)
    
    return df


# Zeit pro Zone ermitteln
def compute_time_in_zones(df):
    time_in_zones = {}
    time_in_zones['zone 1'] = df.loc[df['zone 1'], 'Duration'].sum()
    time_in_zones['zone 2'] = df.loc[df['zone 2'], 'Duration'].sum()
    time_in_zones['zone 3'] = df.loc[df['zone 3'], 'Duration'].sum()
    time_in_zones['zone 4'] = df.loc[df['zone 4'], 'Duration'].sum()
    time_in_zones['zone 5'] = df.loc[df['zone 5'], 'Duration'].sum()
    
    return time_in_zones


# Durchschnittliche Leistung pro Zone
def compute_power_in_zones(df):
    power_in_zones = {}
    power_in_zones['zone 1'] = df.loc[df['zone 1'], 'PowerOriginal'].mean()
    power_in_zones['zone 2'] = df.loc[df['zone 2'], 'PowerOriginal'].mean()
    power_in_zones['zone 3'] = df.loc[df['zone 3'], 'PowerOriginal'].mean()
    power_in_zones['zone 4'] = df.loc[df['zone 4'], 'PowerOriginal'].mean()
    power_in_zones['zone 5'] = df.loc[df['zone 5'], 'PowerOriginal'].mean()

    return power_in_zones


# %%
if __name__ == "__main__": 
    df = read_activity_csv()
    print(df.head())
    p_mean, p_max, hr_max = compute_power_statistics(df)
    print("p_mean:", p_mean)
    print("p_max:", p_max)
    print("hr_max:", hr_max)
    df = add_HR_zones(df, hr_max)
    time_in_zones = compute_time_in_zones(df)
    for zone, time in time_in_zones.items():
        print(f"Zeit in {zone}: {time} Sekunden")
    power_in_zones = compute_power_in_zones(df)
    for zone, power in power_in_zones.items():
        print(f"Durchschnittliche Leistung in {zone}: {power} Watt")
    fig = plot_pow_HR(df)
    fig.show()
