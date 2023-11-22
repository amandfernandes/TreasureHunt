# AP2
# FALTA:

Comandos
O jogador possui os seguintes comandos possíveis, todos controlados pelo teclado:
Tecla I: Abre o menu de itens do aventureiro; (falta fazer usar o item)

Classes
O aventureiro:
Métodos:
Usar item: remove o item da mochila e aplica o seu efeito, a depender do seu tipo:
Tipo Vida: recupera 20 vezes intensidade o valor da vida atual (até a Vida Máxima);
Tipo Força: aumenta permanentemente 1 vez intensidade o valor do atributo Força;
Tipo Defesa: aumenta permanentemente 1 vez intensidade o valor do atributo Defesa;
Além disso, o aventureiro pode carregar itens, que também são uma classe com os seguintes atributos:
Atributos:
Nome: nome do item;
Tipo: classificação do item;
Intensidade: bônus sobre o atributo (a depender do tipo);

Mecânica
Em cada rodada, o aventureiro pode fazer uma de quatro ações:
Usar um item: utilizando a tecla I, o jogo deve exibir a lista de itens, e o aventureiro pode escolher um para ser usado. Caso um item seja selecionado para usar, realiza a ação dele e remove o item da mochila;
Ver atributos: verifica força, defesa e vida do aventureiro;


Movimentando
Ao movimentar o aventureiro, o jogo deve recalcular a sua coordenada baseado na direção que ele se moveu. O aventureiro não pode se mover para as extremidades do mapa (sua posição não pode ser inferior a 0 e nem superior a 9).
Caso o aventureiro realmente se mova, um de três efeitos podem ocorrer:
Item! (20%): um dos seguintes itens aparece para o aventureiro, e ele é adicionado à mochila;
Poção de força, intensidade 1 (10% de chance)
Poção de força, intensidade 2 (5% de chance)
Poção de vida, intensidade 1 (50% de chance)
Poção de vida, intensidade 2 (30% de chance)
Poção de defesa, intensidade 1 (5% de chance)


Inventar uma nova mecanica




