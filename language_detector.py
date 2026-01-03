# Importing langdetect library
from langdetect import detect
#Importing colorama library
from colorama import Fore
# Function to detect the language of a sentence
def detect_language(text):
    return detect(text)

# The sentence
text = "வணக்கம்"

# ISO 639-1 language codes
codes = {
    'ar': 'Arabic',
    'sq': 'Albanian',
    'bn': 'Bangla',
    'bg': 'Bulgarian',
    'cs': 'Czech',
    'da': 'Danish',
    'de': 'German',
    'en': 'English',
    'fr': 'French',
    'el': 'Greek',
    'hi': 'Hindi',
    'id': 'Indonesian',
    'it': 'Italian',
    'ja': 'Japanese',
    'kn': 'Kannada',
    'ko': 'Korean',
    'la': 'Latin',
    'mr': 'Marathi',
    'nl': 'Dutch',
    'ta': 'Tamil',
    'te': 'Telugu',
    'cy': 'Welsh'
}

lang_code = detect_language(text)

print(Fore.GREEN + "Detected language code:", lang_code)
print(Fore.GREEN + "Detected language:", codes.get(lang_code, "Unknown Language"))

print(Fore.WHITE + "\nThank you for your patience")
