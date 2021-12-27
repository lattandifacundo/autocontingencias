def template(alertType):
    if alertType == 'green':
        return "🟢 Alerta verde\n"+\
            "🌦 Se ha detectado una pequeña formación de granizo en las nubes\n\n"+\
            "⚠ Le recomendamos que revise la imagen usted mismo, el algoritmo puede fallar.\n"+\
            "❓ ¿No sabe como leer la imagen? <a href=\'https://lattandifacundo.github.io/autocontingencias/docs.html\'>Aprenda aquí</a>."
    
    elif alertType == 'yellow':
        return "🟡 <b>Alerta amarilla</b>\n"+\
            "⛈ <b>Se han detectado formaciones leves de granizo en las nubes</b>\n\n"+\
            "⚠ Le recomendamos que revise la imagen usted mismo, el algoritmo puede fallar.\n"+\
            "❓ ¿No sabe como leer la imagen? <a href=\'https://lattandifacundo.github.io/autocontingencias/docs.html\'>Aprenda aquí</a>."
    
    elif alertType == 'red':
        return "🔴 <b><u>Alerta roja</u></b>\n"+\
            "⛈ <b>Se ha detectado granizo en las nubes</b>\n\n"+\
            "⚠ Este tipo de tormentas suelen provocar descargas atmosfericas.\n"+\
            "⚠ Le recomendamos que revise la imagen usted mismo, el algoritmo puede fallar.\n"+\
            "❓ ¿No sabe como leer la imagen? <a href=\'https://lattandifacundo.github.io/autocontingencias/docs.html\'>Aprenda aquí</a>."
