# 🎙️ Guión de Entrevista de Retroalimentación (Método DESC)

Este proyecto genera una simulación de audio realista de una entrevista de evaluación de desempeño entre un gerente y un colaborador. Utiliza Python y la librería `edge-tts` para convertir el guion en una conversación fluida con voces neuronales (IA).

## 📋 Contexto del Escenario

* **Objetivo:** Entrevista de revisión de resultados y retroalimentación constructiva.
* **Metodología:** Se utiliza el método **DESC** (Describir, Expresar, Sugerir, Consecuencias) dentro de una estructura de "Sándwich" (Positivo - Mejora - Positivo).
* **Personajes:**
    * 👩‍💼 **Elena (Gerente):** Voz rápida, dinámica y profesional.
    * 👨‍💼 **Javier (Ejecutivo de Ventas):** Voz tranquila y receptiva.

---

## 💬 El Diálogo

A continuación, se presenta el guion completo utilizado en la generación del audio:

### Fase 1: Apertura y Conexión
> **👩‍💼 Elena:** Hola, Javier. Gracias por tomarte este tiempo. Pasa, por favor. ¿Cómo has sentido el cierre de este trimestre?
>
> **👨‍💼 Javier:** Hola, Elena. Pues intenso, la verdad. Los clientes estuvieron muy exigentes las últimas semanas, pero creo que logramos sacar los números.
>
> **👩‍💼 Elena:** Justamente de eso quiero que hablemos. El objetivo de esta reunión no es solo revisar los KPIs, sino ver qué funcionó, qué nos frenó y cómo puedo apoyarte para el próximo Q3. Quiero que sea una charla abierta, ¿te parece?
>
> **👨‍💼 Javier:** Claro, me parece bien. Estoy listo.

### Fase 2: Refuerzo Positivo
> **👩‍💼 Elena:** Empecemos con lo bueno, que es bastante. Revisando tu tablero de resultados, superaste la meta de facturación en un 12%. Además, el cliente Tech-Solutions envió un correo felicitándote por la gestión de la crisis de la semana pasada.
>
> **👨‍💼 Javier:** ¡Qué bueno que llegó ese correo! La verdad me costó bastante calmar al gerente de compras, pero logramos retener la cuenta.
>
> **👩‍💼 Elena:** Esa habilidad que tienes para la negociación es tu fortaleza clave, Javier. El equipo aprende mucho viéndote interactuar con clientes difíciles. Quiero que sigas potenciando eso.

### Fase 3: Retroalimentación Constructiva (Método DESC)
> **👩‍💼 Elena (Describir):** Sin embargo, hay un aspecto operativo que necesitamos revisar para que ese talento en ventas brille más. He notado que, durante el último mes, los ingresos de datos al CRM se realizaron los viernes a última hora, en lugar de hacerlo diariamente.
>
> **👩‍💼 Elena (Expresar):** Me preocupa esto porque cuando Marketing extrae los datos los jueves, tu cartera aparece desactualizada. Esto genera reprocesos y me crea incertidumbre sobre el estado real del pipeline.
>
> **👩‍💼 Elena (Sugerir):** Para solucionar esto, necesito que reserves 15 minutos al final de cada día para actualizar el estatus de las llamadas clave.
>
> **👨‍💼 Javier:** Entiendo el punto, Elena. La verdad es que a veces siento que si me detengo a llenar el CRM pierdo el ritmo de las llamadas. Siento que es burocracia que me quita tiempo de venta.
>
> **👩‍💼 Elena:** Te entiendo, nadie se hizo vendedor por amor a llenar formularios. Pero piénsalo así: la semana pasada perdiste un lead porque Marketing no sabía que ya habías hablado con él y le enviaron una promoción equivocada.
>
> **👨‍💼 Javier:** Sí... eso fue un desastre. Tienes razón. Si lo veo como una herramienta para que no me quemen al cliente, tiene más sentido.

### Fase 4: Acuerdos y Cierre
> **👩‍💼 Elena:** Exacto. No es control por control, es alineación. ¿Crees que reservar los 15 minutos diarios es viable o prefieres hacerlo tras cada llamada?
>
> **👨‍💼 Javier:** Creo que prefiero el bloque de 15 minutos antes de irme. Si lo hago tras cada llamada, corto la inspiración.
>
> **👩‍💼 Elena (Consecuencias/Cierre):** Perfecto, entonces quedamos así: Mantienes tu enfoque en negociación y cierre. Bloqueas 15 minutos diarios a las 5 y media para vaciar datos en el CRM. Y revisamos en dos semanas si este nuevo hábito te está funcionando.
>
> **👨‍💼 Javier:** Me parece justo. Voy a poner la alarma en el calendario hoy mismo.
>
> **👩‍💼 Elena:** Excelente, Javier. De verdad, gracias por el esfuerzo este trimestre. Si solucionamos este tema administrativo, tu camino para la promoción a Senior estará mucho más despejado.
>
> **👨‍💼 Javier:** Gracias a ti por la claridad, Elena. A trabajar.

---

## 🚀 Cómo generar el audio tú mismo

Si quieres ejecutar el script para escuchar la conversación, sigue estos pasos:

### 1. Requisitos
Necesitas tener **Python 3.x** instalado.

### 2. Instalación
Instala la librería necesaria para conectar con las voces de Microsoft Edge:

```bash
pip install edge-tts
