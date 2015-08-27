# TO convert 32_bit.asm to 64_bit. when interpreter.py is run 32_bit.asm gets converted to 64 bit assembly and gets saved 
# in 32_bit.asm only. 

# The only instruction that will get used in this case are mov and add. The only sections needed will be .text (for instructions)
# and .data (for the 3 variables that we will use)

import sys
import fileinput
import re

# Change 32-bit registers to 64-bit registers .Eg change eax to rax i.e. e*x to r*x
for line in fileinput.input('32_bit.asm', inplace=1):
    line = re.sub('eax','rax', line.rstrip())
    line = re.sub('ebx','rbx', line.rstrip())
    line = re.sub('ecx','rcx', line.rstrip())
    line = re.sub('edx','rdx', line.rstrip())
    line = re.sub('esi','rsi', line.rstrip())
    line = re.sub('ebp','rbp', line.rstrip())
    line = re.sub('edi','rdi', line.rstrip())
    line = re.sub('esp','rsp', line.rstrip())
    print(line)
