import pytest
from app.lib.biblioteca_animale import culoare_veverita, descriere_veverita

def test_culoare_veverita():
    assert isinstance(culoare_veverita(), str)
    assert "alb" in culoare_veverita().lower()

def test_descriere_veverita():
    assert isinstance(descriere_veverita(), str)
    assert len(descriere_veverita()) > 10
