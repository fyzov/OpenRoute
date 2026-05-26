from gpytranslate import SyncTranslator
from services import service

@service("t")
@service("translate")
def execute(prompt: str) -> None:
    translator = SyncTranslator()

    detected_lang = translator.detect(prompt)

    if detected_lang == 'ru':
        result = translator.translate(prompt, targetlang="en")
    else:
        result = translator.translate(prompt, targetlang="ru")

    print(result.text)
