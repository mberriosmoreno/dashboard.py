import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data(file, sheet_name):
    return pd.read_excel(file, sheet_name=sheet_name)

st.title("Dashboard de Datos")

# Cargar archivo Excel
uploaded_file = st.sidebar.file_uploader("Cargar archivo Excel", type=["xlsx"])
if uploaded_file:
    xls = pd.ExcelFile(uploaded_file)
    sheet_names = xls.sheet_names
    selected_sheet = st.sidebar.selectbox("Selecciona la hoja", sheet_names)
    df = load_data(uploaded_file, selected_sheet)
    
    st.write(f"Datos de la hoja '{selected_sheet}':")
    st.dataframe(df)
    
    all_columns = df.columns.tolist()
    x_axis = st.sidebar.selectbox("Selecciona la columna para el eje X", all_columns)
    y_axis = st.sidebar.selectbox("Selecciona la columna para el eje Y", all_columns)
    
    if st.sidebar.checkbox("Gráfico de Barras"):
        st.subheader("Gráfico de Barras")
        fig, ax = plt.subplots(figsize=(10, 6))
        x_values = df[x_axis].astype(str)
        bars = ax.bar(x_values, df[y_axis], color='skyblue', edgecolor='black')
        
        # Añadir etiquetas de valor
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), va='bottom', ha='center', fontsize=10, color='black')
        
        ax.set_xlabel(x_axis, fontsize=12)
        ax.set_ylabel(y_axis, fontsize=12)
        ax.set_title(f"Gráfico de Barras de {y_axis} vs {x_axis}", fontsize=14)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(fig)
    
    if st.sidebar.checkbox("Gráfico de Líneas"):
        st.subheader("Gráfico de Líneas")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df[x_axis], df[y_axis], marker='o', color='b', linestyle='-', linewidth=2, markersize=6)
        ax.set_xlabel(x_axis, fontsize=12)
        ax.set_ylabel(y_axis, fontsize=12)
        ax.set_title(f"Gráfico de Líneas de {y_axis} vs {x_axis}", fontsize=14)
        plt.tight_layout()
        st.pyplot(fig)
    
    if st.sidebar.checkbox("Gráfico de Dispersión"):
        st.subheader("Gráfico de Dispersión")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(df[x_axis], df[y_axis], color='r', edgecolor='k', alpha=0.7)
        ax.set_xlabel(x_axis, fontsize=12)
        ax.set_ylabel(y_axis, fontsize=12)
        ax.set_title(f"Gráfico de Dispersión de {y_axis} vs {x_axis}", fontsize=14)
        plt.tight_layout()
        st.pyplot(fig)
    
    if st.sidebar.checkbox("Histograma"):
        st.subheader("Histograma")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(df[y_axis], bins=30, color='c', edgecolor='k')
        ax.set_xlabel(y_axis, fontsize=12)
        ax.set_ylabel('Frecuencia', fontsize=12)
        ax.set_title(f"Histograma de {y_axis}", fontsize=14)
        plt.tight_layout()
        st.pyplot(fig)
else:
    st.write("Por favor, carga un archivo de Excel.")
