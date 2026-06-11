# Lekce 13 – Grafika s Pyglet

Materiály pro lekci 13 kurzu [PyLadies Praha – jaro 2026](https://naucse.python.cz/2025/praha-pyladies-jaro/).

## Obsah

### `had/`
Animovaný had – úvod do Pygletu. Postupně ukazuje:
- okno a smyčku událostí
- načtení obrázku a sprite
- pohyb pomocí `dt`
- vlnový pohyb (`sin`)
- přepínání snímků (animace)
- reakce na klik myší

### `pong/`
Finální řešení hry Pong rozdělené do souborů:

| Soubor | Obsah |
|---|---|
| `constants.py` | konstanty (velikost okna, rychlosti, …) |
| `obdelnik.py` | třída `Obdelnik` – základní kreslení |
| `mic.py` | třída `Mic(Obdelnik)` – pohyb a reset míčku |
| `palka.py` | třída `Palka(Obdelnik)` – pohyb palky, zarážky |
| `hra.py` | třída `Hra` – herní logika, odrazy, skóre |
| `pong.py` | vstupní bod – vytvoří okno a spustí hru |

Ovládání: hráč 1 = **W / S**, hráč 2 = **↑ / ↓**

### `pong_kroky/`
8 postupných kroků vedoucích od prázdného okna k hotové hře:

| Složka | Co přibývá |
|---|---|
| `krok1_okno` | prázdné okno |
| `krok2_mic_kresleni` | třída `Obdelnik`, `Mic` – vykreslení míčku |
| `krok3_palka_kresleni` | třída `Palka` – vykreslení palek |
| `krok4_cara_skore` | přerušovaná čára, skóre |
| `krok5_klavesy_pohyb` | klávesy, pohyb palek |
| `krok6_pohyb_mice` | pohyb míčku (`reset`, `pohyb`) |
| `krok7_odrazy` | odrazy od stěn a palek |
| `krok8_trida_hra` | třída `Hra` – vše pohromadě |

## Spuštění

```bash
pip install pyglet
python pong/pong.py
```
