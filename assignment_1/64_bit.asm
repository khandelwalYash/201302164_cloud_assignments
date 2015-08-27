segment .data
    x db  0x1
    y db  0x1
    z db  0x1

segment .text
    global main

main:

   mov rax, [z]
   mov rbx, [y]
   mov rcx, [x]
   add rax, rbx
   add rcx, rax
   mov [x], rcx
