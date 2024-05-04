# Avaliação EDAA
[![wakatime](https://wakatime.com/badge/user/939444ec-3797-43ff-bb09-6e41081ae12c/project/1108851a-06f6-4e4f-95da-f74104897feb.svg)](https://wakatime.com/badge/user/939444ec-3797-43ff-bb09-6e41081ae12c/project/1108851a-06f6-4e4f-95da-f74104897feb)

## 1) Objetivo
A utilização de arranjos estáticos ou estruturas de dados lineares e não-lineares têm
vantagens e desvantagens de acordo com o problema que está sendo resolvido. Por vezes, a
manipulação dos dados (inserção e remoção, por exemplo) é mais otimizada. 

Porém, busca e ordenação, podem ser menos custosas utilizando vetores.

Esta atividade individual consiste em implementar e comparar a eficiência dos seguintes
métodos de busca considerando arranjos estáticos e estruturas de dados lineares e não não-lineares com valores inteiros:

- Arranjos estáticos: busca sequencial padrão e busca binária.
- Estruturas lineares e não-lineares: busca sequencial em lista ligada e busca em
árvores binárias de busca.

## 2) Casos de Teste
Para realizar a comparação, devem ser gerados diferentes cenários de teste aleatórios
variando-se o tamanho do arranjo de 100 mil a 1 milhão de elementos únicos, em intervalos de 100
mil. 

Os mesmos cenários devem ser utilizado para todos os algoritmos.

Calcular média e desvio padrão para o número de comparações, o tempo de execução e o
consumo de memória considerando:

- O pior caso, com 3 execuções de cada;
- Casos aleatórios: 100 buscas para cada cenário.

## 3) Execução

- A linguagem de programação é livre;
- Os valores não devem se repetir;
- O custo de criação das estruturas deve ser descartado (alocação do vetor, criação das listas e árvores);
- O custo de ordenação, quando necessário, deve ser computado no custo total, mas registrado e discutido individualmente.
    - Utilize um método de ordenação disponível na linguagem e descreva o seu
funcionamento detalhado no relatório;
- Se o tempo de execução for muito pequeno, pode-se incluir um custo constante em cada
comparação da chave de busca com o elemento do arranjo.
