
# ANEXO TÉCNICO: SIMULACIÓN DE BOT DE WHATSAPP PARA GESTIÓN DE VACACIONES

# Simulacion una base de datos interna de la empresa
BASE_DATOS_EMPLEADOS = {
    "3512345678": {"nombre": "Juan Pérez", "saldo_dias": 14},
    "3518765432": {"nombre": "María Evans", "saldo_dias": 21}
}

def validar_usuario(telefono):
    """
    Verifica si el número de teléfono está registrado en el sistema.
    Retorna los datos del empleado si existe, o None si no se encuentra.
    """
    if telefono in BASE_DATOS_EMPLEADOS:
        return BASE_DATOS_EMPLEADOS[telefono]
    return None

def solicitar_dias():
    """
    Manejo de Errores y Robustez: Solicita los días al usuario y
    obliga a reingresar el dato mediante un bucle si introduce texto.
    """
    while True:
        entrada = input("Bot: ¿Cuántos días de vacaciones deseas solicitar?: ")
        # Validación de formato numérico entero (evita que el programa se rompa)
        if entrada.isdigit():
            return int(entrada)
        else:
            print("Bot: Error de formato. Por favor, ingresa un número entero válido (ej: 7).")

def verificar_y_procesar_saldo(empleado, dias_solicitados):
    """
    Aplica las Reglas de Negocio controlando si el saldo es suficiente.
    Modifica el saldo si se aprueba y retorna True, de lo contrario False.
    """
    if dias_solicitados <= empleado["saldo_dias"]:
        # Modificación automatizada del saldo en la base de datos
        empleado["saldo_dias"] -= dias_solicitados
        return True
    return False

def ejecutar_bot_vacaciones():
    """
    Función principal que coordina el flujo del proceso (Diagrama To-Be)
    """
    print("--- SIMULACIÓN DE INTERFAZ DE WHATSAPP ---")
    telefono_usuario = input("Usuario envía mensaje desde el celular N°: ")
    
    # 1. Filtro de Seguridad / Validación de identidad
    empleado = validar_usuario(telefono_usuario)
    if empleado is None:
        print("Bot: Acceso Denegado. Este número de teléfono no está registrado.")
        print("--- FIN DEL PROCESO (Solicitud Rechazada) ---")
        return

    # 2. Saludo e información inicial de saldo
    print(f"\nBot: ¡Hola, {empleado['nombre']}! Bienvenido al asistente de RRHH.")
    print(f"Bot: Tu saldo actual disponible es de: {empleado['saldo_dias']} días.")
    
    # 3. Solicitud y validación de formato de días (Bucle interactivo)
    dias_pedidos = solicitar_dias()
    
    # 4. Solicitud de datos adicionales (Fecha de inicio)
    fecha_inicio = input("Bot: Ingresa la fecha de inicio deseada (DD/MM/AAAA): ")
    
    # 5. Validación de reglas de negocio (Saldo disponible)
    aprobado = verificar_y_procesar_saldo(empleado, dias_pedidos)
    
    if aprobado:
        # Generación automática de identificador único de trámite para auditoría
        codigo_tramite = f"VAC-{telefono_usuario[-4:]}-{dias_pedidos}"
        print("\nBot: ¡Solicitud Confirmada con éxito! 🎉")
        print(f"Bot: Se han registrado {dias_pedidos} días a partir del {fecha_inicio}.")
        print(f"Bot: Tu nuevo saldo disponible es: {empleado['saldo_dias']} días.")
        print(f"Bot: Código único de registro: {codigo_tramite}")
    else:
        print("\nBot: Solicitud Rechazada.")
        print(f"Bot: No tienes saldo suficiente. Solicitaste {dias_pedidos} días pero te quedan {empleado['saldo_dias']}.")
    
    print("--- FIN DEL PROCESO ---")

# Ejecución de la simulación del sistema automatizado
if __name__ == "__main__":
    ejecutar_bot_vacaciones()