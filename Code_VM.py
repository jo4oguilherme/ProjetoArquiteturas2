
run = True      # Variavel Booleana para o Loop While
instr = ""		# Recebe cada linha do arquivo Binario.txt
instr_type = "" # Recebe as duas primeiras posição do vetor instr, indicando a operação a ser realizada
data1 = 0 		# Recebe o valor do endereço data_A
data2 = 0 		# Recebe o valor do endereço data_B
data_A = 0		# Recebe o endereço da variavel A
data_b = 0		# Recebe o endereço da variavel B
data_C = 0		# Recebe o resultado da operação
PC=0			# Contador


arqProg = open("Binario.txt", "r") 	# Le o arquivo Binario.txt
prog = arqProg.read().split("\n") 	# Recebe todo o conteudo do arquivo Binario.txt

arqMem = open("Memoria.txt", "r")	# Le o arquivo Memoria.txt
mem = arqMem.read().split("\n")		# Recebe todo o conteudo do arquivo Memoria.txt

while run:						# Loop Infinito
    instr = prog[PC]			# Recebe a linha na posição PC 
    PC = PC + 1					# PC é incrementado
    
	if len(instr)==0: break		# Verifica se encontrou uma linha vazia
	
    instr_type = instr[0:2]		
    data_A = int(instr[2:6],2)	# Recebe o endereço da variavel A
	data_B = int(instr[6:10],2)	# Recebe o endereço da variavel B
    data1 = int(mem[data_A])	# Recebe o valor do endereço data_A
	data2 = int(mem[data_B])	# Recebe o valor do endereço data_B
	
    if instr_type == "00": 		# Faz a adição
        data_C = data_A + data_B
    elif instr_type == "01":	# Faz a Subtração
        data_C = data_A - data_B
    elif instr_type == "10":	# Faz a Divisão
        data_C = data_A / data_B
    elif instr_type == "11":	# Faz a Multiplicação
        data_C = data_A * data_B

    print("C: ", data_C)		# Escreve C
	