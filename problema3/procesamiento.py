import pandas as pd

def limpiar_columnas(df):
    # Renombrar columnas
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    
    # Eliminar columnas repetidas
    df = df.loc[:, ~df.columns.duplicated()]
    
    # Eliminar coma de la columna 'dispositivo_legal'
    df['dispositivo_legal'] = df['dispositivo_legal'].str.replace(',', '')

    return df

def dolarizar_montos(df, tasa_cambio):
    df['monto_inversion_dolares'] = df['monto_inversion'] / tasa_cambio
    df['monto_transferencia_dolares'] = df['monto_transferencia'] / tasa_cambio

    return df

def mapear_estado(df):
    estado_mapping = {
        'Actos Previos': 1,
        'Resuelto': 0,
        'Ejecucion': 2,
        'Concluido': 3
    }
    df['estado_puntuado'] = df['estado'].map(estado_mapping)

    return df