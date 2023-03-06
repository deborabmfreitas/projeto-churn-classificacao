# Previsão de Churn

![img](img/img1.jpg)

Foi requisitado um modelo de performance para a identificação de clientes em churn. O projeto foi separado em sprints, seguindo a ideia trabalhada na abordagem SCRUM. Os dados foram obtidos pelo [Kaggle](https://www.kaggle.com/datasets/mervetorkan/churndataset).  

# Visão geral

Após o entendimento do negócio, o **recall** foi utilizado como métrica para treinar os modelos, pois nesse caso, **é mais importante detectar todos os possíveis clientes que serão churn do que fazer classificações precisas**. O fato dos dados serem desbalanceados também indica que a métrica de acurácia seria enviesada.

Pelo fato de estarem desbalanceados, no treinamento dos algoritmos foi acrescentado o argumento `class_weight = 'balanced'`, que determina pesos de acordo com a proporção de instâncias para as classes. A classe que representa o churn '1' recebeu o maior peso.

Além disso, foram utilizados transformadores customizados para a preparação dos dados e todo o workflow do projeto foi automatizado com **pipelines**.

Após a escolha do melhor modelo, que no projeto foi o Random Forest Classifier, foi feita a otimização dos hiperparâmetros utilizando o módulo `RandomizedSearchCV`.


# Organização das atividades


## 1. Objetivos da Sprint 1

- Descrição dos dados
- Análise geral dos dados
- Planejamento e substituições de NA
- Lista de hipóteses
- Split do dataset


## 2. Objetivos da Sprint 2
- EDA
- Data preparation

## 3. Objetivos da Sprint 3

- Implementação dos algoritmos de Machine learning
- Métricas de performance
- Avaliação final


## 4. Objetivos da Sprint 4

- Deploy do modelo


# Descrição dos dados

Coluna | Descrição
-------|----------
RowNumber | Nº da linha
CustomerId | ID do cliente
Surname | Sobrenome do cliente
CreditScore | Pontuação de crédito do cliente para o mercado de consumo
Geography | País onde o cliente reside
Gender | Gênero do cliente
Age | Idade do cliente
Tenure| Nº de meses que o cliente permaneceu ativo
Balance  | Valor gasto pelo cliente
NumOfProducts | Nº de produtos comprados pelo cliente
HasCrCard | Indica se o cliente possui ou não um cartão de crédito
IsActiveMember | Indica se o cliente ainda tem o cadastro ativo na empresa
EstimatedSalary | Estimativa de salário mensal do cliente
Exited | Indica se o cliente está ou não em churn 


# Algoritmos de Machine learning

- LogisticRegression
- SVM
- Random Forest Classifier

# Ferramentas e métodos
- Python
- Principais frameworks/bibliotecas: Pandas, Matplotlib, Seaborn e Scikit-learn
- Jupyter Notebook (projeto) e VSCode (README)
- Git e GitHub

# Performance do modelo

<div align="center">

Modelo | Accuracy | Recall | Precision
-------|----------|--------| ----------
RFC | 0.79	| **0.73224** | 0.489051

</div>


# Deploy

Foi feito um [deploy](https://huggingface.co/spaces/deborabmfreitas/churn-prediction-deploy) utilizando o Hugging Face. 
 
Clique [aqui](https://github.com/deborabmfreitas/projeto-churn-classificacao/blob/main/churn-prediction-project.ipynb) para visualizar mais detalhes do projeto.