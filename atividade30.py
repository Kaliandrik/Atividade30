# crie uma duncao que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7

def media(nota1,nota2,nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media
def verificaraprovados(media):
    if media >= 7:
      return "Aprovado"
    else:
        return "Reprovado"

nota1 = int(input("DIGITE SUA NOTA:"))
nota2 = int(input("DIGITE SUA NOTA:"))
nota3 = int(input("DIGITE SUA NOTA:"))

mediafinal = media(nota1, nota2, nota3)
print(mediafinal)

verificar = verificaraprovados(mediafinal)
print(verificar)
