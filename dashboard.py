import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de estilo de gráficos
sns.set(style="whitegrid")

def load_data(file, sheet_name):
    """Cargar datos desde un archivo Excel."""
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

    # Gráfico de Barras
    if st.sidebar.checkbox("Gráfico de Barras"):
        st.subheader("Gráfico de Barras")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=df[x_axis].astype(str), y=df[y_axis], ax=ax, palette="Blues_d")
        ax.set_xlabel(x_axis, fontsize=12)
        ax.set_ylabel(y_axis, fontsize=12)
        ax.set_title(f"Gráfico de Barras de {y_axis} vs {x_axis}", fontsize=14)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(fig)

    # Gráfico de Líneas
    if st.sidebar.checkbox("Gráfico de Líneas"):
        st.subheader("Gráfico de Líneas")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax, marker='o', color='b')
        ax.set_xlabel(x_axis, fontsize=12)
        ax.set_ylabel(y_axis, fontsize=12)
        ax.set_title(f"Gráfico de Líneas de {y_axis} vs {x_axis}", fontsize=14)
        plt.tight_layout()
        st.pyplot(fig)

    # Gráfico de Dispersión
    if st.sidebar.checkbox("Gráfico de Dispersión"):
        st.subheader("Gráfico de Dispersión")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax, color='r', edgecolor='k')
        ax.set_xlabel(x_axis, fontsize=12)
        ax.set_ylabel(y_axis, fontsize=12)
        ax.set_title(f"Gráfico de Dispersión de {y_axis} vs {x_axis}", fontsize=14)
        plt.tight_layout()
        st.pyplot(fig)

    # Histograma
    if st.sidebar.checkbox("Histograma"):
        st.subheader("Histograma")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(df[y_axis], bins=30, ax=ax, color='c', edgecolor='k')
        ax.set_xlabel(y_axis, fontsize=12)
        ax.set_ylabel('Frecuencia', fontsize=12)
        ax.set_title(f"Histograma de {y_axis}", fontsize=14)
        plt.tight_layout()
        st.pyplot(fig)

else:
    st.write("Por favor, carga un archivo de Excel.")
