# Proyecto Python: Entrada/Salida (I/O) y Manipulación de Sistemas de Archivos Multiformato

Este repositorio contiene un proyecto práctico desarrollado en Python enfocado en el manejo avanzado de flujos de entrada y salida (Input/Output). El script implementa procesos automatizados para la lectura y parseo de registros tabulares complejos (`CSV`), la generación dinámica de objetos de intercambio de información estructurada (`JSON`), y la persistencia de datos crudos sobre archivos de texto plano (`TXT`), simulando una auditoría lógica de control de accesos.

---

## Código Python del Proyecto

El programa lee un reporte de credenciales comprometidas, extrae los identificadores de usuario del sistema afectado, genera una notificación de estado cifrada y sobrescribe firmas digitales de validación:

```python
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

```

---

## Pipeline del Sistema de Archivos (Manejo de Formatos)

El script actúa como un puente de transformación entre múltiples estándares de la industria del software:

### 1. Entrada Tabular (`passwords.csv`)

La base de datos de origen organiza las columnas mediante delimitadores de comas, la cual es leída fila por fila por el objeto mapeador:

```csv
Username,Password
dev_user,secret123
linuxtroll,qwerty99

```

### 2. Salida de Serialización (`boss_message.json`)

La información procesada se empaqueta utilizando la sintaxis de objetos estándar de Javascript, garantizando la interoperabilidad con servicios web o APIs externas:

```json
{
  "recipient": "The Boss",
  "message": "Mission Success"
}

```

---

## Conceptos Técnicos Aplicados

* **Administradores de Contexto (`with open`)**: Estructura de control nativa de Python que garantiza una gestión segura de recursos. Asegura de forma automática el cierre físico del canal del archivo en el sistema operativo una vez que se sale del bloque, evitando fugas de memoria o corrupción de datos.
* **Clase `csv.DictReader**`: Objeto especializado que lee archivos delimitados transformando cada fila directamente en un diccionario ordenado de Python, donde las claves corresponden de forma exacta a los encabezados definidos en la primera línea del archivo.
* **Serialización mediante `json.dump()**`: Método que traduce un objeto nativo de Python (como un diccionario) a una cadena de texto plana bajo la especificación JSON estructurada, guardándola directamente en el flujo del archivo asignado.
* **Modos de Apertura (`r` vs `w`)**: El modo por defecto (`r`) asegura la lectura protegida sin riesgo de modificación, mientras que el modo de escritura (`w`) trunca o vacía por completo el archivo seleccionado antes de volcar las nuevas cadenas de caracteres.
