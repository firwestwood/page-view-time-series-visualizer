import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Import the data
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Step 2: Clean the data by removing top and bottom 2.5%
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

# Step 3: Line Plot
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    return fig

# Step 4: Bar Plot
def draw_bar_plot():
    # Prepare data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month
    df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean().unstack()

    fig = df_bar.plot(kind='bar', figsize=(12, 6)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    return fig

# Step 5: Box Plot
def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = df_box['date'].dt.year
    df_box['Month'] = df_box['date'].dt.month_name()

    # Draw box plots
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Year-wise Box Plot
    sns.boxplot(x='Year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise Box Plot
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    sns.boxplot(x='Month', y='value', data=df_box, order=month_order, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    return fig
