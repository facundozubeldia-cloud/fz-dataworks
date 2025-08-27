import time
import sys
import statistics
import os
import json
import pandas as pd
###
CANTIDAD_DE_VUELTAS = 52
pilotos = [ "Alexander Albon",
             "Carlos Sainz",
             "Charles Leclerc",
             "Esteban Ocon",
             "Fernando Alonso",
             "Gabriel Bortoleto",
             "George Russell",
             "Isack Hadjar",
             "Jack Doohan",
             "Kimi Antonelli",
             "Lance Stroll",
             "Lando Norris",
             "Lewis Hamilton",
             "Liam Lawson",
             "Max Verstappen",
             "Nico Hulkenberg",
             "Oliver Bearman",
             "Oscar Piastri",
             "Pierre Gasly",
             "Yuki Tsunoda"]


tiempos= [        [1417, 13, 86],
                  [1482, 13, 94],
                  [5408, 52, 81],
                  [ 708,  6, 79],
                  [ 222,  2,102],
                  [5355, 45, 93],
                  [4935, 47, 89],
                  [5616, 52, 98],
                  [5980, 52, 91],
                  [5512, 52, 85],
                  [3600, 30, 98],
                  [5304, 52, 90],
                  [5564, 52, 94],
                  [6084, 52, 87],
                  [5200, 52, 85],
                  [6032, 52, 91],
                  [5720, 52, 88],
                  [5356, 52, 87],
                  [5876, 52, 88],
                  [5824, 52, 92]      ]

pilotos_escuderias=[    
            "PIERRE GASLY"      ,	"ALPINE",		10,
            "JACK DOOHAN"       ,	"ALPINE",		7,
            "FERNANDO ALONSO"   ,	"ASTON MARTIN",	14,
            "LANCE STROLL"      ,	"ASTON MARTIN",	18,
            "LEWIS HAMILTON"    ,	"FERRARI",		44,
            "CHARLES LECLERC"   ,	"FERRARI",		16,
            "ESTEBAN OCON"      ,	"HAAS",			31,
            "OLIVER BEARMAN"    ,	"HAAS",			87,
            "NICO HULKENBERG"   ,	"KICK SAUBER",	27,
            "GABRIEL BORTOLETO" ,	"KICK SAUBER",	5,
            "LANDO NORRIS"      ,	"MCLAREN",		81,
            "OSCAR PIASTRI"     ,	"MCLAREN",		4,
            "GEORGE RUSSELL"    ,	"MERCEDES",		63,
            "KIMI ANTONELLI"    ,	"MERCEDES",		12,
            "LIAM LAWSON"       ,	"RACING BULL",	30,
            "ISACK HADJAR"      ,	"RACING BULL",	6,
            "MAX VERSTAPPEN"    ,	"RED BULL",		1,
            "YUKI TSUNODA"      ,	"RED BULL",		22,
            "CARLOS SAINZ"      ,	"WILLIAMS",		55,
            "ALEXANDER ALBON"   ,	"WILLIAMS",		23	]

aux =  "tiempo total en pista", "total de vueltas", "vuelta mas rapida"
########################################################################
def terminaron():
    pilotos_si_terminaron = []
    pilotos_no_terminaron = []
    print (f"📋 Lista de pilotos: {pilotos}")
    print (f"⏱️ Lista de tiempos: {tiempos}")
    print (f"📑 Lista de aux: {aux}")
    
    for piloto,(datos) in zip(pilotos,tiempos):
        print (f"""el piloto {piloto} tiene los siguientes datos :
        {aux[0]}= {datos[0]} 
        {aux[1]}= {datos[1]} vueltas completas 
        {aux[2]}= {datos[2]} segundos
        {"-"*100}
        """)
        if datos[1]== 52:
            pilotos_si_terminaron.append(piloto)
        else:
            pilotos_no_terminaron.append(piloto)
    return (pilotos_si_terminaron, pilotos_no_terminaron)

pilotos_si_terminaron, pilotos_no_terminaron = terminaron ()

print ("*"*100)
print (f"los pilotos que terminaron la carrera fueron :{pilotos_si_terminaron}")
print (f"los pilotos que no terminaron la carrera fueron :{pilotos_no_terminaron}")

########################################################################
dic_general=dict()
dic_escuderias={}
def estruc_dic():
    for piloto,(datos) in zip(pilotos,tiempos):
        
        
        indice     = pilotos_escuderias.index(piloto.upper())
        escuderia  = pilotos_escuderias[indice+1]
        numero     = pilotos_escuderias[indice+2]
        
        
        
        dic_general[piloto]= {
                                aux[0]          :   datos[0], 
                                aux[1]          :   datos[1], 
                                aux[2]          :   datos[2],
                                "Escuderia"     :   escuderia.title(),
                                "Numero"        :   numero,
                                "Puntos"        :   0
                                }
    print (f"{dic_general=}")
