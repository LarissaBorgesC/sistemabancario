# Sistema Bancário Básico

Este é um sistema bancário básico implementado em **Python**, projetado para simular operações de uma conta bancária por meio de uma interface de console interativa. O programa permite realizar depósitos, saques e consultar o extrato, com validações para garantir a consistência das operações.

## Funcionalidades

O sistema oferece as seguintes operações:

1. **Depósito** (`d`):
   - Aceita valores positivos para depósito.
   - Adiciona o valor ao saldo e registra a transação no extrato no formato: `Depósito: R$ + X.XX`.
   - Exibe mensagem de erro para valores não positivos.

2. **Saque** (`s`):
   - Permite até **3 saques diários**, cada um com limite máximo de **R$500,00**.
   - Verifica se o saldo é suficiente, se o valor do saque excede o limite e se o número máximo de saques foi atingido.
   - Registra saques no extrato no formato: `Saque: R$ - X.XX`.
   - Exibe mensagens de erro para saldo insuficiente, limite excedido, número máximo de saques atingido ou valores não positivos.

3. **Extrato** (`e`):
   - Exibe o histórico de todas as transações (depósitos e saques).
   - Mostra o saldo atual no formato: `Saldo: R$ X.XX`.
   - Exibe mensagem de "Não foram realizados movimentações" se o extrato estiver vazio.

4. **Sair** (`q`):
   - Encerra o programa com uma mensagem de despedida.

## Estrutura do Código

- **Linguagem**: Python 3.x
- **Dependências**: Nenhuma (não utiliza módulos externos).
- **Restrições**:
  - Utiliza apenas operadores de comparação (`==`, `>`, `<`, `>=`) e repetição (`while`).
  - Não utiliza funções, conforme o design simplificado.
  - Usa **f-strings** para formatação de strings.
- **Organização**:
  - Um loop `while` gerencia o menu principal.
  - Blocos condicionais (`if`/`elif`) controlam as operações de depósito, saque, extrato e saída.
  - Variáveis globais armazenam o estado: `saldo`, `extrato`, `numero_saques`, `limite_valor`, `limite_saques`.
  - Tratamento de erros com `try-except` implícito na conversão de entrada para `float`.

## Como Executar

### Pré-requisitos
- Python 3.x instalado (verifique com `python --version` ou `python3 --version`).
- Nenhuma biblioteca externa é necessária.

### Passos
1. Salve o código em um arquivo chamado `sistemabancario.py`.
2. Abra o terminal na pasta onde o arquivo está localizado.
3. Execute o programa com o comando:
   ```bash
   python sistemabancario.py
   ```
- Siga as instruções no console, digitando `d` para depósito, `s` para saque, `e` para extrato ou `q` para sair.


