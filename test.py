# pip install googletrans==3.1.0a0

from googletrans import Translator
translator = Translator(service_urls=['translate.googleapis.com'])
trans = translator.translate("Der Himmel ist blau und ich mag Bananen", dest='en')
print(trans.text)