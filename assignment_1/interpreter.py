# Current Scenario - Adding two numbers and then converting the 32-bit.asm file to 64-bit.asm via interpreter
# Reduced Case - Since for adding two numbers and then storing the result in another variable the use case is limited.
# The only instruction that will get used in this case are mov and add. The only sections needed will be .text (for instructions)
# and .data (for the 3 variables that we will use)

import sys
import fileinput
import re

# Replace all the 32-bit register types with 64-bit register types, i.e register of types e[*]x with type r[*]x
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
