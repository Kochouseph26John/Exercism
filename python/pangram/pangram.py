def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in sentence:
            return False
    return True
    pass
