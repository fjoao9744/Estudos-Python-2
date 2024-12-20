import pytest

@pytest.fixture(params=[1, 2, 3])
def numero(request):
    return request.param

def test_multiplicacao(numero):
    assert numero * 2 == numero + numero
