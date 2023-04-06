import unicodedata

def strip_accents(text: str) -> str:
    """Removes accents from text."""
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                  if unicodedata.category(c) != 'Mn')