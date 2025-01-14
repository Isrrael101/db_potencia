import mysql.connector
import random

# Configuración de la conexión a MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '654321',
    'database': 'potencia'
}

def crear_base_datos():
    # Conectar al servidor MySQL
    conn = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password']
    )
    cursor = conn.cursor()
    
    # Crear base de datos si no existe
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_config['database']}")
    cursor.execute(f"USE {db_config['database']}")
    
    # Crear tabla
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mediciones_electricas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            voltage FLOAT,
            corriente FLOAT,
            potencia FLOAT
        )
    """)
    
    # Generar 1000 registros
    for _ in range(1000):
        voltage = round(random.uniform(118, 225), 2)
        corriente = round(random.uniform(30, 40), 2)
        potencia = round(voltage * corriente, 2)
        
        cursor.execute("""
            INSERT INTO mediciones_electricas (voltage, corriente, potencia)
            VALUES (%s, %s, %s)
        """, (voltage, corriente, potencia))
    
    # Confirmar cambios
    conn.commit()
    
    # Mostrar algunos registros de ejemplo
    cursor.execute("SELECT * FROM mediciones_electricas LIMIT 5")
    print("\nPrimeros 5 registros generados:")
    for registro in cursor.fetchall():
        print(f"ID: {registro[0]}, Voltage: {registro[1]}V, Corriente: {registro[2]}A, Potencia: {registro[3]}W")
    
    # Calcular y mostrar promedios
    cursor.execute("""
        SELECT 
            AVG(voltage) as voltage_promedio,
            AVG(corriente) as corriente_promedio,
            AVG(potencia) as potencia_promedio
        FROM mediciones_electricas
    """)
    promedios = cursor.fetchone()
    print("\nPromedios:")
    print(f"Voltage promedio: {promedios[0]:.2f} V")
    print(f"Corriente promedio: {promedios[1]:.2f} A")
    print(f"Potencia promedio: {promedios[2]:.2f} W")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    print("Generando datos...")
    crear_base_datos()
    print("\n¡Datos generados exitosamente!")