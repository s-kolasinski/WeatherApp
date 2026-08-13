
# Desktopowy Asystent Pogodowy

## 1. Krótki opis
Aplikacja desktopowa napisana w języku Python, umożliwiająca szybkie sprawdzanie aktualnej pogody dla wybranego miasta. Projekt został zrealizowany w celu nauki tworzenia interfejsów graficznych (GUI) w bibliotece PySide6, obsługi zapytań sieciowych HTTP, bezpiecznego zarządzania zmiennymi środowiskowymi oraz utrwalania danych. Aplikacja posiada wbudowaną historię wyszukiwania zapisywaną lokalnie oraz okna dialogowe do obsługi błędów.

## 2. Technologie
* **Python 3**
* **PySide6 (Qt)** - budowa interfejsu graficznego (Event-driven programming)
* **requests** - klient HTTP do komunikacji z zewnętrznym API
* **python-dotenv** - bezpieczne ładowanie kluczy uwierzytelniających
* **JSON** - lokalny zapis i odczyt historii wyszukiwań
* **OpenWeatherMap API** - źródło danych pogodowych

## 3. Instrukcja uruchomienia

Postępuj zgodnie z poniższymi krokami, aby uruchomić projekt lokalnie na swoim komputerze.

1. **Sklonuj repozytorium:**
   ```bash
   git clone [https://github.com/TWOJA_NAZWA_UZYTKOWNIKA/nazwa-repozytorium.git](https://github.com/TWOJA_NAZWA_UZYTKOWNIKA/nazwa-repozytorium.git)
   cd nazwa-repozytorium

2. **Utwórz i aktywuj środowisko wirtualne:**
* **Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```


* **macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate

```




3. **Zainstaluj wymagane pakiety:**
```bash
pip install -r requirements.txt

```


4. **Skonfiguruj zmienne środowiskowe:**
* Utwórz plik o nazwie `.env` w głównym folderze projektu.
* Wklej do niego swój klucz API pobrany z serwisu OpenWeatherMap w poniższym formacie:
```env
key=TWÓJ_KLUCZ_API

```




5. **Uruchom aplikację:**
```bash
python main.py
```
