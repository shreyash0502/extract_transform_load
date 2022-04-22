def transform1(inp):
    outline = ''
    for line in inp:
        words = line.split(' ')
        for word in words:
            word = word.capitalize()
            outline = outline + ' ' + word
        outline = outline.lstrip(' ')
        outline += '\n'
    return outline
