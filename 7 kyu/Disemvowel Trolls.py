def disemvowel(string):
    remove = string.translate(str.maketrans('', '', 'aeiouAEIOU'))
    return remove