estruc_dic()
########################################################################
def ver_datos_dic(**dic):
    for clave, valor in dic.items():
        print(f"📌 {clave}") 
        if isinstance(valor, dict):
            for sub_clave, sub_valor in valor.items():
                print (f"    ➤ {sub_clave.ljust(25)}:   {str(sub_valor).ljust(20)}     ({type(sub_valor).__name__})") 
        elif isinstance(valor, (list,tuple,set) ):
            for indice, sub_valor in enumerate(valor):
                print (f"    ➤ {indice}                 {str(sub_valor).ljust(20)}     ({type(sub_valor).__name__})")  
        else:
            print (f"{valor}") 
        print (f"{'-'*100} ") 
        

print ("*"*100)
ver_datos_dic(**dic_general)

########################################################################
def buscar_piloto_ganador(dic_general):
    menor = float("inf")
    piloto_ganador = None
    for piloto_nombre in dic_general.keys():
        if dic_general[piloto_nombre][aux[1]] == 52 and dic_general[piloto_nombre][aux[0]] < menor:
            
            menor = dic_general[piloto_nombre][aux[0]]
            piloto_ganador = piloto_nombre
    
    return piloto_ganador
piloto_ganador = buscar_piloto_ganador(dic_general)

print ("-"*100)
print (f"""
🥇 El piloto ganador es {piloto_ganador}
    🔁 {dic_general[piloto_ganador][aux[1]] =}
    ⚡ {dic_general[piloto_ganador][aux[2]] =}
    ️⏱️ {dic_general[piloto_ganador][aux[0]] =}
""")
print ("*"*100)

########################################################################
def buscar_pilotos_podio(dic_general,podio):
    for clave in podio.keys():
        menor = float("inf")
        for piloto_nombre, valor in dic_general.items():
            if valor ["total de vueltas"] ==52 \
                and valor["tiempo total en pista"] < menor \
                and piloto_nombre not in  podio.values():
                menor = valor["tiempo total en pista"]
                podio[clave] = piloto_nombre
    return 
podio= {
     "primer puesto" : "",
     "segundo puesto":"",
     "tercer puesto" :""
        }
    
buscar_pilotos_podio(dic_general,podio)

print("-" * 100)
print("🏆 P O D I O   F Ó R M U L A   1 - 2 0 2 5 🏆".center(100))
print("-" * 100)

for puesto, piloto in podio.items():
    datos = dic_general[piloto]
    print(f"""
🥇 {puesto.upper()}
    👤 Piloto:              {piloto}
    ⏱️ Tiempo total:        {datos['tiempo total en pista']} s
    ⚡ Vuelta más rápida:   {datos['vuelta mas rapida']} s
    🔁 Vueltas completadas: {datos['total de vueltas']}
    """)
print("-" * 100)

########################################################################
def buscar_pilotos_puntos(*puntos, **dic_general):
    puntos_por_orden_llegada = []
    for puntos_obtenidos in puntos:
        menor_tiempo_total_en_pista = float("inf")
        piloto_con_puntos = None
        
        for piloto in dic_general.keys():
            if (dic_general[piloto]['total de vueltas'] == 52 and
                dic_general[piloto]['tiempo total en pista'] < menor_tiempo_total_en_pista and
                piloto not in puntos_por_orden_llegada):
                
                menor_tiempo_total_en_pista = dic_general[piloto]['tiempo total en pista']
                piloto_con_puntos = piloto 
        
        if piloto_con_puntos:
            puntos_por_orden_llegada.append(piloto_con_puntos)
            dic_general[piloto_con_puntos]["Puntos"] += puntos_obtenidos
            
    return puntos_por_orden_llegada
    dic_puntos = dict(fromkeys(puntos))

puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
puntos_por_orden_llegada = buscar_pilotos_puntos(*puntos, **dic_general)

print("-" * 100)
print("🏁  RESULTADO FINAL DEL GRAN PREMIO 🏁\n")
for index, (puntos, piloto) in enumerate(zip(puntos, puntos_por_orden_llegada)):
    print(f"Piloto en {index + 1} lugar con {puntos} puntos = {piloto}\n{dic_general[piloto]}\n")
print ("-"*50)
print(f"{puntos_por_orden_llegada=}")
print(f"{dic_general=}")
print ("-"*50)

ver_datos_dic(**dic_general)

print("*"*100)

########################################################################
def vuelta_mas_rapida( **dic_general):
    vuelta_rapida_menor = float("inf")
    piloto_vuelta_rapida = None
    for piloto in dic_general.keys():
        if dic_general[piloto]['vuelta mas rapida'] < vuelta_rapida_menor \
        and piloto in puntos_por_orden_llegada[:10]:
            vuelta_rapida_menor = dic_general[piloto]['vuelta mas rapida']
            piloto_mas_rapido = piloto
    if piloto_mas_rapido:
        return piloto_mas_rapido
    else:
        return "No se consiguie la vuelta mas rápida dentro de los 10 primeros"

