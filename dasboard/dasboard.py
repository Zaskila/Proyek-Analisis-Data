import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.header(' Dashboard Penyewaan Sepeda :sparkles:')

    

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("download.png")
    
    filtermusim = st.checkbox ("musim", value=True) #grouping by season
    filtercuaca = st.checkbox ("cuaca", value=True) #grouping by cuaca
    filterjam = st.checkbox ("jam", value=True) #grouping by jam
    filterday = st.checkbox ("hari", value=True) #grouping by hari

#Import dataset
df_day = pd.read_csv('dasboard\day.csv')
df_day.head()

df_hours = pd.read_csv('dasboard\hour.csv')
df_hours.head()

# Menampilkan pernyataan 1 line chart
import streamlit as st
import matplotlib.pyplot as plt

if filtermusim:
    
    # Data yang akan diplot
    x = df_day.groupby(by="season").cnt.nunique().index
    y = df_day.groupby(by="season").cnt.nunique().values

    # Mengubah label y menjadi string yang diinginkan
    ylabel_mapping = {1: 'Springer', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    new_ylabel = [ylabel_mapping[label] for label in x]

    # Membuat plot diagram garis
    fig, ax = plt.subplots()
    ax.plot(new_ylabel, y)

    # Menambahkan label sumbu x dan y
    ax.set_xlabel("Musim")
    ax.set_ylabel("Tota Penyewaan")

    # Menambahkan judul plot
    ax.set_title("Pengaruh Penyewaan Berdasarkan Musim")

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig)


# diagram 2
if filtercuaca :
    # Data yang akan diplot
    x = df_day.groupby(by="weathersit").cnt.nunique().index
    y = df_day.groupby(by="weathersit").cnt.nunique().values

    # Mengubah label x menjadi string yang diinginkan
    xlabel_mapping = {1: 'Clear', 2: 'Mist', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Snow/Fog'}
    new_xlabel = [xlabel_mapping[label] for label in x]

    # Membuat plot diagram batang
    fig, ax = plt.subplots()
    ax.bar(new_xlabel, y)

    # Menambahkan label sumbu x dan y
    ax.set_xlabel("Cuaca")
    ax.set_ylabel("Total Penyewaan")

    # Menambahkan judul plot
    ax.set_title("Pengaruh Penyewaan Berdasarkan Cuaca")

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig)

#diagram 3

if filterjam :
    # Mengambil data jumlah penyewaan unik per jam
    hourly_rental_counts = df_hours.groupby(by="hr")['cnt'].nunique().sort_index()

    # Mengurutkan data berdasarkan jumlah penyewaan
    sorted_hourly_rental_counts = hourly_rental_counts.sort_values(ascending=False)

    # Mengambil 5 data dengan performa terbaik
    top_5_hours = sorted_hourly_rental_counts.head(5)

    # Mengambil 5 data dengan performa terendah
    bottom_5_hours = sorted_hourly_rental_counts.tail(5)

    # Membuat plot untuk 5 data dengan performa terbaik dan terendah
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Plot untuk top 5
    axes[0].bar(top_5_hours.index, top_5_hours.values)
    axes[0].set_xlabel("Jam")
    axes[0].set_ylabel("Total Penyewaan")
    axes[0].set_title("5 Jam Teratas dengan Penyewaan Sepeda Tertinggi")

    # Plot untuk bottom 5
    axes[1].bar(bottom_5_hours.index, bottom_5_hours.values)
    axes[1].set_xlabel("Jam")
    axes[1].set_ylabel("Total Penyewaan")
    axes[1].set_title("5 Jam Teratas dengan Penyewaan Sepeda Terendah")

    # Menyesuaikan layout
    plt.tight_layout()

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig)

#Diagram 4
import streamlit as st
import matplotlib.pyplot as plt

# Mengambil data jumlah penyewaan unik per hari
weekday_counts = df_day.groupby(by="weekday").cnt.nunique().sort_values(ascending=False)

# Membuat plot diagram batang
fig, ax = plt.subplots()
ax.bar(weekday_counts.index, weekday_counts.values)

# Menambahkan label sumbu x dan y
ax.set_xlabel("Hari Kerja")
ax.set_ylabel("Total Penyewaan")

# Menambahkan judul plot
ax.set_title("Pengaruh Penyewaan Berdasarkan Weekday")

# Menampilkan plot menggunakan Streamlit
st.pyplot(fig)





