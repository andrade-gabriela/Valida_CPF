""""""

from valida_cpf import dv1_bruto, dv1, dv2_bruto, dv2, dv

def test_dv1_bruto():
    assert dv1_bruto('398136146') == 258

def test_dv1_digito():
    assert dv1('398136146') == 6

def test_dv2_bruto():
    assert dv2_bruto('398136146') == 299

def test_dv2():
    assert dv2('398136146') == 8

def test_dv_final():
    assert dv('398136146') == '68'