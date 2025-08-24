# JUEGO-DE-AHORCADO
🎯 Objetivo
Desarrollar un juego interactivo del ahorcado que permita aplicar conceptos clave de programación como estructuras de datos, lógica condicional, eventos gráficos y validación de entrada. El proyecto busca integrar los contenidos de las 4 unidades del curso, con un enfoque educativo y técnico.

🧠 Tecnologías utilizadas
- Python 3
- Tkinter (interfaz gráfica)
- Estructuras de datos: listas, tuplas y diccionarios
- Programación orientada a objetos
- Programación funcional (uso de funciones lambda)

🧱 Estructura del Código
El juego está encapsulado en una clase AhorcadoApp que gestiona la interfaz y la lógica del juego. Se implementaron las siguientes mejoras:
- Tupla para representar la palabra secreta (inmutable)
- Lista para almacenar letras adivinadas
- Diccionario para manejar el estado completo del juego (estado_juego)
- Funciones lambda para dibujar partes del ahorcado de forma modular

🖥️ Funcionalidades
- Selección aleatoria de palabra secreta
- Visualización de letras adivinadas y guiones bajos
- Validación de entrada (solo letras, sin repetir)
- Dibujo progresivo del ahorcado en cada fallo
- Mensajes de victoria o derrota
- Botón para reiniciar el juego

📷 Interfaz Gráfica
El juego utiliza tkinter para mostrar:
- Canvas para dibujar el ahorcado
- Labels para mostrar la palabra, mensajes y contador de intentos
- Entry para ingresar letras
- Botones para adivinar y reiniciar

