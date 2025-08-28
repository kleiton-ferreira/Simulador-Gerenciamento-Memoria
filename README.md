# Simulador-Gerenciamento-Memoria

Este projeto implementa um simulador de alocação de memória em Python, utilizando três algoritmos clássicos de gerenciamento:

- First Fit → Aloca no primeiro espaço livre encontrado.

- Best Fit → Aloca no menor espaço livre possível que comporte o processo.

- Worst Fit → Aloca no maior espaço livre disponível.

O simulador mostra o estado da memória após cada alocação e liberação de processos, permitindo visualizar o comportamento de cada estratégia e os efeitos da fragmentação.

## 🛠️ Tecnologias utilizadas

- Python 3.x → Linguagem principal do projeto.

- time (módulo padrão) → Utilizado para pausas entre as operações e melhor visualização do fluxo.

## 📂 Estrutura do projeto

📦 simulador-memoria

 ┣ 📜 memoria.py          # Classe Memoria: gerencia blocos e processos
 
 ┣ 📜 algoritmos.py       # Implementação dos algoritmos First Fit, Best Fit e Worst Fit
 
 ┣ 📜 main.py             # Script principal para rodar a simulação
 
 ┗ 📜 README.md           # Documentação do projeto

 
## ▶️ Como rodar o projeto

- Clone o repositório
- Instale o Python e o Pycharm
- Abra o projeto no Pycharm
- Execute o arquivo "main.py"
