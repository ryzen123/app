#menentukan library yang ingin digunakan
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#membuat sidebar
with st.sidebar:
    selected = option_menu(
        menu_title = "Menu",
        options = ["Jumlah Status Order", "Rerata permintaan sewa"],
    )

#gathering data dari berbagai data set
orders_file_path = "orders_dataset.csv"
orders_data = pd.read_csv(orders_file_path)

#orders_data_year = orders_data['order_purchase_timestamp']
#st.write(orders_data_year)


if selected == "Rerata permintaan sewa":
    st.header("Rata-rata permintaan sewa")

if selected == "Jumlah Status Order":
    tab1, tab2 = st.tabs(["Analisis 1", "Analisis 2"])
    with tab1:
        st.title("Proses Analisis Data")
        st.header("Nuri Hanang Prasetyo - 10122091")
        st.header("Data Gathering")
        st.write(orders_data)
        st.markdown("Menampilkan data set orders_dataset.csv, selanjutnya dari data set tersebut hanya menggunakan kolom tabel order_status.")
        display_status_order = orders_data["order_status"]
        st.write(display_status_order)
        st.header("Data Cleaning")
        st.markdown("Dalam data set tersebut, tidak terdapat nilai tidak valid dan duplikasi data.")
        st.title("E-Commerce Data Analysis")
        st.header("Jumlah Status Order Type")
        st.markdown("Dalam kasus ini memvisualisasikan data juga menghitung jumlah masing-masing dari setiap status order.   Bisa disimak bahwa jumlah status order yang paling tinggi, yakni status delivered sebesar 96478. Dan status order yang paling sedikit jumlah nya yaitu status order approved hanya sejumlah 2.")
        status = orders_data['order_status']
        rekapStatus = {}
        for s in status:
            if s in rekapStatus:
                rekapStatus[s] += 1
            else:
                rekapStatus[s] = 1

        jml = 0
        statusType = list(rekapStatus.keys())
        jumlah = list(rekapStatus.values())
        #jumlahStatus = jumlah.sum()
        #st.write(jumlahStatus)

        
        barPlot = plt.bar(statusType, jumlah,color='darkcyan', align='center',)

        delivered_count = rekapStatus.get('delivered', 0)
        cancelled_count = rekapStatus.get('canceled', 0)
        invoiced_count = rekapStatus.get('invoiced', 0)
        shipped_count = rekapStatus.get('shipped', 0)
        processing_count = rekapStatus.get('processing', 0)
        unavailable_count = rekapStatus.get('unavailable', 0)
        created_count = rekapStatus.get('created', 0)
        approved_count = rekapStatus.get('approved', 0)

        totalStatus = delivered_count + cancelled_count + invoiced_count + shipped_count + processing_count + unavailable_count + created_count + approved_count

        #Memvisualisasikan menjadi bar chart
        plt.title('Jumlah Status Order')
        plt.ylabel('Jumlah Status')
        plt.xlabel('Tipe Status Order')
        plt.xticks(rotation=60)
        plt.xticks(statusType)
        plt.bar_label(barPlot, labels = jumlah, label_type = 'edge')
        st.pyplot(plt)
        
        rekapStatus_df = pd.DataFrame({'Status' : rekapStatus.keys, 'Jumlah' : [rekapStatus.values]})
        st.dataframe(data=rekapStatus, width=500)

        st.header("Presentase delivered")
        st.markdown("Dengan menggunakn rumus berikut :")
        st.latex(r'Persentase\ delivered = \frac{Persentase\ delivered}{Persentase\ delivered + Persentase\ cancelled} \times 100')
        presentase_delivered = round((delivered_count / (delivered_count + cancelled_count)) * 100, 1)
        st.markdown(f"Maka perbandingan presentase status delivered dengan status presentase cancelled adalah")
        st.write(presentase_delivered)

        st.header("Kesimpulan")
        with st.expander("Lebih lanjut"):
            st.markdown("Menghitung jumlah status order dari masing masing jenis order, setelah mendapatkan hasil nya lalu dimasukan kedalam dictionary. Setelah itu, dalam dictionary terdapat value dan keys. value yaitu jumlah dari masing masing status order sedangkan keys maka jenis dari status order itu sendiri. lalu divisualisasikan dengan bar chart.")
            with tab2:
                st.markdown("")