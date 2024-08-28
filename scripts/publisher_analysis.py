import pandas as pd

def publisher_analysis(df, publisher_column):
    # Count the number of articles per publisher
    publisher_counts = df[publisher_column].value_counts()

    # Extract domains from email addresses (if applicable)
    if "@" in publisher_column:
        df['domain'] = df[publisher_column].apply(lambda x: x.split('@')[-1])
        domain_counts = df['domain'].value_counts()
    else:
        domain_counts = None
    
    return publisher_counts, domain_counts
