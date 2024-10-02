# Space Shooter - Juego en Python 🚀

## Descripción

**Space Shooter** es un videojuego en 2D desarrollado en Python utilizando la librería **PyGame**. El jugador controla una nave espacial y su objetivo es sobrevivir 20 segundos mientras destruye a los enemigos.

## Características del juego

- **Vidas del jugador**: El jugador tiene 3 vidas. Si es tocado por un enemigo, perderá una vida.
- **Enemigos**: Los enemigos aparecen aleatoriamente y se mueven hacia la nave del jugador.
- **Disparos**: El jugador puede disparar proyectiles presionando la barra espaciadora.
- **Música y efectos**: Incluye música de fondo y efectos de sonido al disparar.

## Instrucciones de instalación

### Requisitos

1. **Python** (versión 3.x)
2. **PyGame**, que puedes instalar con:

    ```bash
    pip install pygame
    ```

### Instalación

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener las siguientes imágenes y sonidos en la carpeta `assets/`:
   - `nave.png`
   - `enemy.png`
   - `projectile.png`
   - `space_background.png`
   - `shoot.wav`
   - `background_music.mp3`

3. Ejecuta el juego con:

    ```bash
    python main.py
    ```

## Controles del juego

- **Movimiento**: Usa las flechas izquierda/derecha.
- **Disparar**: Presiona la barra espaciadora.

## Archivos principales

| Archivo         | Descripción                          |
| --------------- | ------------------------------------ |
| `main.py`       | Archivo principal que ejecuta el juego |
| `player.py`     | Clase que controla la nave del jugador |
| `enemy.py`      | Clase que maneja los enemigos        |
| `projectile.py` | Clase que controla los disparos      |
