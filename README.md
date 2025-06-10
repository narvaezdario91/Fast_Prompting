# Generador de Casos de Pruebas en Gherkin a partir de Historias de Usuario

---

## Descripción del Proyecto

Este proyecto es una herramienta que automatiza la creación de escenarios de casos de pruebas en **formato Gherkin** a partir de una **Historia de Usuario** dada. Utiliza la **API de Gemini** para generar estos escenarios, lo que permite agilizar el proceso de diseño de pruebas y asegurar una mayor cobertura. La implementación se realiza en **Jupyter Notebooks**, facilitando la interactividad y la experimentación.

## ¿Por qué este proyecto?

En el ciclo de desarrollo de software, la creación manual de casos de prueba es un proceso que consume mucho tiempo y es propenso a errores. Este proyecto busca mitigar estos desafíos al aprovechar el poder de la inteligencia artificial para:

* **Acelerar la creación de casos de prueba**: Genera automáticamente escenarios en Gherkin, reduciendo el esfuerzo manual.
* **Mejorar la cobertura de pruebas**: La IA puede identificar diferentes caminos y escenarios que quizás no se consideren en un enfoque manual.
* **Mantener la consistencia**: Asegura que los casos de prueba sigan el formato Gherkin estándar, facilitando la legibilidad y la automatización.

---

## Características

* **Generación de escenarios Gherkin**: Convierte historias de usuario en escenarios de prueba estructurados.
* **Integración con la API de Gemini**: Utiliza las capacidades de IA avanzada de Gemini para la comprensión y generación de texto.
* **Desarrollo en Jupyter Notebooks**: Proporciona un entorno interactivo para el desarrollo, ejecución y visualización de los resultados.
* **Técnica de Prompting "Few-Shot Learning"**: Se utilizan ejemplos para guiar a Gemini en la generación de casos de prueba relevantes y precisos.

---

## Estructura del Proyecto
```bash
├── notebooks/
│   ├── Generador_Casos_Prueba.ipynb
│   └── ejemplos_prompting/
│       └── ejemplo_historia_usuario_1.txt
│       └── ejemplo_gherkin_1.feature
├── .env.example
├── requirements.txt
└── README.md
```

* `notebooks/Generador_Casos_Prueba.ipynb`: Contiene el código principal del proyecto, incluyendo la lógica para interactuar con la API de Gemini y generar los casos de prueba.
* `notebooks/ejemplos_prompting/`: Directorio que almacena los ejemplos utilizados para la técnica de *few-shot learning*.
* `.env.example`: Archivo de ejemplo para la configuración de las variables de entorno (por ejemplo, la clave de la API de Gemini).
* `requirements.txt`: Lista de dependencias del proyecto.
* `README.md`: Este archivo.

---

## Configuración del Entorno

Sigue estos pasos para configurar tu entorno y ejecutar el proyecto:

1.  **Clona el repositorio**:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd Generador_Casos_De_Pruebas_en_Gerkin_a_Partir_de_Historias_de_Usuario
    ```

2.  **Crea un entorno virtual (opcional pero recomendado)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    # venv\Scripts\activate   # En Windows
    ```

3.  **Instala las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configura tu clave de API de Gemini**:
    * Crea una cuenta en Google AI Studio y genera una clave de API.
    * Copia el archivo `.env.example` a `.env`:
        ```bash
        cp .env.example .env
        ```
    * Abre el archivo `.env` y reemplaza `YOUR_GEMINI_API_KEY` con tu clave de API real:
        ```
        GEMINI_API_KEY=YOUR_GEMINI_API_KEY
        ```

5.  **Inicia Jupyter Notebook**:
    ```bash
    jupyter notebook
    ```
    Se abrirá tu navegador con el entorno de Jupyter. Navega al directorio `notebooks/` y abre `Generador_Casos_Prueba.ipynb`.

---

## Uso

Una vez que tengas el entorno configurado y el Jupyter Notebook abierto:

1.  **Carga el Notebook `Generador_Casos_Prueba.ipynb`**.
2.  **Inserta tu Historia de Usuario**: Dentro del notebook, habrá una sección designada donde podrás pegar o cargar la historia de usuario que deseas convertir en casos de prueba.
3.  **Ejecuta las celdas**: Sigue las instrucciones del notebook y ejecuta cada celda. El código se encargará de llamar a la API de Gemini, aplicar la técnica de prompting y generar los escenarios Gherkin.
4.  **Revisa los resultados**: Los escenarios generados se mostrarán directamente en el notebook. Podrás copiarlos y utilizarlos en tus herramientas de automatización de pruebas.

---

## Técnica de Prompting Utilizada: "Few-Shot Learning"

Este proyecto implementa la técnica de **"Few-Shot Learning"** para guiar a la API de Gemini en la generación de escenarios Gherkin. En lugar de simplemente darle una historia de usuario y esperar una respuesta, le proporcionamos a Gemini **ejemplos de pares de entrada-salida**. Es decir, le mostramos:

* Una **Historia de Usuario de ejemplo**.
* Los **escenarios Gherkin esperados** que se derivarían de esa historia de usuario.

Al presentar varios de estos ejemplos, el modelo de Gemini aprende el patrón y la estructura deseada para la generación de Gherkin a partir de nuevas historias de usuario. Esto mejora significativamente la calidad y relevancia de los casos de prueba generados, asegurando que se adhieran al formato BDD (Behavior-Driven Development) y reflejen las expectativas de la historia de usuario.

Los ejemplos específicos utilizados para el *few-shot learning* se encuentran en el directorio `notebooks/ejemplos_prompting/`.

---

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este proyecto, como la adición de nuevas funcionalidades, la optimización de la técnica de prompting o mejoras en la interfaz de usuario, no dudes en:

1.  Hacer un *fork* del repositorio.
2.  Crear una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3.  Realizar tus cambios.
4.  Enviar un *pull request*.
