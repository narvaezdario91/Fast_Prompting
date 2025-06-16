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
* **Técnica de Prompting "Fast Prompting"**: Se utilizan ejemplos para guiar a Gemini en la generación de casos de prueba relevantes y precisos.

---

## Configura tu clave de API de Gemini**:
* Crea una cuenta en Google AI Studio y genera una clave de API.
---

## Técnica de Prompting Utilizada: "Fast Prompting"

Este proyecto implementa la técnica de **"Fast Prompting"** para guiar a la API de Gemini en la generación de escenarios Gherkin. En lugar de simplemente darle una historia de usuario y esperar una respuesta, le proporcionamos a Gemini **ejemplos de pares de entrada-salida**. Es decir, le mostramos:

* Una **Historia de Usuario de ejemplo**.
* Los **escenarios Gherkin esperados** que se derivarían de esa historia de usuario.

Al presentar varios de estos ejemplos, el modelo de Gemini aprende el patrón y la estructura deseada para la generación de Gherkin a partir de nuevas historias de usuario. Esto mejora significativamente la calidad y relevancia de los casos de prueba generados, asegurando que se adhieran al formato BDD (Behavior-Driven Development) y reflejen las expectativas de la historia de usuario.

---
