# Super Tłumacz 📖 - Frontend Development

Ten profil stanowi fork oryginalnego repozytorium projektu akademickiego "Super Tłumacz". Celem tego repozytorium jest szczegółowe zaprezentowanie **mojego osobistego wkładu** w rozwój warstwy prezentacji (Frontend) aplikacji.

Projekt został zrealizowany w zespole czteroosobowym. Moim zadaniem było zaprojektowanie, wdrożenie i optymalizacja interfejsu użytkownika oraz logiki klienckiej.

## 👨‍💻 Moja rola: Frontend Developer (Mateusz Brokos)

W ramach prac nad projektem odpowiadałem za architekturę aplikacji po stronie klienta, budując w pełni funkcjonalne SPA (Single Page Application). Poniżej znajduje się zestawienie moich kluczowych implementacji:

### 🚀 Kluczowe wdrożenia:
* **Architektura SPA w Vue.js 3:** Zbudowanie struktury aplikacji wykorzystującej najnowsze standardy frameworka, w tym *Composition API*, co zapewniło czytelność i łatwość w utrzymaniu kodu.
* **Autorski State Management:** Zamiast implementacji zewnętrznych, ciężkich bibliotek (np. Vuex/Pinia), zaprojektowałem lekki, globalny stan aplikacji oparty na wbudowanej funkcji `reactive()`. Pozwoliło to na natychmiastowe odświeżanie komponentów (np. Navbaru) po zalogowaniu, bez przeładowywania strony.
* **Integracja z REST API:** Skonfigurowanie komunikacji między frontendem a serwerem Django. Użycie biblioteki **Axios** do asynchronicznej obsługi żądań HTTP (metody GET/POST, format JSON), co wyeliminowało efekt blokowania interfejsu podczas oczekiwania na odpowiedź z zewnętrznego API tłumacza.
* **Routing i Nawigacja:** Wdrożenie `vue-router` do płynnego przełączania się między widokami: Stroną Główną, formularzami autoryzacji oraz spersonalizowanym Panelem Użytkownika.
* **Responsywny UI/UX:** Zaprojektowanie i zakodowanie interfejsu przy użyciu czystego CSS3 (Flexbox), gwarantując pełną responsywność (RWD) na urządzeniach o różnej rozdzielczości.

## 🛠️ Stos technologiczny (Moja część)
* **Framework:** Vue.js 3
* **Języki:** JavaScript (ES6+), HTML5, CSS3
* **Komunikacja HTTP:** Axios
* **Routing:** Vue Router
* **Narzędzia:** Vite

## 💡 Czego nauczył mnie ten projekt?
Praca nad "Super Tłumaczem" pozwoliła mi w praktyce zrozumieć koncepcję reaktywności w nowoczesnych frameworkach JS oraz mechanizmy komunikacji bezstanowej z backendem. Nauczyłem się również efektywnego debugowania problemów z asynchronicznością i cyklem życia komponentów.

---
*Oryginalne repozytorium z pełnym kodem backendu (Django / MySQL) znajduje się w głównym projekcie zespołu.*
