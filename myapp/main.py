# -*- coding: utf-8 -*-
"""main.ipynb
## Tugas Besar - "Visualisasi Data Interaktif Fluktuasi Harga Saham"
"""

import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_file, output_notebook
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool
from bokeh.models.widgets import Tabs, Panel

# Membaca dataset dari stock market
df = pd.read_csv('data/data.csv', parse_dates=['Date'])

# Untuk menyimpan baris-baris tiap index di variabel hangseng, nasdaq dan nikkei
hangseng = df[df.Name == 'HANG SENG']
nasdaq = df[df.Name == 'NASDAQ']
nikkei = df[df.Name == 'NIKKEI']

# Untuk menampilkan source data hangseng, nasdaq, nikkei
source_hangseng = ColumnDataSource(data=hangseng)
source_nasdaq = ColumnDataSource(data=nasdaq)
source_nikkei = ColumnDataSource(data=nikkei)

source_hangseng1 = ColumnDataSource(data=hangseng)
source_nasdaq1 = ColumnDataSource(data=nasdaq)
source_nikkei1 = ColumnDataSource(data=nikkei)

source_hangseng2 = ColumnDataSource(data=hangseng)
source_nasdaq2 = ColumnDataSource(data=nasdaq)
source_nikkei2 = ColumnDataSource(data=nikkei)

"""## Level 1"""

# Menampilkan ke plot HTML
output_file('Level 1.html', title='Level 1')

# Membuat Figure untuk menampilkan adj close
fig1 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='Adj. Close',
    title='Adj. Close',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

# Untuk menampilkan line plot adj close dari Hangseng
a = fig1.line(
    x='Date',
    y='Adj Close',
    source=source_hangseng,
    color='blue',
    legend_label='Hang Seng'
)

# Untuk menampilkan line plot adj close dari Nasdaq
b = fig1.line(
    x='Date',
    y='Adj Close',
    source=source_nasdaq,
    color='red',
    legend_label='Nasdaq'
)

# Untuk menampilkan line plot adj close dari Nikkei
c = fig1.line(
    x='Date',
    y='Adj Close',
    source=source_nikkei,
    color='yellow',
    legend_label='Nikkei'
)

# Bokeh Library
tooltips = [
            ('Index','@Name'),
            ('Adj. Close', '$@{Adj Close}{0.2f}')
]

# Menambahkan HoverTool untuk membuat fig
fig1.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

# Visualisasi
show(fig1)

"""**Penjelasan Level 1**

Untuk kasus level 1 kita disuruh untuk menampilkan seluruh nilai close adj close untuk setiap index di pasar saham. Kita bisa lihat di dalam figure bahwa jika kita menempelkan kursor ke line plot tertentu akan menampilkan adj close baik untuk Hangseng, Nasdaq dan Nikkei pada tanggal tertentu.

## Level 2
"""

# Membuat Figure untuk menampilkan adj close
fig1 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='Adj. Close',
    title='Adj. Close',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

# Untuk menampilkan line plot adj close dari Hangseng
a = fig1.line(
    x='Date',
    y='Adj Close',
    source=source_hangseng1,
    color='blue',
    legend_label='Hang Seng'
)

# Untuk menampilkan line plot adj close dari Nasdaq
b = fig1.line(
    x='Date',
    y='Adj Close',
    source=source_nasdaq1,
    color='red',
    legend_label='Nasdaq'
)

# Untuk menampilkan line plot adj close dari Nikkei
c = fig1.line(
    x='Date',
    y='Adj Close',
    source=source_nikkei1,
    color='yellow',
    legend_label='Nikkei'
)

# Bokeh Library
tooltips = [
            ('Index','@Name'),
            ('Adj. Close', '$@{Adj Close}{0.2f}')
]

# Menambahkan HoverTool untuk membuat fig
fig1.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

# Membuat Figure untuk menampilkan volume
fig2 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='Volume',
    title='Volume',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

# Untuk menampilkan line plot Volume dari Hangseng
a = fig2.line(
    x='Date',
    y='Volume',
    source=source_hangseng1,
    color='blue',
    legend_label='Hang Seng'
)

# Untuk menampilkan line plot volume dari Nasdaq
b = fig2.line(
    x='Date',
    y='Volume',
    source=source_nasdaq1,
    color='red',
    legend_label='Nasdaq'
)

# Untuk menampilkan line plot volume dari Nikkei
c = fig2.line(
    x='Date',
    y='Volume',
    source=source_nikkei1,
    color='yellow',
    legend_label='Nikkei'
)

# Bokeh Library
tooltips = [
            ('Index','@Name'),
            ('Volume', '@Volume')
]

# Menambahkan HoverTool untuk membuat fig
fig2.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

# Membuat Figure untuk menampilkan day perc change
fig3 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='Day % Change',
    title='Day % Change',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

# Untuk menampilkan line plot day perc change dari Hangseng
a = fig3.line(
    x='Date',
    y='Day_Perc_Change',
    source=source_hangseng1,
    color='blue',
    legend_label='Hang Seng'
)

# Untuk menampilkan line plot day perc change dari Nasdaq
b = fig3.line(
    x='Date',
    y='Day_Perc_Change',
    source=source_nasdaq1,
    color='red',
    legend_label='Nasdaq'
)

