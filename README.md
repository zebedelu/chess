# Chess

Um jogo de xadrez desenvolvido em Python com foco em **código limpo**, **programação orientada a objetos (POO)** e boa organização de código.

Projeto criado dia 23 de janeiro de 2026, desenvolvido em apenas 3 dias, sem uso de inteligência artificial para codificar por mim, apenas para tirar dúvidas simples.

## Funcionalidades

- Tabuleiro completo de 8x8 com todas as peças do xadrez tradicional.
- Validação completa de movimentos para cada tipo de peça (Peão, Torre, Cavalo, Bispo, Rainha e Rei).
- Detecção de **xeque**, **xeque-mate** e **empate**.
- Interface gráfica simples (usando assets na pasta `assets/` e UI separada).
- Modo Jogador vs Jogador (PvP) — (futuramente: IA simples ou PvE).
- Sistema de regras modular na pasta `rules/`.
- Configurações centralizadas em `configs.py`.

## Tecnologias utilizadas

- **Python 3**
- Bibliotecas: (ex: `pygame` para interface gráfica — confirme/adapte conforme o código)
- Estrutura modular com POO (classes para peças, tabuleiro, jogo e regras).

## Como jogar

1. Clone o repositório:
```bash
git clone https://github.com/zebedelu/chess.git
cd chess
```

Instale as dependências (se necessário):
```bash
pip install pygame-ce
```

Execute o jogo:
```bash
python main.py
```

## Objetivos do projeto

Praticar POO e separação de responsabilidades.
Implementar lógica complexa de regras e validações.
Aprender a trabalhar com assets e interface gráfica.
Manter o código organizado e legível (seguindo boas práticas).

## Status atual
Em desenvolvimento inicial.
Próximos passos:

- Finalizar validação de todos os movimentos especiais (en passant, castling, promoção de peão, check, check-mate).
- Implementar detecção automática de fim de jogo.
- Adicionar IA básica (minimax ou random moves).
- Melhorar interface gráfica.
