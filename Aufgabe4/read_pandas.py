# %%
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from matplotlib.ticker import FuncFormatter

# %%
# Daten einlesen
def read_activity_csv():
    path = 'data/activities/activity.csv'
    df = pd.read_csv(path)
    df['time'] = df['Duration'].cumsum()
    
    return df


def find_best_effort(df, t_int, f_s):
    window_size = t_int * f_s
    rolling_mean = df['PowerOriginal'].rolling(window=window_size).mean()
    best_power = rolling_mean.max()
    
    return best_power
    
    
def create_power_curve(df, f_s):
   
    max_duration = len(df) // f_s  # Maximale Dauer in Sekunden
    durations = np.arange(1, max_duration + 1)  # Zeitintervalle in Sekunden
    
    power_curve = []
    
    for duration in durations:
        max_power = find_best_effort(df, duration, f_s)
        power_curve.append((duration, max_power))
    
    power_curve_df = pd.DataFrame(power_curve, columns=['Time (s)', 'Power (W)'])
    return power_curve_df

def format_time(x, _):
    if x < 60: 
        return f"{x:.0f} s"
    else:  
        return f"{x/60:.0f} min"

def plot_power_curve(power_curve_df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=power_curve_df['Time (s)'], y=power_curve_df['Power (W)'], name='Power Curve'))
    fig.update_layout(title='Power Curve',
                      xaxis_title='Time',
                      yaxis_title='Power (W)',
                      xaxis=dict(type='log', tickformat='g'))
    fig.update_xaxes(tickvals=[1, 2, 5, 10, 20, 30, 60, 120, 300, 600, 1200, 1800],
                     ticktext=["1s", "2s", "5s", "10s", "20s", "30s", "1min", "2min", "5min", "10min", "20min", "30min"])
                      
    return fig
    