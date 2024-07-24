import streamlit as st
import mysql.connector

# Mengambil informasi rahasia
# db_config = {
#     'user': st.secrets["mysql"]["user"],
#     'password': st.secrets["mysql"]["password"],
#     'host': st.secrets["mysql"]["host"],
#     'database': st.secrets["mysql"]["database"]
# }

db_config = {
    'user': "erop3494_tes",
    'password': "Uzo12345_!",
    'host': "erozz911.my.id",
    'database': "erop3494_prediksi_pengeboran"
}


# Membuat koneksi ke database
def get_connection():
    return mysql.connector.connect(**db_config)

# Query data
def query_data(query):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result



# Streamlit app
st.title('Data dari MySQL')

# Membuat input teks
input = st.text_input('Masukkan Nama Anda')

# Membuat tombol submit
if st.button('Submit'):
    data = query_data(input)
    st.write(data)