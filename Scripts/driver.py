from trans1 import transform1
from trans2 import transform2
from extractor import extractor
from loader import loader


def driver(inpdir, outdir, choice, inp_offset='', out_offset=''):
    inp = extractor(inpdir, inp_offset)

    if choice == 1:
        output = transform1(inp)
        loader(outdir, output, out_offset)

    else:
        output = transform2(inp)
        loader(outdir, output, out_offset)

    inp.close()


