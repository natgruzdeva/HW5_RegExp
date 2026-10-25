import re
import os

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


def rename_files(
    dir: str,
    pattern: str,
    new_pattern: str | None = None,
    sample_names: dict[str, str] | None = None,
    to_replace: bool = False,
) -> None:
    """Rename or copy files by pattern, by dictionary, or sequentially by both"""
    
    for filename in os.listdir(dir):
        old_path = os.path.join(dir, filename)
        if not os.path.isfile(old_path):
            continue
        if not re.search(pattern, filename):
            continue

        new_name = filename

        if new_pattern is not None: # Replace with pattern
            new_name = re.sub(pattern, new_pattern, new_name)
        if sample_names: # Replace with dictionary
            for old_sample, rep_sample in sample_names.items():
                new_name = re.sub(r'\b' + re.escape(old_sample) + r'\b', rep_sample, new_name)
        if new_name == filename: # Skip if file hasn't change name
            continue

        new_path = os.path.join(dir, new_name)

        if to_replace:
            os.replace(old_path, new_path)
        else:
            with open(old_path, "rb") as src, open(new_path, "wb") as dst:
                dst.write(src.read())