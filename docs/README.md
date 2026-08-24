# 🧠 testeTuringUSP

[![GitHub license](https://img.shields.io/github/license/clcmo/testeTuringUSP?style=for-the-badge)](https://github.com/clcmo/testeTuringUSP)
[![GitHub stars](https://img.shields.io/github/stars/clcmo/testeTuringUSP?style=for-the-badge)](https://github.com/clcmo/testeTuringUSP/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/clcmo/testeTuringUSP?style=for-the-badge)](https://github.com/clcmo/testeTuringUSP/network)
[![GitHub issues](https://img.shields.io/github/issues/clcmo/testeTuringUSP?style=for-the-badge)](https://github.com/clcmo/testeTuringUSP/issues)
[![GitHub donate](https://img.shields.io/github/sponsors/clcmo?color=pink&style=for-the-badge)](https://github.com/sponsors/clcmo)

Projeto desenvolvido como parte dos estudos e desafios relacionados a **Inteligência Artificial, Análise de Dados e Lógica de Programação**, explorando desde a resolução de problemas em Python até a construção de análises e modelos preditivos.

O projeto reúne diferentes etapas do processo de desenvolvimento e investigação de dados, incluindo **limpeza, tratamento, exploração e modelagem**, além de exercícios de lógica e materiais de apoio.

## 📌 Sobre o projeto

O repositório está organizado em diferentes frentes:

* **Análise de Dados e IA:** exploração e preparação de dados, tratamento de inconsistências, identificação de outliers e construção de modelos preditivos;
* **Lógica de Programação:** resolução de desafios e exercícios utilizando Python;
* **Documentação:** registros das decisões, objetivos e materiais relacionados ao desenvolvimento;
* **Turing Talks:** materiais complementares relacionados ao projeto.

Um dos principais objetivos da etapa de análise é investigar como **fatores socioeconômicos e hábitos de estudo** podem estar relacionados ao desempenho acadêmico dos estudantes, utilizando `final_exam_score` como variável-alvo. A modelagem utiliza ferramentas do ecossistema Python, incluindo **Scikit-Learn**.

## 🗂️ Estrutura do projeto

```text
testeTuringUSP/
│
├── analise/
│   ├── analise_e_predicao.ipynb
│   ├── clean.py
│   ├── objetivos.md
│   ├── raciocionio.md
│   └── setup.py
│
├── docs/
│   ├── README.md
│   └── SECURITY.md
│
├── logica/
│   ├── desafio.py
│   ├── q1.py
│   ├── q2.py
│   └── q3.py
│
├── turingtalks/
│   └── turing_talks.pdf
│
├── .github/
├── .gitignore
├── .releaserc.json
├── LICENCE
├── package.json
└── struct.md
```

## 🔬 Análise de Dados e IA

A pasta [`analise/`](./analise) concentra a etapa dedicada à análise dos dados.

Entre as atividades desenvolvidas estão:

1. **Carregamento e inspeção dos dados**
2. **Limpeza e preparação do dataset**
3. **Tratamento de valores ausentes**
4. **Identificação e tratamento de inconsistências**
5. **Análise de outliers**
6. **Exploração das variáveis**
7. **Investigação de relações entre características dos estudantes e desempenho acadêmico**
8. **Construção de modelos preditivos com Scikit-Learn**

### 🧹 Tratamento dos dados

Durante a preparação dos dados, são consideradas situações como:

* remoção de identificadores sem valor preditivo;
* tratamento de valores fisicamente ou semanticamente inconsistentes;
* conversão de valores inválidos para `NaN`;
* imputação de valores ausentes;
* utilização da **mediana** para variáveis numéricas;
* utilização da **moda** para variáveis categóricas.

As decisões adotadas durante essa etapa estão documentadas em [`analise/raciocionio.md`](./analise/raciocionio.md).

## 🐍 Tecnologias e ferramentas

* **Python**
* **Jupyter Notebook**
* **Scikit-Learn**
* **Pandas**
* **NumPy**
* **Análise e visualização de dados**
* **Git e GitHub**

## ▶️ Como executar

### Pré-requisitos

Recomenda-se ter instalado:

* Python 3.x
* Git
* Jupyter Notebook ou JupyterLab

### Clonar o repositório

```bash
git clone https://github.com/clcmo/testeTuringUSP.git
cd testeTuringUSP
```

### Executar a análise

A análise principal pode ser encontrada em:

```text
analise/analise_e_predicao.ipynb
```

O notebook pode ser executado localmente através do Jupyter ou em um ambiente compatível com notebooks Python.

## 📚 Documentação

Alguns materiais importantes do projeto:

* [`analise/objetivos.md`](./analise/objetivos.md) — objetivos da etapa de análise;
* [`analise/raciocionio.md`](./analise/raciocionio.md) — justificativas das decisões de limpeza dos dados;
* [`struct.md`](./struct.md) — estrutura do projeto;
* [`docs/`](./docs) — documentação complementar.

## 🎯 Objetivos de aprendizagem

Este projeto busca desenvolver conhecimentos práticos em:

* análise exploratória de dados;
* preparação e limpeza de datasets;
* raciocínio lógico e resolução de problemas;
* programação em Python;
* fundamentos de Machine Learning;
* construção e avaliação de modelos preditivos;
* documentação e organização de projetos;
* utilização do Git e GitHub em projetos técnicos.

## 🚧 Status

**Em desenvolvimento.**

O projeto pode receber novas análises, experimentos, modelos e documentação ao longo do processo de aprendizagem.

## 🤝 Contribuições

Sugestões, correções e melhorias são bem-vindas.

Para contribuir:

1. Faça um fork do projeto;
2. Crie uma branch para sua alteração;
3. Implemente e documente a melhoria;
4. Faça um commit;
5. Abra um Pull Request.

## 📄 Licença

Este projeto está distribuído sob a licença **MIT**. Consulte o arquivo [`LICENCE`](./LICENCE) para mais informações.

---

**Desenvolvido por [Camila Oliveira](https://github.com/clcmo).**
