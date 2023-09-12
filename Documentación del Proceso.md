# **AIScribe: Documentación del Proceso**

## **Tabla de Contenidos**

1. **[Introducción](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#introducci%C3%B3n)**
2. **[Requisitos Previos](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#requisitos-previos)**
3. **[Instalación del Plugin](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#instalaci%C3%B3n-del-plugin)**
4. **[Activación de AIScribe](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#activaci%C3%B3n-de-aiscribe)**
5. **[Generación de Documentación](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#generaci%C3%B3n-de-documentaci%C3%B3n)**
6. **[Simplificación de Documentación](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#simplificaci%C3%B3n-de-documentaci%C3%B3n)**
7. **[Resumen de Documentación](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#resumen-de-documentaci%C3%B3n)**
8. **[Referencias Cruzadas](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#referencias-cruzadas)**
9. **[Desactivación y Desinstalación](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#desactivaci%C3%B3n-y-desinstalaci%C3%B3n)**

---

## **Introducción**

Esta sección de la documentación está diseñada para guiar al usuario a través del proceso específico de utilizar AIScribe, desde la instalación hasta la generación y simplificación de la documentación técnica.

---

## **Requisitos Previos**

Antes de instalar AIScribe, asegúrate de tener instalado:

- Visual Studio Code
- Docker (si planeas trabajar con la API)
- Acceso a Azure Repos para clonar el repositorio

---

## **Instalación del Plugin**

Para instalar el plugin de AIScribe en Visual Studio Code, sigue estos pasos:

1. Abre Visual Studio Code.
2. Ve a la sección de extensiones.
3. Busca "AIScribe" y haz clic en "Instalar".

---

## **Activación de AIScribe**

Una vez instalado el plugin, puedes activarlo de la siguiente manera:

1. Abre la paleta de comandos de Visual Studio Code (**`Ctrl+Shift+P`** o **`Cmd+Shift+P`** en Mac).
2. Escribe y selecciona **`aiscribe:activate`**.

Esto creará una carpeta llamada **`aiscribe-docs`** en tu proyecto y abrirá un archivo **`general.md`** para empezar a documentar.

---

## **Generación de Documentación**

Para generar documentación, tienes dos comandos principales:

- **`/prompt "{input}"`**: Este comando envía un prompt al modelo de lenguaje para generar contenido de documentación.
- **`/snippet`**: Este comando te permite seleccionar fragmentos de código para incluirlos en la documentación.

Ambos comandos se pueden utilizar directamente en el archivo **`general.md`** o en cualquier otro archivo Markdown dentro de la carpeta **`aiscribe-docs`**.

---

## **Simplificación de Documentación**

Si deseas simplificar la documentación para hacerla más accesible para un público no técnico, sigue estos pasos:

1. Abre la paleta de comandos de Visual Studio Code.
2. Escribe y selecciona **`aiscribe:simplify`**.

Esto generará una versión simplificada de todos los archivos de documentación en la carpeta **`aiscribe-docs`**.

---

## **Resumen de Documentación**

Para resumir la documentación existente:

1. Abre la paleta de comandos de Visual Studio Code.
2. Escribe y selecciona **`aiscribe:summarize`**.

Esto generará un resumen de la documentación existente, destacando los puntos clave.

---

## **Ejecución de Comandos con 'Run Commands'**

Para ejecutar cualquier comando de AIScribe, es crucial utilizar el comando **`run commands`** en la barra de búsqueda de Visual Studio Code. Aquí te mostramos cómo hacerlo:

1. Abre la paleta de comandos de Visual Studio Code (**`Ctrl+Shift+P`** o **`Cmd+Shift+P`** en Mac).
2. Escribe **`run commands`** en la barra de búsqueda.
3. Selecciona **`run commands`** de la lista desplegable.
4. Ahora podrás ver una lista de todos los comandos disponibles para AIScribe (como **`aiscribe:activate`**, **`aiscribe:simplify`**, etc.). Selecciona el que desees ejecutar.

Este paso es esencial para asegurarte de que los comandos de AIScribe se ejecuten correctamente.

---

## **Desactivación y Desinstalación**

Para desactivar o desinstalar AIScribe:

1. Abre la paleta de comandos de Visual Studio Code.
2. Escribe y selecciona **`aiscribe:deactivate`** para desactivar.
3. Para desinstalar, ve a la sección de extensiones, busca "AIScribe" y haz clic en "Desinstalar".