# Untuk menampilkan line plot day perc change dari Nikkei
c = fig3.line(
    x='Date',
    y='Day_Perc_Change',
    source=source_nikkei1,
    color='yellow',
    legend_label='Nikkei'
)

# Bokeh Library
tooltips = [
            ('Index','@Name'),
            ('Day % Change', '@Day_Perc_Change')
]

# Menambahkan HoverTool untuk membuat fig
fig3.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

# Menampilkan ke plot HTML
output_file('Level 2.html', title='Level 2')

# Membuat tiga panel yaitu Adj Close,Volume,Day Perc Change
Adj_Close = Panel(
    child=fig1,
    title='Adj Close'
)
Volume = Panel(
    child=fig2,
    title='Volume'
)
Day_Perc_Change = Panel(
    child=fig3,
    title='Day % Change'
)

# Assign the panels to Tabs
tabs = Tabs(tabs=[
                  Adj_Close, Volume, Day_Perc_Change
                ])

# Show the tabbed layout
show(tabs)

"""**Penjelasan level 2**

Untuk level dua menambahkan aspek interaktif yang memungkinkan user untuk memilih parameter yang diinginkan. Parameternya adalah Adj Close, volume dan day_perc_volume dan jika ingin memilih salah satu dari paramater yang sudah disebutkan tadi tinggal mengklik saja dan akan menampilkan parameter yang diinginkan.

## Level 3
"""

# Membuat Figure untuk menampilkan adj close
fig1 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='Adj. Close',
    title='Adj. Close',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

# Untuk menampilkan line plot adj close dari Hangseng
a = fig1.line(
    x='Date',
    y='Adj Close',
    source=source_hangseng2,
    color='blue',
    legend_label='Hang Seng'
)

# Untuk menampilkan line plot adj close dari Nasdaq
b = fig1.line(
    x='Date',
    y='Adj Close',
    source=source_nasdaq2,
    color='red',
    legend_label='Nasdaq'
)

# Untuk menampilkan line plot adj close dari Nikkei
c = fig1.line(
    x='Date',
    y='Adj Close',
    source=source_nikkei2,
    color='yellow',
    legend_label='Nikkei'
)

# Bokeh Library
tooltips = [
            ('Index','@Name'),
            ('Adj. Close', '$@{Adj Close}{0.2f}')
]

# Menambahkan HoverTool untuk membuat fig
fig1.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

# Membuat Figure untuk menampilkan volume
fig2 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='Volume',
    title='Volume',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

# Untuk menampilkan line plot Volume dari Hangseng
a = fig2.line(
    x='Date',
    y='Volume',
    source=source_hangseng2,
    color='blue',
    legend_label='Hang Seng'
)

# Untuk menampilkan line plot volume dari Hangseng
b = fig2.line(
    x='Date',
    y='Volume',
    source=source_nasdaq2,
    color='red',
    legend_label='Nasdaq'
)

# Untuk menampilkan line plot volume dari Hangseng
c = fig2.line(
    x='Date',
    y='Volume',
    source=source_nikkei2,
    color='yellow',
    legend_label='Nikkei'
)

# Bokeh Library
tooltips = [
            ('Index','@Name'),
            ('Volume', '@Volume')
]

# Menambahkan HoverTool untuk membuat fig
fig2.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

# Membuat Figure untuk menampilkan day perc change
fig3 = figure(
    x_axis_type='datetime',
    x_axis_label='Date',
    y_axis_label='Day % Change',
    title='Day % Change',
    toolbar_location='below',
    plot_height=600,
    plot_width=800
)

# Untuk menampilkan line plot day perc change dari Hangseng
a = fig3.line(
    x='Date',
    y='Day_Perc_Change',
    source=source_hangseng2,
    color='blue',
    legend_label='Hang Seng'
)

# Untuk menampilkan line plot day perc change dari Nasdaq
b = fig3.line(
    x='Date',
    y='Day_Perc_Change',
    source=source_nasdaq2,
    color='red',
    legend_label='Nasdaq'
)

# Untuk menampilkan line plot day perc change dari Nikkei
c = fig3.line(
    x='Date',
    y='Day_Perc_Change',
    source=source_nikkei2,
    color='yellow',
    legend_label='Nikkei'
)

# Bokeh Library
tooltips = [
            ('Index','@Name'),
            ('Day % Change', '@Day_Perc_Change')
]

# Menambahkan HoverTool untuk membuat fig
fig3.add_tools(HoverTool(
    tooltips=tooltips,
    mode='vline'
))

# Menampilkan ke plot HTML
output_file('Level 3.html', title='Level 3')

fig1.legend.click_policy = 'hide'
fig2.legend.click_policy = 'hide'
fig3.legend.click_policy = 'hide'

# Membuat tiga panel yaitu Adj Close,Volume,Day Perc Change
Adj_Close = Panel(
    child=fig1,
    title='Adj Close'
)
Volume = Panel(
    child=fig2,
    title='Volume'
)
Day_Perc_Change = Panel(
    child=fig3,
    title='Day % Change'
)

tabs = Tabs(tabs=[
                  Adj_Close, Volume, Day_Perc_Change
                ])

show(tabs)

"""**Penjelasan level 3**

Untuk level tiga menambahkan aspek interaktif yang memungkinkan user untuk menyembunyikan data untuk indeks pasar saham tertentu dengan mengklik legend dari indeks yang ingin dipilih.
"""