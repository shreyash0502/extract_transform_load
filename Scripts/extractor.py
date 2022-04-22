def extractor(inpdir, inp_offset, filename='input'):
    inp = open(inpdir + filename + str(inp_offset) + '.txt', 'r')
    return inp
