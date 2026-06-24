import csv 
import json  

compromised_users = []

# --- 1. Procesamiento e Ingesta del Reporte CSV ---
# Abre el archivo de credenciales y parsea las filas mapeando las columnas por sus encabezados
with open("passwords.csv") as password_file:
    password_csv = csv.DictReader(password_file)
    for password_row in password_csv:
        compromised_users.append(password_row["Username"])

# --- 2. Persistencia de Identificadores en Texto Plano ---
# Almacena de forma secuencial la lista de usuarios afectados
with open("compromised_users.txt", "w") as compromised_user_file:
    for compri_user in compromised_users:
        compromised_user_file.write(compri_user + "\n")

# --- 3. Generación y Exportación de Mensajería JSON ---
# Crea un diccionario de control de estado y lo serializa a un formato estructurado de red
with open("boss_message.json", "w") as boss_message:
    boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
    json.dump(boss_message_dict, boss_message)

# --- 4. Escritura de Firma Digital (ASCII Art) ---
# Variable que almacena el bloque de verificación del agente externo
slash_null_sig = """ _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __    ____  _  _ 
 ___   / ___)(  )    / _\  / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/"""

# Sobrescribe el archivo maestro inyectando la firma de validación
with open("new_password.csv", "w") as new_password_obj:
    new_password_obj.write(slash_null_sig)
