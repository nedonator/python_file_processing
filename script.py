import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input')
parser.add_argument('-o', '--output')
parser.add_argument('-n', type=int)
parser.add_argument('-b', '--buffer', type=int)  # speed optimization
args = parser.parse_args()

input = open(args.input, encoding='utf-8') if args.input else sys.stdin
output = open(args.output, 'w', encoding='utf-8') if args.output else sys.stdout
n = args.n if args.n else 10
buffer_size = args.buffer if args.buffer else 10000

output_buffer = []
for line in input:
    for word in line.split():
        if len(word) > n:
            output_buffer.append(line)
            break
    if len(output_buffer) > buffer_size:
        output.writelines(output_buffer)
        output_buffer.clear()

output.writelines(output_buffer)

if args.input:
    input.close()
if args.output:
    output.close()
