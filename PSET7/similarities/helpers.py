from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""
    # Turn split versions of both files into sets to remove duplicates
    # Split Lines used to automatically split at the end of a line. No need for "\n" this way
    a1 = set(a.splitlines())
    b1 = set(b.splitlines())

    return a1 & b1


def sentences(a, b):
    """Return sentences in both a and b"""
    # Tokenize has the ability to separate, in this case, sentences by finding relevant symbols (.,!,?,etc) in text
    aS1 = set(sent_tokenize(a))
    bS1 = set(sent_tokenize(b))

    return aS1 & bS1


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    # Create empty lists
    c = []
    d = []
    # Append in new lists the length of the selected string based on user input
    # Loop looks at each character while staying within length of specified substring size
    for i in range(len(a) - n + 1):
        c.append(a[i:i+n])

    for i in range(len(b) - n + 1):
        d.append(b[i:i+n])

    # Lists of substrings are turned into sets to remove duplicates
    setA = set(c)
    setB = set(d)

    return setA & setB
