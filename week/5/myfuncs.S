section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

	mov r11, 0	; r8 is ctr, init to 0
loops:
	cmp r11, rdx	; compares ctr to strlen
	jge end		; leave if condition not met
	mov [rdi], sil	; set str to char
	add rdi, 1	;inc str pointer
	add r11, 1	; inc ctr
	jmp loops	; loop
end:
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame


	mov r11, 0	; r8 is ctr, init to 0
loops2:
	cmp r11, rdx	; compares ctr to strlen
	jge end2		; leave if condition not met
	mov rax, [rsi]	;load src
	mov [rdi], al	; set dst to char
	add rdi, 1	;inc str pointer
	add rsi, 1	; inc str pointer
	add r11, 1	; inc ctr
	jmp loops2	; loop
end2:
     


        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!

