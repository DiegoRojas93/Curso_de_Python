from translate import Translator
import os

path = os.path.dirname(os.path.abspath(__file__))

with open(f"{ path }/fileFolder/message.txt", mode='r') as my_file:
    my_text = my_file.read()
    print(f"Mensaje original: {my_text}")
    print("Translating...")
    translator = Translator(to_lang="es")
    translation = translator.translate(my_text)
    print(f"Mensaje traducido: {translation}")
    
    with open(f"{ path }/fileFolder/translate_message.txt", 'w') as my_file_translation:
        text = my_file_translation.write(translation)