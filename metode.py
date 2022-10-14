import streamlit as st
import pandas as pd
from io import StringIO
import csv
import numpy as np

class SM():
    
    def Test():    
        uploaded_file1 = st.file_uploader("Choose a file csv",type=['csv'])
        if uploaded_file1 is not None:
            # To read file as bytes:
            bytes_data = uploaded_file1.getvalue()
            # st.write(bytes_data)

            # To convert to a string based IO:
            stringio = StringIO(uploaded_file1.getvalue().decode("utf-8"))
            # st.write(stringio)

            # To read file as string:
            # string_data = stringio.read()
            # st.write(string_data)

            # Can be used wherever a "file-like" object is accepted:
            dataframe1 = pd.read_csv(uploaded_file1)
            st.write(dataframe1)
            
            # data = pd.DataFrame(dataframe1)
            # st.write(data.tail(2).sum())
            
            col1, col2 = st.columns(2)
        
            peringkat_pertama = dataframe1[dataframe1.Rangking == dataframe1.Rangking.min()]
            data_delta = dataframe1.Rangking.min()
            data_values = peringkat_pertama.max()['Alternatif']
            col1.metric("Alternatif", str(data_values), int(data_delta))
            
            peringkat_terakhir = dataframe1[dataframe1.Rangking == dataframe1.Rangking.max()]
            data_delta = dataframe1.Rangking.max()
            data_values = peringkat_terakhir.max()['Alternatif']
            col2.metric("Alternatif", str(data_values), int(-data_delta))
    
            if uploaded_file1 is not None:
                uploaded_file2 = st.file_uploader("Choose a secound file csv",type=['csv'])
                if uploaded_file2 is not None:
                    # To read file as bytes:
                    bytes_data = uploaded_file2.getvalue()
                    # st.write(bytes_data)

                    # To convert to a string based IO:
                    stringio = StringIO(uploaded_file2.getvalue().decode("utf-8"))
                    # st.write(stringio)

                    # To read file as string:
                    # string_data = stringio.read()
                    # st.write(string_data)

                    # Can be used wherever a "file-like" object is accepted:
                    dataframe2 = pd.read_csv(uploaded_file2)
                    st.write(dataframe2)
                    
                    col1, col2 = st.columns(2)
        
                    peringkat_pertama = dataframe2[dataframe2.Rangking == dataframe2.Rangking.min()]
                    data_delta = dataframe2.Rangking.min()
                    data_values = peringkat_pertama.max()['Alternatif']
                    col1.metric("Alternatif", str(data_values), int(data_delta))
                    
                    peringkat_terakhir = dataframe2[dataframe2.Rangking == dataframe2.Rangking.max()]
                    data_delta = dataframe2.Rangking.max()
                    data_values = peringkat_terakhir.max()['Alternatif']
                    col2.metric("Alternatif", str(data_values), int(-data_delta))

                    # Spearman Coefficient (rs)
                    
                    st.subheader("Spearman Coefficient (rs)")
                    # st.table(dataframe2.Rangking.sum(2))
                    datam1 = dataframe1['Rangking']
                    datam2 = dataframe2['Rangking']
                    
                    pengurangan = datam1 - datam2
                    pangkat = pengurangan ** 2
                    sumdata = pangkat.sum()
                    jumlah_data = pangkat.count()
                    perkalian1 = 6 * sumdata
                    jumlah_data_pangkat = jumlah_data ** 2
                    jumlah_data_pangkat_kurang1 = jumlah_data_pangkat - 1
                    perkalian2 = jumlah_data * jumlah_data_pangkat_kurang1 
                    pembagian = perkalian1 / perkalian2
                                        
                    rs = 1 - pembagian
                     
                    # pangkat.columns = ['Spearman Coefficient (rs)']
                    # st.table(pangkat)
                                                                               
                    st.text("Data Spearman Coefficient")
                    st.text(rs)
                    
                    st.subheader("Weighted Spearman coefficient (rw)")
                    
                    jumlah_data1 = jumlah_data - datam1 + 1
                    jumlah_data2 = jumlah_data - datam2 + 1
                    perkalian_jumlah_data = pangkat * (jumlah_data1 + jumlah_data2)
                    sum_perkalian_jumlah_data = perkalian_jumlah_data.sum()
                    quadrat_jumlah_data = (jumlah_data ** 4) + (jumlah_data ** 3) - (jumlah_data ** 2) - (jumlah_data)
                    rw = 1 - ((6 * sum_perkalian_jumlah_data) / quadrat_jumlah_data)
                    
                    st.text(rw)
                    
                    st.subheader("WS Coefficient")

                    quadrat_data1 = float(2)**-datam1
                    Rxi_Ryi = pengurangan
                    kurang_Rxi = 1 - datam1
                    jumlah_data_kurang_Rxi = jumlah_data - datam1
                    menggabungkan_data = pd.DataFrame({'a': kurang_Rxi,
                                           'b': jumlah_data_kurang_Rxi})
                    maxx = menggabungkan_data.max(axis = 1)
                    pembagianws = Rxi_Ryi/maxx
                    data_qadrat_dikali_pembagianws = quadrat_data1 * pembagianws
                    sum_data_qadrat_dikali_pembagianws = data_qadrat_dikali_pembagianws.sum()                  
                    ws = 1 - sum_data_qadrat_dikali_pembagianws
                    
                    st.text(ws)
                    
                else:
                    st.text("Mohon pilih data csv")
                    
            
        else:
            st.text("Mohon pilih data csv")
        
        




            