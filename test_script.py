
import pytest

def test_html_title():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        assert '<title>Szajkó</title>' in content, "A címsor nem tartalmazza a 'Szajkó' szót!"

def test_html_structure():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        assert '<div class="container">' in content, "A body elem nem tartalmazza a div.container elemet!"

def test_css_container_style():
    with open('style.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert '.container {' in content, "Nincs .container osztály a CSS-ben!"
        assert 'margin: 15%;' in content, "A .container osztály nem tartalmaz 15%-os margót!"
        assert 'background-color: navy;' in content, "A .container osztály háttérszíne nem navy!"
        assert 'color: white;' in content, "A .container osztály betűszíne nem fehér!"

def test_h1_style():
    with open('style.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'h1 {' in content, "Nincs h1 elem stílus a CSS-ben!"
        assert 'text-align: center;' in content, "A h1 elem nincs középre igazítva!"
