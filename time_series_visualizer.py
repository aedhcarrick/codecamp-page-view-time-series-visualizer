import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    df_line = df.copy()
    # Draw line plot
    # The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. 
    # The label on the x axis should be Date and the label on the y axis should be Page Views.   
    fig, ax = plt.subplots(figsize=(14,5))
    ax.plot(df_line.index, df_line['value'])
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Draw bar plot
    # Copy and modify data for monthly bar plot
    # It should show average daily page views for each month grouped by year. 
    # The legend should show month labels and have a title of Months. 
    # On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.
    df_bar = df.copy()
    df_bar = df_bar.groupby([df.index.year, df.index.month]).mean()
    df_bar.index.rename(['year', 'month'], inplace=True)
    df_bar = df_bar.reset_index()
    df_bar['month'] = pd.to_datetime(df_bar['month'], format='%m').dt.month_name()
    df_bar = df_bar.pivot(index='year',columns='month',values='value')
    df_bar = df_bar[['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']] 
#    plot = sns.catplot(x='year', y='value', hue='month', data=df_bar, 
#            kind='bar')  <-- don't work??
    fig, ax = plt.subplots(figsize=(14,5))
    df_bar.plot(ax=ax, kind='bar')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(loc='upper left')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
#    print(df_box)
    # Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png". 
    # These box plots should show how the values are distributed within a given year or month and how it compares over time. 
    # The title of the first chart should be Year-wise Box Plot (Trend) 
    # and the title of the second chart should be Month-wise Box Plot (Seasonality). 
    # Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly.
    fig, (ax1, ax2) = plt.subplots(1,2,figsize=(14,5))

    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(ax=ax1, x='year', y='value', data=df_box)

    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    sns.boxplot(ax=ax2, x='month', y='value', data=df_box, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
