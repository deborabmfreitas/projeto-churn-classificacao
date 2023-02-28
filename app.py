import gradio as gr
import joblib as jb

def predict(RowNumber, CustomerId, Surname, CreditScore, Geography,
       Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard,
       IsActiveMember, EstimatedSalary):

    model = jb.load('model.pkl')

    RowNumber = int(RowNumber)
    CustomerId = int(CustomerId)
    CreditScore = int(CreditScore)
    Age = int(Age)
    Tenure = int(Tenure)
    Balance = float(Balance)
    NumOfProducts = int(NumOfProducts)
    HasCrCard = int(HasCrCard)
    IsActiveMember = int(IsActiveMember)
    EstimatedSalary = float(EstimatedSalary)

    p = model.predict_proba([[RowNumber, CustomerId, Surname, CreditScore, Geography,
       Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard,
       IsActiveMember, EstimatedSalary]])[0]
    return {'Not churn':p[0], 'Churn':p[1]}


input = ['number', 'number', gr.Textbox(), 'number', gr.Dropdown(choices=['France','Germany','Spain']), gr.Dropdown(choices=['Male','Female']),
          'number', 'number','number','number','number','number','number']

demo = gr.Interface(fn=predict, inputs=input, outputs='label')
demo.launch()