def is_anagram(string1, string2):
    str1, str2 = string1.lower(), string2.lower()
    for ch in [',', ' ', '"', "'"]:
        str1, str2 = str1.replace(ch, ''), str2.replace(ch, '')
    if len(str1) != len(str2):
        return False

    listr2 = list(str2)

    for c1 in str1:
        if c1 not in listr2:
            return False
        else:
            listr2.remove(c1)
    return True
