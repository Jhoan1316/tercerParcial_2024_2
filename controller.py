import time
import sqlite3 as sql

def createDB():
    conn = sql.connect("autoconocimiento.db")
    print("base de datos autoconocimiento creada")
    conn.commit()
    conn.close()

def createTable():
    coon = sql.connect("autoconocimiento.db")
    cursor = coon.cursor()
    cursor.execute(""" CREATE TABLE progress_tracking (
    tracking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    experience_id INTEGER,
    experience_type TEXT,  -- 'growth' or 'contribution'
    milestone TEXT,
    completion_percentage INTEGER DEFAULT 0,
    notes TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (experience_id) REFERENCES growth_experiences(growth_id)
    );
    """)

    print("tabla creada")


    coon.commit()
    coon.close()

def insertRow(id_experiencia, tipo_experiencia, experiencia, porcentaje, notas):
    coon = sql.connect("autoconocimiento.db")
    cursor = coon.cursor()
    instruccion =  """
    INSERT INTO progress_tracking 
    (experience_id, experience_type, milestone, completion_percentage, notes) 
    VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(instruccion, (id_experiencia, tipo_experiencia, experiencia, porcentaje, notas))
    coon.commit()
    coon.close()

def readRows():
    coon = sql.connect("autoconocimiento.db")
    cursor = coon.cursor()
    instruccion =  f"SELECT * FROM progress_tracking"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    coon.commit()
    coon.close()
    print(datos)
def insertRows(progress_trackingList):
    coon = sql.connect("autoconocimiento.db")
    cursor = coon.cursor()
    instruccion = """
    INSERT INTO progress_tracking (experience_id, experience_type, milestone, completion_percentage, notes)
    VALUES (?, ?, ?, ?, ?)
    """
    for row in progress_trackingList:
        try:
            cursor.execute(instruccion, row)  # Ejecutar el INSERT para cada fila
        except Exception as e:
            print(f"Error al insertar la fila {row}: {e}")
    
    coon.commit()
    coon.close()
    
def Buscar():
    coon = sql.connect("autoconocimiento.db")
    cursor = coon.cursor()
    instruccion =  f"SELECT * FROM progress_tracking WHERE experience_id = 1234"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    coon.commit()
    coon.close()
    print(datos)

if __name__ == "__main__":
    #createDB()
    #createTable()
    #insertRow(1234,"growth", "buena app", 50, "bien")
    #readRows()
    #Buscar()
    # progress_tracking = [
    #     (987,'contribution', 'mala app',30,'mal'),
    #     (567,'contribution', 'exelente app',90,'bien'),
    #     (678,'contribution', 'buenisima app',30,'buenisisma')
    # ]
    # insertRows(progress_tracking)
    pass