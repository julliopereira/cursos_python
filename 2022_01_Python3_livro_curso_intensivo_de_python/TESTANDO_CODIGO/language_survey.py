# PROGRAMA QUE UTILIZE A CLASSE SURVEY

from survey import AnonymousSurvey

# Define uma pergunta e cria uma pesquisa
question = "What language did you first learn to speak? "
my_survey = AnonymousSurvey(question)

# Mostra a pergunta e armazena as respostas à pergunta
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

#Exibe o resultado das pesquisas
print("\nObrigado a todos por participar!!")
my_survey.show_results()


