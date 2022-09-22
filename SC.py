import streamlit as st
import pandas as pd

df = pd.read_csv (r'comet.csv')

mantap = pd.DataFrame (df, columns= ['Alternatif','Rangking'])

st.table(mantap)
# df = pd.DataFrame(
#    np.random.randn(50, 20),
#    columns=('col %d' % i for i in range(20)))

# st.dataframe(df)  # Same as st.write(df)