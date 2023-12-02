# HiriRUNNER - Juego en Pygame

¡Bienvenido a HiriRUNNER! Este es un juego simple creado con Pygame, donde controlas a un jugador que debe esquivar enemigos y acumular puntos. Aquí hay una breve descripción y guía de cómo funciona el código.

## Controles del Juego

- Utiliza las teclas **izquierda** y **derecha** para mover al jugador y esquivar los enemigos.
- Acumula puntos a medida que evitas a los enemigos.
- El juego termina si colisionas con un enemigo.

## Estructura del Código

### `main_menu()`
- La función `main_menu()` representa el menú principal del juego.
- Muestra las opciones para jugar, acceder a las opciones o salir del juego.
- Utiliza la clase `Button` para manejar las interacciones del usuario.

### `play()`
- La función `play()` inicia el juego principal.
- Controla la lógica del juego, incluyendo el movimiento del jugador, la generación de enemigos y la gestión de colisiones.
- Muestra el puntaje actual en la esquina superior derecha de la pantalla.

### `options()`
- La función `options()` representa la pantalla de opciones.
- Permite al usuario realizar ajustes o regresar al menú principal.


## FUNCIONALIDADES A AGREGAR
- Lograr un menu de opciones funcional, donde se pueda ajustar entre otras cosas, dificultad del juego y velocidad de desplazamiento.
- Lograr que siempre haya un camino posible, y que no haya muerte "obligatoria" sino que dependa exclusivamente de las habilidades del jugador.


## Estructura de Carpetas
- **assets**: Contiene las imágenes utilizadas en el juego.
- **button.py**: Archivo que define la clase `Button` para gestionar botones interactivos.
- **font.ttf**: Fuente utilizada en el juego.

## Requerimientos
- Python 3.x
- Pygame

## Ejecución del Juego
1. Tener Python y Pygame instalados.
2. Ejecuta el archivo `main.py`.

¡Divertite jugando HiriRUNNER! Si tenés alguna pregunta o comentario, no dudes en preguntar.

