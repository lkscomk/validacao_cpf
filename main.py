def validarcpf(cpf = None):
    if (not cpf):
      return 'Ausência de CPF.'

    if (len(cpf) <= 10 or len(cpf) >= 12):
      return 'CPF não tem o número de 11 caracteres.'

    resultado = 0
    for x in range(len(cpf[0:9])):
        resultado += int(cpf[x]) * (10 - x)

    modulo = resultado % 11

    final = 0 if (11 - modulo) >= 10 else 11 - modulo

    seg_resultado = 0
    for x in range(len(cpf[0:10])):
        seg_resultado += int(cpf[x]) * (11 - x)

    seg_modulo = seg_resultado % 11

    seg_final = 0 if (11 - seg_modulo) >= 10 else 11 - seg_modulo

    finalizacao = True if (str(final) +
                           str(seg_final)) == str(cpf[9:12]) else False

    return finalizacao

#exemplos
print(validarcpf())
print(validarcpf('69024351897778'))
print(validarcpf(''))
print(validarcpf('41865239089'))
print(validarcpf('56947138264'))
print(validarcpf('08975362159'))
