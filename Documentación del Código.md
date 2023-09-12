# **AIScribe: Documentación del Código**

## **Tabla de Contenidos**

1. **[Introducción](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#introducci%C3%B3n)**
2. **[Estructura del Proyecto](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#estructura-del-proyecto)**
3. **[API de AIScribe](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#api-de-aiscribe)**
4. **[Plugin de Visual Studio Code](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#plugin-de-visual-studio-code)**
5. **[Modelos y Servicios](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#modelos-y-servicios)**
6. **[Utilidades](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#utilidades)**
7. **[Pruebas](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#pruebas)**
8. **[Contribución](https://chat.openai.com/c/00f2fe03-936c-48a1-9d93-0c808081d43c#contribuci%C3%B3n)**

---

## **Introducción**

Esta documentación está diseñada para proporcionar una visión detallada del código de AIScribe, explicando la estructura, las clases, las funciones y los métodos utilizados en el proyecto.

---

## **Estructura del Proyecto**

El proyecto AIScribe se divide en dos componentes principales:

- **`api`**: Contiene todo el código relacionado con la API de AIScribe.
- **`plugin`**: Contiene el código del plugin de Visual Studio Code.

---

## **API de AIScribe**

### **Endpoints**

- **`GET /prompts`**: Obtiene una lista de prompts generales.
- **`POST /simplify`**: Simplifica el texto enviado.

---

## **Plugin de Visual Studio Code**

### **Comandos**

- **`aiscribe:activate`**: Activa AIScribe en el proyecto actual.
- **`aiscribe:simplify`**: Simplifica la documentación existente.

---

## **Modelos y Servicios**

### **Modelos**

- **`Prompt`**: Modelo para los prompts generales.
- **`SimplifiedText`**: Modelo para el texto simplificado.

### **Servicios**

- **`OpenAIService`**: Servicio para interactuar con la API de OpenAI.

---

## **Utilidades**

- **`text_utils.py`**: Contiene funciones de utilidad para el manejo de texto.
- **`api_utils.py`**: Contiene funciones de utilidad para interactuar con APIs.

---

## **Pruebas**

- **`test_api.py`**: Pruebas para la API de AIScribe.
- **`test_plugin.py`**: Pruebas para el plugin de Visual Studio Code.

---

## **Contribución**

Si deseas contribuir al proyecto, por favor sigue las **[directrices de contribución](https://chat.openai.com/c/CONTRIBUTING.md)**.

---

Esta documentación del código tiene como objetivo proporcionar una comprensión clara de cómo está estructurado el proyecto y cómo funcionan sus diferentes componentes. Para más detalles, por favor refiérase al código fuente y a los comentarios dentro del código.
