import re


def transform2(inp):
    final = dict()
    for line in inp:
        words = line.split()
        for word in words:
            word = word.lower()
            if word in final:
                final[word] += 1
            else:
                final[word] = 1
    output = str(final)
    output = re.sub("[{}]", '', output)
    output = re.sub(r"(\d), ", r"\1\n", output)
    # output = output.group(0)
    # output = re.sub(",", "\n", output)
    return output

