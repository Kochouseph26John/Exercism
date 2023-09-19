def translate(t):
    te = []
    for text in t.split():
        if text[0] in ['a','e','i','o','u'] or text.startswith('xr') or text.startswith('yt'):
            pass
        elif 'qu' in text:
            i = text.index('qu')
            text = text[i+2:] + text[0:i+2] 
        else:
            for i, c in enumerate(text):
                if c in 'aeiou':
                    text = text[i:] + text[0:i]
                    break
                elif c == 'y' and i >=1:
                    text = text[i:] + text[0:i] 
                    break
        text=text+'ay'
        te.append(text)
    return " ".join(te)