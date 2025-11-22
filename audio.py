import asyncio
import edge_tts
import os

# --- CONFIGURACIÓN DE PERSONAJES ---
# Ajustamos velocidad (rate) y tono (pitch) para dar personalidad
# Elena: Habla rápido (+15%) y dinámico.
CONFIG_ELENA = {
    "voice": "es-MX-DaliaNeural",
    "rate": "+15%",  
    "pitch": "+2Hz"
}

# Javier: Habla un poco más pausado que Elena (+10%) y tono ligeramente grave.
CONFIG_JAVIER = {
    "voice": "es-MX-JorgeNeural",
    "rate": "+10%",
    "pitch": "-2Hz"
}

guion = [
    ("Elena", "Hola, Javier. Gracias por tomarte este tiempo. Pasa, por favor. ¿Cómo has sentido el cierre de este trimestre?"),
    ("Javier", "Hola, Elena. Pues intenso, la verdad. Los clientes estuvieron muy exigentes las últimas semanas, pero creo que logramos sacar los números."),
    ("Elena", "Justamente de eso quiero que hablemos. El objetivo de esta reunión no es solo revisar los KPIs, sino ver qué funcionó, qué nos frenó y cómo puedo apoyarte para el próximo Q3. Quiero que sea una charla abierta, ¿te parece?"),
    ("Javier", "Claro, me parece bien. Estoy listo."),
    ("Elena", "Empecemos con lo bueno, que es bastante. Revisando tu tablero de resultados, superaste la meta de facturación en un 12%. Además, el cliente Tech-Solutions envió un correo felicitándote por la gestión de la crisis de la semana pasada."),
    ("Javier", "¡Qué bueno que llegó ese correo! La verdad me costó bastante calmar al gerente de compras, pero logramos retener la cuenta."),
    ("Elena", "Esa habilidad que tienes para la negociación es tu fortaleza clave, Javier. El equipo aprende mucho viéndote interactuar con clientes difíciles. Quiero que sigas potenciando eso."),
    ("Elena", "Sin embargo, hay un aspecto operativo que necesitamos revisar para que ese talento en ventas brille más. He notado que, durante el último mes, los ingresos de datos al CRM se realizaron los viernes a última hora, en lugar de hacerlo diariamente."),
    ("Elena", "Me preocupa esto porque cuando Marketing extrae los datos los jueves, tu cartera aparece desactualizada. Esto genera reprocesos y me crea incertidumbre sobre el estado real del pipeline."),
    ("Elena", "Para solucionar esto, necesito que reserves 15 minutos al final de cada día para actualizar el estatus de las llamadas clave."),
    ("Javier", "Entiendo el punto, Elena. La verdad es que a veces siento que si me detengo a llenar el CRM pierdo el ritmo de las llamadas. Siento que es burocracia que me quita tiempo de venta."),
    ("Elena", "Te entiendo, nadie se hizo vendedor por amor a llenar formularios. Pero piénsalo así: la semana pasada perdiste un lead porque Marketing no sabía que ya habías hablado con él y le enviaron una promoción equivocada."),
    ("Javier", "Sí... eso fue un desastre. Tienes razón. Si lo veo como una herramienta para que no me quemen al cliente, tiene más sentido."),
    ("Elena", "Exacto. No es control por control, es alineación. ¿Crees que reservar los 15 minutos diarios es viable o prefieres hacerlo tras cada llamada?"),
    ("Javier", "Creo que prefiero el bloque de 15 minutos antes de irme. Si lo hago tras cada llamada, corto la inspiración."),
    ("Elena", "Perfecto, entonces quedamos así: Mantienes tu enfoque en negociación y cierre. Bloqueas 15 minutos diarios a las 5 y media para vaciar datos en el CRM. Y revisamos en dos semanas si este nuevo hábito te está funcionando."),
    ("Javier", "Me parece justo. Voy a poner la alarma en el calendario hoy mismo."),
    ("Elena", "Excelente, Javier. De verdad, gracias por el esfuerzo este trimestre. Si solucionamos este tema administrativo, tu camino para la promoción a Senior estará mucho más despejado."),
    ("Javier", "Gracias a ti por la claridad, Elena. A trabajar.")
]

async def generar_audio():
    carpeta_salida = "audio_entrevista"
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)
    
    archivos_generados = []
    
    print(f"--- Generando diálogo realista (Velocidad ajustada) ---")

    for i, (personaje, texto) in enumerate(guion):
        # Seleccionar configuración
        config = CONFIG_ELENA if personaje == "Elena" else CONFIG_JAVIER
        
        numero = str(i + 1).zfill(2)
        nombre_archivo = f"{carpeta_salida}/{numero}_{personaje}.mp3"
        archivos_generados.append(nombre_archivo)
        
        print(f"Generando {numero} ({personaje})...")
        
        # Generamos el audio con los parámetros de velocidad y tono
        comunicate = edge_tts.Communicate(texto, config["voice"], rate=config["rate"], pitch=config["pitch"])
        await comunicate.save(nombre_archivo)

    print("\n--- Uniendo archivos en uno solo ---")
    
    # HACK: Unión binaria simple para evitar instalar ffmpeg
    # Funciona en la mayoría de reproductores modernos
    archivo_final = "ENTREVISTA_COMPLETA.mp3"
    
    with open(archivo_final, 'wb') as outfile:
        for fname in archivos_generados:
            with open(fname, 'rb') as infile:
                outfile.write(infile.read())
    
    print(f"¡ÉXITO! Escucha el archivo final: {archivo_final}")

if __name__ == "__main__":
    asyncio.run(generar_audio())