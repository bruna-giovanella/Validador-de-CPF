
def validarCPF(cpf):
  cont = 0

  for i in cpf:
    if i in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
      cont += 1
  if cont == 11 and len(cpf) == 11:
    return 1
  else:
    if len(cpf) == 14 and cont == 11 and cpf[3] == '.' and cpf[
        7] == '.' and cpf[11] == '-':
      return 1
    else:
      return 0

cpfBruto = input('cpf: ')
cpf = cpfBruto.replace('.', '').replace('-', '')
print(validarCPF(cpf))


def verificadorDigito(cpf):
  if(validarCPF(cpf) == 1):
    def primeiroDigito(cpf):
        produto = 0
        x = 10
        cpf_Primeiros9digitos = cpf[:9]
       

        for i in cpf_Primeiros9digitos:
          produto += int(i) * x
          x -= 1
        resto = produto % 11
        digitoVerificador = 11 - resto
        

        if digitoVerificador < 10:
            resultado = f'O penúltimo digito verificador é {digitoVerificador}'
        else:
            resultado = 'O penúltimo digito verificador é 0'
            digitoVerificador = 0
        
        
        if digitoVerificador == int(cpf[9]):
          produto2 = 0
          x2 = 11
          cpf_Primeiros10digitos = cpf[:10]
          
          for i in cpf_Primeiros10digitos:
            produto2 += int(i) * x2
            x2 -= 1
          
          resto = produto2 % 11
          digitoVerificador2 = 11 - resto
  
          if digitoVerificador2 < 10:
              resultado2 = f'O último digito verificador é {digitoVerificador2}'
          else:
              resultado2 ='O último digito verificador é 0'
          print(resultado, resultado2)
        else:
          print("cpf invalido")
        

    primeiroDigito(cpf)

verificadorDigito(cpf)
