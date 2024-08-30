import pandas as pd

def descriptive_statistics(df, headline_column, publisher_column, date_column):
    # Headline length statistics
    df['headline_length'] = df[headline_column].apply(len)
    headline_stats = df['headline_length'].describe()

    # Articles per publisher
    articles_per_publisher = df[publisher_column].value_counts()

    # Trend over time
    df[date_column] = pd.to_datetime(df[date_column])
    trend_over_time = df.groupby(df[date_column].dt.date).size()

    return {
        "headline_stats": headline_stats,
        "articles_per_publisher": articles_per_publisher,
        "trend_over_time": trend_over_time
    }
