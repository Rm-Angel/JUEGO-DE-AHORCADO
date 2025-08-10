# JUEGO-DE-AHORCADO
Adivinar una palabra secreta letra por letra antes de que se complete el dibujo de un ahorcado. Cada error acerca al jugador a perder la partida.

#Características
•	Interfaz gráfica amigable con tkinter
•	Dibujo progresivo del muñeco en cada fallo
•	Validación de letras y control de intentos
•	Botón para reiniciar el juego
•	Palabras aleatorias seleccionadas al inicio

#Vista previa
#La interfaz incluye:
•	Un área de dibujo (Canvas) donde se forma el muñeco
•	Un campo de entrada para letras
•	Mensajes de aciertos, errores y estado del juego
•	Contador de intentos
•	Botón para reiniciar la partida

#Lógica del juego
•	Se elige una palabra secreta aleatoria de una lista
•	El jugador ingresa letras una por una
•	Si la letra está en la palabra, se revela en pantalla
•	Si no está, se dibuja una parte del muñeco (cabeza, cuerpo, brazos, piernas)
•	El juego termina cuando se completa la palabra o se alcanzan 6 errores

#Requisitos
•	Python 3.x
•	No se requieren librerías externas (solo tkinter, que viene con Python)

 #Cómo ejecutar
•	python ahorcado.py
•	Asegúrate de tener el archivo guardado con extensión .py y que Python esté instalado correctamente.

 #Estructura del código
•	AhorcadoApp: clase principal que gestiona la interfaz y la lógica
•	dibujar_base(): dibuja la estructura de la horca
•	dibujar_ahorcado(): dibuja partes del muñeco según los errores
•	actualizar_palabra(): muestra el progreso de la palabra
•	adivinar(): procesa la letra ingresada
•	reiniciar(): reinicia el juego con una nueva palabra
