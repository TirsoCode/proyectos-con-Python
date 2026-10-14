#Traductor de frases de español a ingles 
from translate import Translator
traductor=Translator(from_lang="es",to_lang="en")
frase_usuario=input("Di la frase que quieres traducir ")
frase_traducida=traductor.translate(frase_usuario)
print(frase_traducida)