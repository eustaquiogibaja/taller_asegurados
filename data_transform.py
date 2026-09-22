import pandas as pd

# Ruta del archivo CSV intermedio
archivo_csv = 'clientes_2026.csv'

try:
    # Leer el archivo CSV
    data = pd.read_csv(archivo_csv)
    

    
    # Exportar a Excel
    archivo_excel = 'clientes_ordenados.xlsx'
    data_ordenada.to_excel(archivo_excel, index=False)
    
    # Regla 3
    // reemplazar valores ('null','','  ','ninguno') = '0' , de la variable edad.
    
    # Regla 4
    // reemplazar valores ('null','','  ','ninguno') = '0' , de la variable tipo seguro.
    
    print(f"Datos exportados exitosamente a {archivo_excel}")
except Exception as e:
    print(f"Error al transformar los datos: {e}")