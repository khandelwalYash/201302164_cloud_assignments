segment .data
    a db  0x1
    b db  0x1
    c db  0x1

segment .text
    global main

main:

   mov rax, [a]
   mov rbx, [b]
   mov rcx, [c]
   add rax, rbx
   add rcx, rax
   mov [c], rcx
