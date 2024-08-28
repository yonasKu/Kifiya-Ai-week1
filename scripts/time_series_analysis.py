import pandas as pd
import matplotlib.pyplot as plt

def time_series_analysis(df, date_column):
    # Convert to datetime
    df[date_column] = pd.to_datetime(df[date_column])
    
    # Group by date and count articles
    df['date'] = df[date_column].dt.date
    publication_count = df.groupby('date').size()

    # Plot time series
    plt.figure(figsize=(10,6))
    publication_count.plot(title="Publication Frequency Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.show()

    return publication_count
