# Usage
# python oneliner.py [input_filename]
# Used to Transcript download from https://downsub.com/

import sys

def make_onelines(lines):
    lines = [line.strip() for line in lines]
    new_lines = []
    tmp_line = ""

    for i in range(len(lines)):
        if lines[i] == "":
            continue
        if not lines[i].endswith(('.','?')):
            tmp_line += lines[i]+" "
        else:
            tmp_line += lines[i]
            new_lines.append(tmp_line)
            tmp_line = ""
    return new_lines

with open(sys.argv[1]) as f:
    lines = list(f)
    new_lines = make_onelines(lines)
    print('\n'.join(new_lines))


