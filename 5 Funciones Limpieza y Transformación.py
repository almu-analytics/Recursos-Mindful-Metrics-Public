## FUNCIONES 

# 📂 1. Lectura de Datos
def cargar_datos(ruta, sep=","):
    """
    Carga un dataset desde un archivo CSV o similar.

    Parámetros:
    - ruta (str): Ruta del archivo a cargar.
    - sep (str): Separador de columnas. Por defecto es ','.

    Devuelve:
    - pd.DataFrame: DataFrame con los datos cargados.
    """
    import pandas as pd
    df = pd.read_csv(ruta, sep=sep)
    return df

# 🔍 2. Exploración General del Dataset
def explorar_dataset(df):
    """
    Realiza una exploración general del dataset.

    Parámetros:
    - df (pd.DataFrame): DataFrame a explorar.

    Devuelve:
    - dict: Diccionario con información básica sobre el dataset, incluyendo dimensiones, tipos de datos y valores nulos.
    """
    info = {
        "dimensiones": df.shape,
        "tipos_de_datos": df.dtypes.to_dict(),
        "valores_nulos": df.isnull().sum().to_dict()
    }
    return info

# 🔄 3. Transformación de Tipo de Datos y Estandarización de Nombres de Variables
def transformar_datos(df, columnas_a_cambiar, tipo):
    """
    Transforma el tipo de datos de columnas específicas y estandariza los nombres de las variables.

    Parámetros:
    - df (pd.DataFrame): DataFrame a transformar.
    - columnas_a_cambiar (list): Lista de columnas a cambiar de tipo.
    - tipo (str): Tipo al que se desea cambiar (por ejemplo, 'int', 'float', 'str').

    Devuelve:
    - pd.DataFrame: DataFrame transformado.
    """
    # Cambiar el tipo de datos
    for col in columnas_a_cambiar:
        df[col] = df[col].astype(tipo)
    
    # Estandarizar nombres de columnas
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    
    return df

# 📊 4. Estadísticas Básicas Variables Numéricas y Frecuencias Variables Categóricas
def estadisticas_basicas(df):
    """
    Calcula estadísticas básicas para variables numéricas y tablas de frecuencias para variables categóricas.

    Parámetros:
    - df (pd.DataFrame): DataFrame a analizar.

    Devuelve:
    - dict: Diccionario con estadísticas descriptivas para variables numéricas y tablas de frecuencias para variables categóricas.
    """
    estadisticas = {
        "numericas": df.describe().to_dict(),
        "categoricas": {col: df[col].value_counts().to_dict() for col in df.select_dtypes(include="object").columns}
    }
    return estadisticas

# 🧹 5. Limpieza y Transformación Dependiendo del Resultado Anterior
def limpiar_datos(df, columnas_a_eliminar=None, condiciones=None):
    """
    Realiza limpieza de datos basada en columnas a eliminar o condiciones específicas.

    Parámetros:
    - df (pd.DataFrame): DataFrame a limpiar.
    - columnas_a_eliminar (list, opcional): Lista de columnas a eliminar.
    - condiciones (dict, opcional): Diccionario de condiciones para filtrar filas.

    Devuelve:
    - pd.DataFrame: DataFrame limpio.
    """
    if columnas_a_eliminar:
        df = df.drop(columns=columnas_a_eliminar)
    
    if condiciones:
        for col, cond in condiciones.items():
            df = df[df[col] != cond]
    
    return df

# ❓ 6. Identificación y Gestión de Nulos
def gestionar_nulos(df, estrategia="media", columnas=None):
    """
    Gestiona los valores nulos en un DataFrame mediante diferentes estrategias.

    Parámetros:
    - df (pd.DataFrame): DataFrame a limpiar.
    - estrategia (str): Estrategia para gestionar nulos ('media', 'mediana', 'moda', 'eliminar').
    - columnas (list, opcional): Lista de columnas específicas a tratar.

    Devuelve:
    - pd.DataFrame: DataFrame con los nulos gestionados.
    """
    if columnas is None:
        columnas = df.columns

    for col in columnas:
        if estrategia == "media":
            df[col].fillna(df[col].mean(), inplace=True)
        elif estrategia == "mediana":
            df[col].fillna(df[col].median(), inplace=True)
        elif estrategia == "moda":
            df[col].fillna(df[col].mode()[0], inplace=True)
        elif estrategia == "eliminar":
            df.dropna(subset=[col], inplace=True)
    
    return df

# 🔍 7. Identificación y Gestión de Duplicados
def gestionar_duplicados(df, mantener="primero"):
    """
    Identifica y elimina duplicados en un DataFrame.

    Parámetros:
    - df (pd.DataFrame): DataFrame a procesar.
    - mantener (str): Indica qué duplicados conservar ('primero', 'último', 'ninguno').

    Devuelve:
    - pd.DataFrame: DataFrame sin duplicados.
    """
    df = df.drop_duplicates(keep=mantener)
    return df

## LLAMADA A FUNCIONES 

df = cargar_datos('https://raw.githubusercontent.com/data-bootcamp-v4/data/main/titanic_train.csv', sep=",")
explorar_dataset(df)


