<script setup>
import { ref } from 'vue'
import axios from 'axios'

// 1. Reaktywne zmienne
const sourceText = ref('')
const translatedText = ref('')
const sourceLang = ref('auto')
const targetLang = ref('pl')

// Licznik dla mechanizmu opóźnienia (debouncing)
let timeout = null

// 2. Funkcja wysyłająca zapytanie do serwera Bartka
const translate = () => {
  // Czyścimy poprzedni licznik, jeśli użytkownik nadal pisze
  clearTimeout(timeout)

  // Jeśli pole jest puste, czyścimy wynik i nie wysyłamy zapytania
  if (sourceText.value.trim() === '') {
    translatedText.value = ''
    return
  }

  // Ustawiamy opóźnienie 500ms, aby nie blokować API przy każdej literce
  timeout = setTimeout(async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/translate/', {
        text: sourceText.value,
        source_lang: sourceLang.value,
        lang: targetLang.value
      })
      
      translatedText.value = response.data.translated_text
    } catch (error) {
      console.error("Błąd połączenia z backendem:", error)
      translatedText.value = "Błąd: Nie udało się połączyć z serwerem tłumaczeń."
    }
  }, 500) 
}

// 3. Funkcja zamiany języków miejscami
const swapLanguages = () => {
  const tempLang = sourceLang.value
  sourceLang.value = targetLang.value
  targetLang.value = tempLang === 'auto' ? 'en' : tempLang 

  const tempText = sourceText.value
  sourceText.value = translatedText.value
  translatedText.value = tempText

  translate()
}
</script>

<template>
  <div class="home-container">
    
    <div class="translator-panel">
      
      <div class="translation-box">
        <div class="box-header">
          <select class="language-select" v-model="sourceLang" @change="translate">
            <option value="auto">Rozpoznaj język</option>
            <option value="pl">Polski</option>
            <option value="en">Angielski</option>
            <option value="de">Niemiecki</option>
            <option value="fr">Francuski</option>
          </select>
        </div>
        <textarea 
          class="text-area" 
          v-model="sourceText"
          @input="translate"
          placeholder="Wpisz tekst do przetłumaczenia..."
        ></textarea>
      </div>

      <button class="swap-btn" @click="swapLanguages" title="Zamień języki">
        ⇄
      </button>

      <div class="translation-box">
        <div class="box-header">
          <select class="language-select" v-model="targetLang" @change="translate">
            <option value="pl">Polski</option>
            <option value="en">Angielski</option>
            <option value="de">Niemiecki</option>
            <option value="fr">Francuski</option>
          </select>
        </div>
        <textarea 
          class="text-area result-area" 
          v-model="translatedText"
          readonly 
          placeholder="Tłumaczenie pojawi się tutaj..."
        ></textarea>
      </div>

    </div>

    <div class="popular-section">
      <h2>Ponad 100 języków do wyboru</h2>
      <h3>Najpopularniejsze</h3>
      <div class="tags">
        <span class="tag" @click="sourceLang='en'; targetLang='pl'; translate()">angielski 〉 polski</span>
        <span class="tag" @click="sourceLang='de'; targetLang='pl'; translate()">niemiecki 〉 polski</span>
        <span class="tag" @click="sourceLang='pl'; targetLang='en'; translate()">polski 〉 angielski</span>
      </div>
    </div>

  </div>
</template>

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  gap: 3rem;
  max-width: 1200px;
  margin: 0 auto;
}

.translator-panel {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.translation-box {
  flex: 1;
  border: 1px solid #2a2e5d;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  transition: border-color 0.3s;
}

.translation-box:focus-within {
  border-color: #4a52ff;
}

.box-header {
  border-bottom: 1px solid #e0e0e0;
  padding: 0.8rem 1.2rem;
  background-color: #fcfcfc;
}

.language-select {
  border: none;
  background: transparent;
  font-weight: bold;
  font-size: 1rem;
  color: #2a2e5d;
  outline: none;
  cursor: pointer;
}

.text-area {
  width: 100%;
  height: 250px;
  border: none;
  padding: 1.5rem;
  font-size: 1.25rem;
  font-family: inherit;
  resize: none;
  outline: none;
  box-sizing: border-box;
  color: #333;
}

.result-area {
  background-color: #f8f9ff;
  color: #555;
}

.swap-btn {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 50%;
  width: 45px;
  height: 45px;
  font-size: 1.5rem;
  color: #2a2e5d;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.swap-btn:hover {
  transform: rotate(180deg);
  border-color: #2a2e5d;
}

.popular-section h2 {
  font-size: 1.8rem;
  margin-bottom: 0.5rem;
}

.popular-section h3 {
  font-size: 1rem;
  color: #666;
  margin-bottom: 1.2rem;
}

.tags {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.tag {
  border: 1px solid #2a2e5d;
  border-radius: 25px;
  padding: 0.5rem 1.2rem;
  font-size: 0.9rem;
  font-weight: bold;
  color: #2a2e5d;
  cursor: pointer;
  transition: all 0.2s;
}

.tag:hover {
  background-color: #2a2e5d;
  color: white;
}
</style>