import re


def wordtrie_format(word: str):
    """Returns a str word formatted for the WordTrie."""
    # return re.sub(r'[^a-zA-Z0-9]', '', word.lower())
    return re.sub('-|:|\s+', '', word.lower())

