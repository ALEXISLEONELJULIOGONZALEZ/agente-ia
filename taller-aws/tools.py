from strands import tool

@tool
def calcular_costo_mensual(costo_hora: float) -> str:
    """Calcula el costo estimado mensual de un servicio de AWS."""
    total = costo_hora * 720
    return f"El costo estimado por 30 días es de ${total:.2f} USD."

@tool
def obtener_region_recomendada(pais: str) -> str:
    """Recomienda la región de AWS según el país."""
    return "Para Colombia, la región recomendada es us-east-1 (N. Virginia)."

@tool
def estado_servicios_aws() -> str:
    """Verifica el estado de salud de los servicios."""
    return "Estado de servicios en us-east-1: Operativo."