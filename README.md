# Cálculo de Infiltração do Solo pelo Método de Horton

Este projeto em Python aplica o método de Horton para ajustar parâmetros de um modelo de infiltração baseado em dados de tempo e infiltração total.

## Estrutura do Código

### Bibliotecas
- **math**: operações matemáticas básicas.
- **scipy.optimize**: otimização de parâmetros com a função `minimize`.

### Funções Principais
- **calc_corr(tempo, a, fc, f0)**: Calcula o valor corrigido de infiltração com base nos parâmetros.
- **calc_dif2(interm, corr)**: Calcula a diferença ao quadrado entre infiltração intermitente e corrigida.
- **calc_f(tempo, a, fc, f0)**: Calcula o valor da função `f` para o tempo e parâmetros dados.
- **error_function(params, tempos, interms)**: Função de erro a ser minimizada, que acumula o erro quadrado entre valores observados e estimados.

### Entrada de Dados
- Solicita valores iniciais para os parâmetros `a`, `fc` e `f0`.
- Recebe vetores de tempo e infiltração total, a partir dos quais calcula infiltrações intermitentes.

### Geração e Exibição de Tabela
- **gerar_tabela(a, fc, f0, tempos, interms, title)**: Gera e exibe uma tabela com dados de tempo, infiltração total, infiltração intermitente, infiltração corrigida, diferença ao quadrado e valor `f` para os parâmetros especificados.

### Otimização
- Utiliza `scipy.optimize.minimize` para ajustar os valores de `a`, `fc` e `f0` que minimizam o erro da função `error_function`.
- Exibe os parâmetros otimizados e uma nova tabela com os resultados ajustados.

## Como Executar
1. Insira os valores iniciais de `a`, `fc`, e `f0` quando solicitado.
2. Insira os valores de tempo e infiltração total para cada ponto de dados.
3. O programa exibirá as tabelas de resultados iniciais e otimizados.

## Exemplo de Saída
- Valores iniciais de `a`, `fc`, `f0` e tabela correspondente.
- Valores otimizados de `a`, `fc`, `f0` e tabela correspondente com o erro minimizado.
