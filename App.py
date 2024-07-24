import streamlit as st
import mysql.connector

# Mengambil informasi rahasia
db_config = {
    'user': st.secrets["mysql"]["user"],
    'password': st.secrets["mysql"]["password"],
    'host': st.secrets["mysql"]["host"],
    'database': st.secrets["mysql"]["database"]
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

query = "SELECT * FROM well_a limit 10"  # Ganti dengan query yang sesuai
data = query_data(query)
st.write(data)