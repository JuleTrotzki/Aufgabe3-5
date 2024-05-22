# %%

# Paket für Bearbeitung von Tabellen
import pandas as pd

# Paket
## zuvor !pip install plotly
## ggf. auch !pip install nbformat
import plotly.express as px
import plotly.graph_objects as go


def read_my_csv():
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df = pd.read_csv("data/ekg_data/01_Ruhe.txt", sep="\t", header=None)

    # Setzt die Columnnames im Dataframe
    df.columns = ["Messwerte in mV","Zeit in ms"]
    
    # Gibt den geladen Dataframe zurück
    return df


# %%
def read_activity_csv():
    path = 'data/activities/activity.csv'
    df = pd.read_csv(path)
    df['time'] = df['Duration'].cumsum()
    return df

def compute_power_statistics(df):
    p_mean = df['PowerOriginal'].mean()
    p_max = df['PowerOriginal'].max()
    hr_max = df['HeartRate'].max()
 
    return p_mean, p_max, hr_max

def plot_pow_HR(df):
    fig = px.line(df, x= "time", y="PowerOriginal")
    fig.add_trace(go.Scatter(x=df['time'], y=df['HeartRate'], mode='lines', name='Herzfrequenz'))
    return fig


def add_HR_zones(df):
    zone1_min = 0,50 * hr_max
    zone1_max = 0.60 * hr_max
    zone2_min = 0.60 * hr_max
    zone2_max = 0.70 * hr_max
    zone3_min = 0.70 * hr_max
    zone3_max = 0.80 * hr_max
    zone4_min = 0.80 * hr_max
    zone4_max = 0.90 * hr_max
    zone5_min = 0.90 * hr_max
    zone5_max = 1,00 * hr_max
    
    df['zone 1'] = df['Heartrate'] > zone1_min and df['Heartrate'] < zone1_max
    df['zone 2'] = df['Heartrate'] > zone2_min and df['Heartrate'] < zone2_max
    df['zone 3'] = df['Heartrate'] > zone3_min and df['Heartrate'] < zone3_max
    df['zone 4'] = df['Heartrate'] > zone4_min and df['Heartrate'] < zone4_max
    df['zone 5'] = df['Heartrate'] > zone5_min and df['Heartrate'] < zone5_max
    
    
    return df

#def compute_power_in_zones(df):
    #return [p_1. p_2, ...]
    
    
def make_plot(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df.head(2000), x= "Zeit in ms", y="Messwerte in mV")
    return fig

#%% Test

#df = read_my_csv()
#fig = make_plot(df)

#fig.show()

# %%
if __name__ == "__main__": 
    df = read_activity_csv()
    print(df.head())
    p_mean, p_max, hr_max = compute_power_statistics(df)
    print("p_mean:", p_mean)
    print("p_max:", p_max)
    print("hr_max:", hr_max)
    fig = plot_pow_HR(df)
    fig.show()