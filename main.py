import string

# Fréquences des lettres pour le français et l'anglais
percentOfLetters = {
    "fr": {
        "a": 7.636,
        "b": 0.901,
        "c": 3.260,
        "d": 3.669,
        "e": 14.715,
        "f": 1.066,
        "g": 0.866,
        "h": 0.737,
        "i": 7.529,
        "j": 0.613,
        "k": 0.074,
        "l": 5.456,
        "m": 2.968,
        "n": 7.095,
        "o": 5.796,
        "p": 2.521,
        "q": 1.362,
        "r": 6.693,
        "s": 7.948,
        "t": 7.244,
        "u": 6.311,
        "v": 1.838,
        "w": 0.049,
        "x": 0.427,
        "y": 0.128,
        "z": 0.326
    },
    "en": {
        "a": 8.167,
        "b": 1.492,
        "c": 2.782,
        "d": 4.253,
        "e": 12.702,
        "f": 2.228,
        "g": 2.015,
        "h": 6.094,
        "i": 6.966,
        "j": 0.153,
        "k": 0.772,
        "l": 4.025,
        "m": 2.406,
        "n": 6.749,
        "o": 7.507,
        "p": 1.929,
        "q": 0.095,
        "r": 5.987,
        "s": 6.327,
        "t": 9.056,
        "u": 2.758,
        "v": 0.978,
        "w": 2.360,
        "x": 0.150,
        "y": 1.974,
        "z": 0.074
    }
}

def calculate_letter_frequencies(text):
    """Calcule les fréquences de lettres dans le texte."""
    text = text.lower()
    total_letters = sum(1 for char in text if char in string.ascii_lowercase)
    frequencies = {char: 0 for char in string.ascii_lowercase}

    for char in text:
        if char in frequencies:
            frequencies[char] += 1

    # Convertir en pourcentages
    return {char: (count / total_letters * 100) for char, count in frequencies.items() if total_letters > 0}

def calculate_language_difference(text_frequencies, language_frequencies):
    """Calcule la différence totale entre les fréquences des lettres du texte et d'une langue donnée."""
    difference = 0
    for letter in string.ascii_lowercase:
        text_freq = text_frequencies.get(letter, 0)
        lang_freq = language_frequencies.get(letter, 0)
        difference += abs(text_freq - lang_freq)
    return difference

def detect_language(text):
    """Détecte la langue du texte basé sur les fréquences des lettres."""
    text_frequencies = calculate_letter_frequencies(text)
    differences = {
        lang: calculate_language_difference(text_frequencies, freqs)
        for lang, freqs in percentOfLetters.items()
    }
    # Retourne la langue avec la plus petite différence
    return min(differences, key=differences.get)

# Exemple d'utilisation
text = "Hello"
detected_language = detect_language(text)
print(f"La langue détectée est : {detected_language}")
