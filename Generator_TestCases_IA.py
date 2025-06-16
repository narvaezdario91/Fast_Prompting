import google.generativeai as genai
import os
import re

# --- Configuración del API de Gemini ---
# Asegúrate de configurar tu clave API de forma segura.
# Por ejemplo, como una variable de entorno.
# Puedes reemplazar `os.environ.get("GEMINI_API_KEY")` con tu clave directamente
# si es solo para pruebas locales y no para producción.
# Para el entorno de Canvas, la clave se inyectará automáticamente si se deja como string vacío.
API_KEY = "" # Deja esto como string vacío para que Canvas lo inyecte automáticamente

# Configurar el acceso a la API de Gemini
genai.configure(api_key=API_KEY)

# Inicializar el modelo Gemini
# Usamos 'gemini-2.0-flash' por ser el modelo recomendado para este tipo de tareas.
# Este modelo es eficiente para la generación de texto estructurado y rápido.
model = genai.GenerativeModel('gemini-2.0-flash')

# --- Función Auxiliar para Extracción de Gherkin ---
# Esta función ayuda a limpiar la salida del modelo, extrayendo solo el bloque de código Gherkin
# si el modelo incluye texto adicional antes o después.
def extract_gherkin(text):
    """
    Extrae el contenido de Gherkin delimitado por ```gherkin...```.
    Si no encuentra el delimitador, devuelve el texto original.
    """
    # Expresión regular para encontrar el bloque `gherkin`
    # re.DOTALL permite que el '.' coincida con saltos de línea
    match = re.search(r"```gherkin(.*?)```", text, re.DOTALL)
    if match:
        # Devuelve el contenido del primer grupo de captura (lo que está dentro del bloque)
        return match.group(1).strip()
    return text # Si no se encuentra el bloque, se devuelve el texto original

# --- Historias de Usuario de Ejemplo ---
# Aquí definimos varias Historias de Usuario para demostrar la versatilidad del prompting.
# Puedes reemplazar estas por las Historias de Usuario de tu Preentrega 1.

# Historia de Usuario 1: Caso simple
user_story_1 = "Como usuario registrado, quiero poder añadir productos al carrito de compras para poder comprarlos posteriormente."

# Historia de Usuario 2: Con más detalles y posibles casos de borde
user_story_2 = "Como administrador, quiero gestionar los usuarios del sistema para poder activar o desactivar sus cuentas."

# Historia de Usuario 3: Que implica múltiples roles o flujos
user_story_3 = "Como cliente de soporte, quiero enviar un ticket de ayuda y como agente de soporte, quiero poder responder a ese ticket."

# --- PROMPT V1: Básico y Directo ---
# Este prompt es una primera aproximación. Su objetivo es ver la respuesta por defecto del modelo
# sin muchas instrucciones explícitas sobre el formato o el rol.
print("=== DEMOSTRACIÓN DE FAST PROMPT CON GEMINI PARA GHERKIN ===")
print("\n--- PASO 1: PROMPT BÁSICO Y SU RESPUESTA ---")
print("Este prompt es simple y no especifica rol ni formato estricto.")

prompt_v1_template = """
Genera escenarios de prueba en formato Gherkin para la siguiente Historia de Usuario:

Historia de Usuario: {user_story}
"""

# Prueba con la primera Historia de Usuario
current_user_story = user_story_1
prompt_v1 = prompt_v1_template.format(user_story=current_user_story)

print(f"\nHistoria de Usuario: {current_user_story}")
print(f"Prompt utilizado:\n```\n{prompt_v1}\n```")

try:
    response_v1 = model.generate_content(prompt_v1,
                                         generation_config=genai.types.GenerationConfig(
                                             temperature=0.7, # Permite cierta creatividad
                                             max_output_tokens=500 # Limita la longitud para evitar respuestas excesivas
                                         ))
    print("\nRespuesta del Modelo (V1 - temperature=0.7):\n")
    print(response_v1.text)
    print("\n" + "="*80 + "\n")
except Exception as e:
    print(f"Error al generar contenido con Prompt V1: {e}")

# --- PROMPT V2: Mejorado con Rol, Formato y Requisitos Específicos ---
# Este prompt demuestra la aplicación de "Fast Prompting" con:
# -   **Rol:** El modelo actúa como un QA Engineer.
# -   **Formato Explícito:** Se le da un ejemplo de cómo debe ser la estructura Gherkin.
# -   **Restricciones/Criterios:** Se le pide cubrir escenarios de éxito y de borde/negativos.
# -   **Clarity:** Instrucciones muy claras sobre la tarea.
print("--- PASO 2: PROMPT MEJORADO CON ROL, FORMATO Y REQUISITOS ESPECÍFICOS ---")
print("Aquí aplicamos técnicas de Fast Prompting para guiar mejor al modelo.")