piloto_mas_rapido=vuelta_mas_rapida( **dic_general)
print(f'''{"-" * 100}
    ⚡ El piloto más rápido de la carrera fue: {piloto_mas_rapido}
    🕒 En su vuelta más rápida tardó: {dic_general[piloto_mas_rapido]["vuelta mas rapida"]} segundos
    🔁 Total de vueltas: {dic_general[piloto_mas_rapido]["total de vueltas"]}
    ⏱️ Tiempo total en pista: {dic_general[piloto_mas_rapido]["tiempo total en pista"]}
{"-"*100}''')
print ("-"*100)
########################################################################

tiempos_totales = [
    datos["tiempo total en pista"]
    for datos in dic_general.values()
    if datos["total de vueltas"] == CANTIDAD_DE_VUELTAS
]

print("📊 Medidas estadísticas de tiempo total (pilotos que terminaron):")
print(f"  • Count : {len(tiempos_totales)}")
print(f"  • Mean  : {statistics.mean(tiempos_totales):.2f} s")
print(f"  • Median: {statistics.median(tiempos_totales):.2f} s")
print(f"  • Min   : {min(tiempos_totales)} s")
print(f"  • Max   : {max(tiempos_totales)} s")
print(f"  • Std   : {statistics.pstdev(tiempos_totales):.2f} s")


def sumar_puntos_por_escuderia(dic_general):
    dic_escuderia = {}

    for piloto, datos in dic_general.items():
        escuderia = datos['Escuderia']
        puntos = datos['Puntos']

        if escuderia not in dic_escuderia.keys():
            dic_escuderia[escuderia] = puntos
        else:
            dic_escuderia[escuderia] += puntos

    return dic_escuderia

dic_escuderia = sumar_puntos_por_escuderia(dic_general)
print("⭐" * 50)
for escuderia, puntos in dic_escuderia.items():
    print(f"Escudería: {escuderia}, Puntos Totales: {puntos}")
print("⭐" * 50) 
########################################################################
def obtener_top_escuderias(dic_escuderia, n=3):
    lista_top = list(map(lambda item: item[0:2], sorted(dic_escuderia.items(), key=lambda x: x[1], reverse=True)))[:n]
    
    return lista_top

top_escuderias = obtener_top_escuderias(dic_escuderia)
print("\n" + "🏆" * 30)
print("🔥 TOP 3 ESCUDERÍAS 🔥")
print("🏆" * 30)
for escuderia, puntos in top_escuderias:
    print(f"Escudería: {escuderia}, Puntos Totales: {puntos}")

print("*" * 100)
########################################################################
try:
    from sqlalchemy import create_engine
except ImportError:
    import pip
    pip.main(['install', 'sqlalchemy'])
    from sqlalchemy import create_engine

# Exportar la vuelta mas rapida en formato Excel (XLSX)
df_rapidas = pd.DataFrame(
    [
        {"Piloto": piloto, "Vuelta Más Rápida (s)": datos["vuelta mas rapida"]}
        for piloto, datos in dic_general.items()
    ]
)
output_dir = r"C:\Github\fz-dataworks\data-analysis\escuderias-proyect"
excel_rapidas = os.path.join(output_dir, "vueltas_rapidas_por_piloto.xlsx")
df_rapidas.to_excel(excel_rapidas, index=False)
print(f"✅ Exportado Excel de vueltas más rápidas en: {excel_rapidas}")

# Guardar JSON
json_path = os.path.join('C:/GitHub/fz-dataworks/data-analysis/escuderias-proyect', 'podio_escuderias.json')
with open(json_path, 'w') as json_file:
    json.dump(dic_escuderia, json_file)

# Guardar el diccionario en formato Excel (XLSX)
df_escuderia = pd.DataFrame(list(dic_escuderia.items()), columns=['Escudería', 'Puntos Totales'])
excel_path = os.path.join('C:/GitHub/fz-dataworks/data-analysis/escuderias-proyect', 'podio_escuderias.xlsx')
df_escuderia.to_excel(excel_path, index=False)

# Guardar el diccionario en una base de datos SQLite
db_path = os.path.join('C:/GitHub/fz-dataworks/data-analysis/escuderias-proyect', 'podio_escuderias.db')
engine = create_engine(f'sqlite:///{db_path}')
df_escuderia.to_sql('escuderias', con=engine, if_exists='replace', index=False)

# Confirmación de los archivos guardados
print("Podio de escuderías guardado en JSON, Excel y BBDD.")
print("*" * 100) 
########################################################################
# Describe basico del dataframe
print(df_escuderia.describe())