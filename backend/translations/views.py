import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Translation, User 
from .serializers import TranslationSerializer

class TranslateAPIView(APIView):
    def post(self, request):
        source_text = request.data.get('text')
        target_lang = request.data.get('lang')
        # Pobieramy język źródłowy wysłany z Vue
        source_lang = request.data.get('source_lang', 'auto') 

        if not source_text or not target_lang:
             return Response({"error": "Brak tekstu lub języka docelowego!"}, status=400)

        # Mapujemy 'auto' na pusty ciąg lub 'en', aby MyMemory nie wyrzucało błędu
        api_source = 'en' if source_lang == 'auto' else source_lang
        lang_pair = f"{api_source}|{target_lang}"
        
        api_url = f"https://api.mymemory.translated.net/get?q={source_text}&langpair={lang_pair}"

        try:
            response = requests.get(api_url)
            data = response.json()
            translated_text = data.get('responseData', {}).get('translatedText', "Błąd tłumaczenia")
            
            # Sprawdzamy czy API nie zwróciło błędu w tekście (to co widziałeś na screenie)
            if "INVALID SOURCE LANGUAGE" in translated_text.upper():
                translated_text = "Błąd: Wybierz konkretny język źródłowy."
        except Exception as e:
            return Response({"error": f"Błąd zewnętrznego API: {str(e)}"}, status=500)

        user = User.objects.first()
        if not user:
            return Response({"error": "Baza użytkowników jest pusta!"}, status=400)

        translation = Translation.objects.create(
            user=user,
            source_text=source_text,
            translated_text=translated_text,
            target_lang=target_lang,
            source_lang=source_lang
        )

        serializer = TranslationSerializer(translation)
        return Response(serializer.data)