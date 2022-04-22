def loader(outdir, output, out_offset, filename="output"):
    out = open(outdir + filename + str(out_offset) + '.txt', 'w')
    out.write(output)
    out.close()

