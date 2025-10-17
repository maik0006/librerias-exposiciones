from PIL import Image, ImageFilter

def aplicar_desenfoque(nombre_entrada, nombre_salida):
    try:
   
        imagen = Image.open(nombre_entrada)
        print(f"Imagen '{nombre_entrada}' cargada correctamente.")

  
        imagen_desenfocada = imagen.filter(ImageFilter.BLUR)
        print("Filtro de desenfoque aplicado.")

    
        imagen_desenfocada.show()

        imagen_desenfocada.save(nombre_salida)
        print(f"Imagen guardada como '{nombre_salida}'.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_entrada}'.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

aplicar_desenfoque("paisaje.jpg", "paisaje_desenfocado.jpg")