prompt_v2_template = """
Eres un experimentado Ingeniero de Calidad (QA Engineer) especializado en la creación de pruebas de aceptación.
Tu tarea es generar escenarios de casos de prueba exhaustivos en formato Gherkin (Feature, Scenario, Given, When, Then) para la siguiente Historia de Usuario.

Asegúrate de cubrir:
-   Un escenario de éxito (flujo principal).
-   Al menos un escenario de caso de borde o negativo (ej: producto no disponible, carrito lleno, usuario no autenticado, permisos incorrectos, etc., relevante para la HU).
-   Si la historia de usuario implica múltiples roles, considera escenarios desde cada perspectiva relevante.

---
Historia de Usuario:
{user_story}
---

Formato de Salida Requerido (debes producir el código Gherkin dentro de un bloque 'gherkin'):
```gherkin
Feature: [Nombre descriptivo de la característica]
    Scenario: [Descripción concisa del escenario de éxito]
        Given [Precondición 1]
        And [Precondición 2]
        When [Acción 1]
        And [Acción 2]
        Then [Resultado esperado 1]
        And [Resultado esperado 2]

    Scenario: [Descripción concisa del escenario de borde/negativo]
        Given [Precondición para el caso de borde]
        When [Acción que lleva al caso de borde]
        Then [Resultado esperado del caso de borde]
```

Ahora, genera los escenarios para la Historia de Usuario proporcionada.
"""

# --- Demostración con Historias de Usuario adicionales ---
# Usaremos la misma plantilla del Prompt V2, pero variando la Historia de Usuario
# y la configuración de temperatura para mostrar su impacto.

# Prueba con la Historia de Usuario 1 (flujo principal) con baja temperatura
print("\n--- Ejecutando Prompt V2 con HU1 (temperature=0.0 - Más determinista) ---")
current_user_story = user_story_1
prompt_v2_hu1_low_temp = prompt_v2_template.format(user_story=current_user_story)

print(f"\nHistoria de Usuario: {current_user_story}")
print(f"Prompt utilizado:\n```\n{prompt_v2_hu1_low_temp}\n```")

try:
    response_v2_hu1_low_temp = model.generate_content(prompt_v2_hu1_low_temp,
                                                      generation_config=genai.types.GenerationConfig(
                                                          temperature=0.0, # Muy bajo para apegarse al formato y ser determinista
                                                          max_output_tokens=700
                                                      ))
    print("\nRespuesta del Modelo (V2 - HU1 - temperature=0.0):\n")
    gherkin_output = extract_gherkin(response_v2_hu1_low_temp.text)
    print(gherkin_output)
    print("\n" + "="*80 + "\n")
except Exception as e:
    print(f"Error al generar contenido con Prompt V2 (HU1, low temp): {e}")


# Prueba con la Historia de Usuario 2 (administrador de usuarios) con temperatura media
print("\n--- Ejecutando Prompt V2 con HU2 (temperature=0.5 - Equilibrio) ---")
current_user_story = user_story_2
prompt_v2_hu2_mid_temp = prompt_v2_template.format(user_story=current_user_story)

print(f"\nHistoria de Usuario: {current_user_story}")
print(f"Prompt utilizado:\n```\n{prompt_v2_hu2_mid_temp}\n```")

try:
    response_v2_hu2_mid_temp = model.generate_content(prompt_v2_hu2_mid_temp,
                                                      generation_config=genai.types.GenerationConfig(
                                                          temperature=0.5, # Un equilibrio entre creatividad y determinismo
                                                          max_output_tokens=700
                                                      ))
    print("\nRespuesta del Modelo (V2 - HU2 - temperature=0.5):\n")
    gherkin_output = extract_gherkin(response_v2_hu2_mid_temp.text)
    print(gherkin_output)
    print("\n" + "="*80 + "\n")
except Exception as e:
    print(f"Error al generar contenido con Prompt V2 (HU2, mid temp): {e}")


# Prueba con la Historia de Usuario 3 (múltiples roles) con temperatura alta
print("\n--- Ejecutando Prompt V2 con HU3 (temperature=0.9 - Más creativo para explorar casos) ---")
current_user_story = user_story_3
prompt_v2_hu3_high_temp = prompt_v2_template.format(user_story=current_user_story)

print(f"\nHistoria de Usuario: {current_user_story}")
print(f"Prompt utilizado:\n```\n{prompt_v2_hu3_high_temp}\n```")

try:
    response_v2_hu3_high_temp = model.generate_content(prompt_v2_hu3_high_temp,
                                                      generation_config=genai.types.GenerationConfig(
                                                          temperature=0.9, # Mayor creatividad para explorar más escenarios y roles
                                                          max_output_tokens=1000 # Más tokens para escenarios más complejos
                                                      ))
    print("\nRespuesta del Modelo (V2 - HU3 - temperature=0.9):\n")
    gherkin_output = extract_gherkin(response_v2_hu3_high_temp.text)
    print(gherkin_output)
    print("\n" + "="*80 + "\n")
except Exception as e:
    print(f"Error al generar contenido con Prompt V2 (HU3, high temp): {e}")

print("\n--- ANÁLISIS DE RESULTADOS ---")
print("Puedes observar cómo el 'Prompt V2' genera escenarios más estructurados y relevantes ")
print("gracias a las instrucciones claras, el rol asignado y la especificación del formato.")
print("La 'temperature' afecta la creatividad y la exploración de casos de borde.")
print("Un 'temperature' bajo (0.0) es ideal para formato estricto, mientras que uno alto (0.7-0.9) ")
print("puede ayudar a descubrir más escenarios si la historia de usuario lo permite.")
print("\n¡Esta es una base sólida para tu POC en Jupyter Notebook!")
