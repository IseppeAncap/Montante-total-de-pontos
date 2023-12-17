def points(games):
    tot = 0 
    """Calcula a pontuação total de uma equipe com base nos resultados dos jogos.

    Args:
        onde x é o número de gols da equipe da casa e y é o número de gols da equipe visitante.

    Returns:
        int: A pontuação total da equipe calculada de acordo com as regras:
        - Vitória: 3 pontos
        - Empate: 1 ponto
        - Derrota: 0 pontos
        
    Version 1.0 não há uma conversão para um int 
    Autor Dev Iseppe libertário
    """
    for score in games:
        if score[0] > score[2]:
            tot +=3
        elif score[0] == score[2]:
            tot +=1
    return tot 
print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))#deve retornar, 30)
print(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']))#Deve retornar, 10)
print(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']))#Deve reornar, 0)
print(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']))# Deve retornar, 15)
print(points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']))# Deve retornar 12)