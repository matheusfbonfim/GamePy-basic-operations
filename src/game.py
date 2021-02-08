from models.calcular import Calcular

def main() -> None:
    pontos: int = 0

    # Chama a função para começar o jogo
    jogar(pontos)

def jogar(pontos: int) -> None:
    # Entrada com o valor de dificulidade
    dificuldade: int = int(input("Informe o nivel de dificuldade desejado [1, 2, 3 ou 4]: "))

    # Instancia do objeto Calcular
    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao() # 5 + 4 = ?

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} pontos')

    continuar: int = int(input("Deseja continuar no jogo? [1 - sim,  0 - não]: "))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s)')
        print("Até a próxima")


if __name__ == '__main__':
    main()
