import pytest
from calculadora import dividir

def test_dividir_exitoso():
    # Arrange & Act
    resultado = dividir(10, 2)
    # Assert
    assert resultado == 5.0

def test_dividir_por_cero_lanza_excepcion():
    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        dividir(10, 0)
    assert str(exc_info.value) == "No se puede dividir entre cero"