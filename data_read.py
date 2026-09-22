import pandas as pd

# Ruta del archivo TXT
archivo_excel = 'Asegurados.csv'

try:
    # Leer el archivo TXT
    data = pd.read_csv(archivo_txt, delimiter='|')
    
    # Guardar los datos en un archivo CSV temporal
    archivo_excel = 'asegurados.csv'
    data.to_csv(archivo_csv, index=False)
    
    print(f"Datos leídos y guardados en {archivo_csv}")
except Exception as e:
    print(f"Error al leer el archivo: {e}")
