# import library
import os
import pandas as pd
from datetime import date
from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.plotting import figure
from bokeh.models import Select, DateRangeSlider, Column, ColumnDataSource

# inisialisasi dataset
data = pd.DataFrame(pd.date_range(start="2000-01-01", end="2018-12-31"), columns=['date'])

# inisialisasi nama kolom data
cols = ["price", "open", "high", "low", "change"]

# load masing-masing dataset
for filename in os.listdir("./data"):

    # read data
    df = pd.read_csv(f"./data/{filename}")

    # ubah kolom date dari str menjadi datetime
    df["Date"] = pd.to_datetime(df.Date)

    # set index data ke date dan reindex data
    df.index = df.Date
    df = df.reindex(pd.date_range(start="2000-01-01", end="2018-12-31"), method="ffill")

    # ambil data sebelum tahun 2019 dan drop kolom yang tidak penting
    df = df[df.Date.apply(lambda x : x.year) <= 2018]
    df = df.reset_index(drop=True).drop(["Date", "Vol."], axis=1)

    # ubah tipe data variabel change menjadi float
    df["Change %"] = df["Change %"].str[:-1].astype("float")

    # ubah nama kolom data
    df.columns = [filename.split()[0].lower() + '_' +  col for col in cols]

    # gabung seluruh data saham
    data = pd.concat([data, df], axis=1)

    del(df)

# tranformasi data
source = ColumnDataSource(data={
    'x' : data.date,
    "y_aapl" : data.aapl_price,
    "y_intc" : data.intc_price,
    "y_msft" : data.msft_price,
})

# inisialisasi figure
p = figure(
        plot_width=1500, title="Stock Prices from 01-01-2000 to 31-12-2018",
        x_axis_label="date", y_axis_label="price", x_axis_type="datetime"
    )

# plot harga saham
p.line(source=source, x='x', y="y_aapl", legend_label="Apple", color="blue", line_width=2)
p.line(source=source, x='x', y="y_intc", legend_label="Intel", color="red", line_width=2)
p.line(source=source, x='x', y="y_msft", legend_label="Microsoft", color="green", line_width=2)

# fungsi callback
def update_plot(attr, old, new):
    
    # ambil tanggal awal dan akhir, dan variabel yang ingin di-plot
    start, end = pd.to_datetime(date_range_slider.value, unit="ms")
    y = var_select.value

    # ubah data lama menjadi data baru berdasarkan kondisi
    cond = (data.date >= start) & (data.date <= end)
    new_data = {
        'x' : data[cond].date,
        "y_aapl" : data[cond][f"aapl_{y}"],
        "y_intc" : data[cond][f"intc_{y}"],
        "y_msft" : data[cond][f"msft_{y}"]
    }
    source.data = new_data

    # ubah judul plot dan legend
    p.title.text = f"Stock {y.capitalize()}s from {start.strftime('%d-%m-%Y')} to {end.strftime('%d-%m-%Y')}"
    p.yaxis.axis_label = y

# buat slider untuk memilih tanggal
date_range_slider = DateRangeSlider(title="Date",
        value=(date(2000, 1, 1), date(2018, 12, 31)),
        start=date(2000, 1, 1), end=date(2018, 12, 31)
    )
date_range_slider.on_change("value", update_plot)

# buat slider untuk memilih variabel
var_select = Select(
    options=["price", "open", "high", "low", "change"],
    value="price", title="Variable"
)
var_select.on_change("value", update_plot)

# buat layout
layout = column(p, date_range_slider, var_select)
curdoc().add_root(layout)