segment .data
    x db  0x1
    y db  0x1
    z db  0x1

segment .text
    global main

main:

   mov eax, [z]
   mov ebx, [y]
   mov ecx, [x]
   add eax, ebx
   add ecx, eax
   mov [x], ecx
