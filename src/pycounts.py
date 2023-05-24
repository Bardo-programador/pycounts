from collections import Counter
from string import punctuation

def loud_file(input_file):
    with open(input_file, "r") as file:
        return file.read()
        
def clean_text(texto):
    texto = texto.lower()
    for p in punctuation:
        texto = texto.replace(p, "")
    return texto
    
def counter_words(input_file):
    texto = loud_file(input_file)
    texto = clean_text(texto)
    palavras = texto.split()
    return Counter(palavras)

palavras = counter_words("zen.txt")

print(palavras)