import pytest
from bs4 import BeautifulSoup
from datetime import datetime

def create_html():
    today_date = datetime.now().strftime("%Y-%m-%d")
    html_content = """<!DOCTYPE html>
<html lang="hu">
<head>
<meta charset="utf-8" />
<title>AIX</title>
</head>
<body>
<h1>AIX</h1>
<p><!-- Egy -->Az <mark>AIX</mark> az <strong>Advanced Interactive eXecutive</strong> rövidítése. 
Az <mark>AIX</mark> egy kereskedelmi Unix operációs rendszer, amit
az IBM fejleszt.</p>
<p><!-- Kettő --><h2>Kettő</h2>Az <mark>AIX</mark> a UNIX System V rendszeren alapszik.</p>
<p><!-- Három --><h2>Három</h2>Támogatott platformok:
IBM RS/6000, POWER, PowerPC, IBM System i, System/370, PS/2, Apple Network Server.</p>
<!-- Felhasználó neve és dátuma: Teszt Felhasználó, {today_date} -->
</body>
</html>"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

# Teszt függvények
def test_language():
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    assert soup.html["lang"] == "hu"

def test_charset():
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    assert soup.meta["charset"].lower() == "utf-8"

def test_title():
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    assert soup.title.string == "AIX"

def test_heading():
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    assert soup.h1.string == "AIX"

def test_sections_with_headers():
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    sections = soup.find_all("h2")
    assert len(sections) == 2, "Nincs meg az összes második szintű fejezetcím."
    assert sections[0].string == "Kettő", "Az első második szintű fejezetcím hibás."
    assert sections[1].string == "Három", "A második második szintű fejezetcím hibás."

def test_bold_text():
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    bold_text = soup.find("strong", string="Advanced Interactive eXecutive")
    assert bold_text is not None, "Az 'Advanced Interactive eXecutive' szöveg nincs félkövérrel megjelölve."

def test_highlighted_aix():
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    highlighted_aix = soup.find_all("mark", string="AIX")
    assert len(highlighted_aix) >= 3, "Az AIX nincs mindenhol kiemelve."

# Tesztek futtatása
if __name__ == "__main__":
    create_html()
    pytest.main()