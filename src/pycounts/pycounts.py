from collections import Counter
from string import punctuation

def loud_file(input_file):
    """Load text from a text file and return as a string.

    Parameters
    ----------
    input_file : str
        Path to text file.

    Returns
    -------
    str
        Text file contents.

    Examples
    --------
    >>> load_text("text.txt")
    """
    with open(input_file, "r") as file:
        return file.read()
        
def clean_text(texto):
    """Lowercase and remove punctuation from a string.

    Parameters
    ----------
    text : str
        Text to clean.

    Returns
    -------
    str
        Cleaned text.

    Examples
    --------
    >>> clean_text("Early optimization is the root of all evil!")
    'early optimization is the root of all evil'
    """
    texto = texto.lower()
    for p in punctuation:
        texto = texto.replace(p, "")
    return texto
    
def count_words(input_file):
    """Count words in a text file.

    Words are made lowercase and punctuation is removed 
    before counting.

    Parameters
    ----------
    input_file : str
        Path to text file.

    Returns
    -------
    collections.Counter
        dict-like object where keys are words and values are counts.

    Examples
    --------
    >>> count_words("text.txt")
    """
    texto = loud_file(input_file)
    texto = clean_text(texto)
    palavras = texto.split()
    return Counter(palavras)
