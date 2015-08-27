segment .data
    a db  0x1
    b db  0x1
    c db  0x1

segment .text
    global main

main:

   mov eax, [a]
   mov ebx, [b]
   mov ecx, [c]
   add eax, ebx
   add ecx, eax
   mov [c], ecx
