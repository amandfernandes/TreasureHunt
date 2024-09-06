# Caça ao tesouro em Python
Este projeto foi desenvolvido como parte da prova final da disciplina de Programação Estruturada em 2023.2.

### Integrantes
Amanda Fernandes
Paula Luiza

### Descrição do Projeto
O objetivo do projeto é criar um jogo de Caça ao Tesouro por linha de comando. No jogo, o jogador controla um aventureiro (representado pelo símbolo @) que busca um tesouro (representado pelo símbolo X) em um mapa 10 x 10. Durante a exploração, o aventureiro pode encontrar monstros!

### Comandos
O jogador possui os seguintes comandos possíveis, todos controlados pelo teclado:

Teclas W, A, S e D: indicam a movimentação do aventureiro pelo mapa (respectivamente cima, esquerda, baixo e direita); Tecla T: Exibe os atributos do aventureiro; Tecla Q: Sai do jogo. Elementos principais O aventureiro é um dicionário em Python, que possui os seguintes dados:

Nome: informado pelo jogador assim que o jogo começa; Força: um inteiro aleatório entre 10 e 18; Defesa: um inteiro aleatório entre 10 e 18; Vida: um inteiro inicializado aleatoriamente entre 100 e 120; Posição: uma lista com dois elementos, inicializado como [0, 0]; Além disso, o aventureiro possui algumas ações possíveis:

Atacar: retorna um inteiro igual à força mais um valor aleatório entre 1 e 6; Defender: recebe como parâmetro um valor de dano, e reduz desse valor a defesa do aventureiro. O valor final é reduzido da vida atual do aventureiro (se for positivo); Mover: muda as coordenadas do aventureiro, na direção indicada (se possível); Está vivo: retorna um booleano informando se o aventureiro está vivo. O jogo também deve ter pode gerar monstros, que são armazenados em dicionários e que possuem os seguintes dados:

Força: um inteiro aleatório entre 5 e 25 Vida: um inteiro aleatório entre 10 e 100 Além disso, o monstro possui algumas ações possíveis:

Atacar: retorna um inteiro igual à força; Defender: recebe como parâmetro um valor de dano. O valor recebido é reduzido da vida atual do monstro; Está vivo: retorna um booleano informando se o mosntro está vivo. Por fim, o jogo ainda possui um dicionário para o tesouro, que tem um único atributo posicao, que corresponde a uma lista com dois inteiros.

### Mecânica
O jogo se passa em um mapa de dimensão 10 x 10. O aventureiro sempre começa na posição [0, 0], e o tesouro em uma posição aleatória no mapa (exceto a posição [0, 0]). O aventureiro é representado pelo caractere @, e o tesouro pelo caractere X.

Em cada rodada, o aventureiro pode fazer uma de quatro ações:

Mover-se: utilizando as teclas W, A, S e D, o aventureiro se move pelo mapa (ver efeito disso a seguir); Ver atributos: verifica força, defesa e vida do aventureiro; Sair do jogo: utilizando a tecla Q, o jogador foge e o jogo encerra. Movimentando Ao movimentar o aventureiro, o jogo deve recalcular a sua coordenada baseado na direção que ele se moveu. O aventureiro não pode se mover para as extremidades do mapa (sua posição não pode ser inferior a 0 e nem superior a 9).

Caso o aventureiro realmente se mova, um de dois efeitos podem ocorrer:

Nada (60%): simplesmente nada acontece, e o aventureiro anda para a nova posição; Monstro! (40%): um novo monstro surge para lutar contra o aventureiro! Veja a seção abaixo. No final do efeito selecionado, se o aventureiro estiver vivo, o mapa é redesenhado com o aventureiro na nova posição.

### Mecânica Adicional:   
Será possivel escolher entre os niveis fácil, normal ou dificil, tendo uma quantidade x de turno para vencer. 

No nível fácil o jogador possui jogadas praticamente ilimitadas (999 rodadas);
No nível normal o jogador tem 20 jogadas para vencer;
No nível difícil o jogador tem 10 jogadas para vencer.

### Combate
O combate se dá nas seguintes ações:

Fase do aventureiro: ataca, armazenando o dano; Fase do monstro: defende, atualizando a vida dele; Fase do monstro: ataca, armazenando o dano; Fase do aventureiro: defende, atualizando a vida dele. O combate encerra assim que um dos dois, aventureiro ou monstro, chega a uma vida menor que zero.

### Encerramento
O jogo acaba quando (a) o aventureiro morre, ou (b) o aventureiro chega no tesouro.



