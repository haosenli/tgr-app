def name_similarity(name1: str, name2: str) -> float:
    """Calculates the float similarity percentage between two names."""
    name1 = name1.split()
    name2 = name2.split()
    for i, word in enumerate(name1):
        if ':' in word:
            name1[i] = word.replace(':', '')
    for i, word in enumerate(name2):
        if ':' in word:
            name2[i] = word.replace(':', '')     
    matches = set_similarity(set(name1), set(name2))
    total = min(len(name1), len(name2))
    return matches/total

def set_similarity(set1: set, set2: set) -> int:
    """Returns an int similarity from two sets."""
    similarity = 0
    set1_len = len(set1)
    # iterate thru the smaller set
    if set1_len == min(set1_len, len(set2)):
        for tag in set1:
            if tag not in set2:
                continue
            similarity += 1
    else:
        for tag in set2:
            if tag not in set1:
                continue
            similarity += 1
    return similarity