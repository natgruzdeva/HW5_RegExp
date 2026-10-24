import re

def add_salt(match: re.Match) -> str:
    """
    Replace one matched russian vowel with its salty form.

    Args:
        match: re.Match: match object containing one vowel.

    Returns:
        original vowel followed by the lowercase 'с' and the same vowel converted to lowercase.
    """
    vowel = match.group()
    return vowel + "с" + vowel.lower()


def to_salty_language(text: str) -> str:
    """
    Translate russian text into the "salty language".
    After every russian vowel, this function inserts the lowercase 'с' and the same vowel in lowercase.

    Args:
        text: russian text.

    Returns:
        text translated into the "salty language".
    """
    pattern = r"[аеёиоуыэюяАЕЁИОУЫЭЮЯ]"

    return re.sub(pattern, add_salt, text)

def get_chords(filepath: str) -> set:
    """
    Find and write all unique chords from a song text file.

    Arguments:
    filepath: str - path to the file with text of song.

    Returns:
    set - a set of unique chords that were found in file.
    """

    with open(filepath, 'r') as file:
        text = file.read()
    
    pattern = r'\b[A-G][a-z0-9#b]*\b'
    chords = re.findall(pattern, text)
    
    return set(chords)