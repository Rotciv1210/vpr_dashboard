
import sqlite3
import pandas as pd
import streamlit as st

st.title("Ventas por tienda")

conn = sqlite3.connect("datos/test.db")

query = """
SELECT
    st.store_name,
    SUM(s.quantity * s.price) AS total_ventas
FROM sales_uuid s
INNER JOIN stores_uuid st
    ON s.store_id = st.store_id
GROUP BY st.store_name;
"""

df = pd.read_sql_query(query, conn)

st.dataframe(df, use_container_width=True)

conn.close()
