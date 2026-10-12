def dividir(a: float, b: float) -> float:
    """Divide dos números y valida la división por cero."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return round(a / b, 2)