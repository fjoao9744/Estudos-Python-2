import pytest

@pytest.fixture
def dados_teste():
    return {"nome": "João", "idade": 25}

def test_dados(dados_teste):
    assert dados_teste["nome"] == "João"
    assert dados_teste["idade"] == 25


