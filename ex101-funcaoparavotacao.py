def voto(ano):
    from datetime import date # Importando a biblioteca dentro da função def, a biblioteca somente será executada
                            # quando o programa for iniciado, desta maneira economiza muita memória
    data_atual = date.today().year
    idade = data_atual - ano
    if idade < 16:
        return f'Com {idade} anos: Voto negado!'
    elif 16 <= idade < 18 or idade > 65:
        return f' Com {idade} anos: Voto opcional!'
    else:
        return f'Com {idade} anos: Voto obrigatório'


ano_nasc = int(input('Digite o ano de seu nascimento: '))
print(voto(ano_nasc))
