# **AIScribe**

## **Tabla de Contenidos**

1. **[Introducción](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#introducci%C3%B3n)**
2. **[Objetivo](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#objetivo)**
3. **[Funcionalidades](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#funcionalidades)**
4. **[Historias de Usuario](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#historias-de-usuario)**
5. **[Componentes del Proyecto](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#componentes-del-proyecto)**
6. **[Proceso del Usuario](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#proceso-del-usuario)**
7. **[Arquitectura](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#arquitectura)**
8. **[Configuración](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#configuraci%C3%B3n)**
9. **[Requisitos del Sistema](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#requisitos-del-sistema)**
10. **[Documentación de los Endpoints](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#documentaci%C3%B3n-de-los-endpoints)**
11. **[Actualizaciones y Versiones Futuras](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#actualizaciones-y-versiones-futuras)**

---

## **Introducción**

AIScribe es un plugin para Visual Studio Code que utiliza el modelo de lenguaje GPT-3.5-turbo de OpenAI para autogenerar documentación técnica. La herramienta busca resolver problemas comunes en la industria tecnológica relacionados con la documentación inadecuada o insuficiente.

---

## **Objetivo**

El objetivo principal de AIScribe es mejorar la calidad y eficiencia de la documentación técnica en proyectos de software. Utiliza inteligencia artificial para generar documentación que sea tanto técnica como accesible para diferentes stakeholders, liberando tiempo de los desarrolladores para tareas más estratégicas.

---

## **Funcionalidades**

- **Generación de Archivos**: Crea archivos de documentación a partir de descripciones de proyectos, código existente o fragmentos de código.
- **Explicación Detallada**: Genera documentación detallada a partir de fragmentos de código, como clases, métodos o archivos completos.
- **Resumen de Documentación**: Capaz de resumir archivos de documentación preexistentes.
- **Simplificación de Lenguaje**: Convierte documentación técnica a un lenguaje más simple y accesible.

---

## **Historias de Usuario**

### **Historia 1: Generación Automática de Documentación Técnica**

**Criterios de Aceptación**:

- Formato legible y organizado en Markdown.
- Análisis del código fuente para extraer información relevante.

### **Historia 2: Acceso a Versión Resumida de la Documentación**

**Criterios de Aceptación**:

- Generación automática de una versión resumida.
- Formato fácil de entender y consumir.

### **Historia 3: Simplificación del Lenguaje en la Documentación**

**Criterios de Aceptación**:

- Opción para simplificar la documentación a un lenguaje más simple.
- Coherencia y retención de información esencial.

### **Historia 4: Referencias Cruzadas en la Documentación**

**Criterios de Aceptación**:

- Contener enlaces o referencias a los archivos y fragmentos de código relacionados.
- Navegación directa al código fuente desde la documentación.

---

## **Componentes del Proyecto**

### **API de AIScribe**

- **Endpoints Específicos**:
    - Endpoint de Prompts Generales
    - Endpoint de Simplificación de Texto

### **Plugin para Visual Studio Code**

- **Activación**: **`aiscribe:activate`**
- **Generación de Documentación**: Comandos **`/prompt`** y **`/snippet`**
- **Simplificación de Documentación**: **`aiscribe:simplify`**

---

## **Proceso del Usuario**

1. Activar la extensión con **`aiscribe:activate`**.
2. Utilizar comandos **`/prompt`** y **`/snippet`** para generar documentación.
3. Utilizar **`aiscribe:simplify`** para simplificar la documentación.

---

## **Arquitectura**

- **API**: Desarrollada en Python 3.10, dockerizada y hospedada en Azure App Services.
- **Plugin VSC**: Desarrollado en Node.js, siguiendo estándares de Visual Studio Code.

---

## **Configuración**

1. Clonar el repositorio AIScribe.
2. Asegurarse de tener Docker instalado.
3. Ejecutar **`docker-compose up --build`**.

---

## **Requisitos del Sistema**

- Docker
- Python 3.10

---

## **Documentación de los Endpoints**

Acceder a la documentación de Swagger en **`http://localhost:8000/docs`**.

---

## **Actualizaciones y Versiones Futuras**

Mantente atento a las actualizaciones y mejoras futuras en nuestro repositorio en Azure Repos y en nuestra comunidad.
