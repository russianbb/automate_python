import random

capitals = {
    'Acre (AC)' : 'Rio Branco',
    'Alagoas (AL)' : 'Maceió',
    'Amapá (AP)' : 'Macapá',
    'Amazonas (AM)' : 'Manaus',
    'Bahia (BA)' : 'Salvador',
    'Ceará (CE)' : 'Fortaleza',
    'Distrito Federal (DF)' : 'Brasília',
    'Espírito Santo (ES)' : 'Vitória',
    'Goiás (GO)' : 'Goiânia',
    'Maranhão (MA)' : 'São Luís',
    'Mato Grosso (MT)' : 'Cuiabá',
    'Mato Grosso do Sul (MS)' : 'Campo Grande',
    'Minas Gerais (MG)' : 'Belo Horizonte',
    'Pará (PA)' : 'Belém',
    'Paraíba (PB)' : 'João Pessoa',
    'Paraná (PR)' : 'Curitiba',
    'Pernambuco (PE)' : 'Recife',
    'Piauí (PI)' : 'Teresina',
    'Rio de Janeiro (RJ)' : 'Rio de Janeiro',
    'Rio Grande do Norte (RN)' : 'Natal',
    'Rio Grande do Sul (RS)' : 'Porto Alegre',
    'Rondônia (RO)' : 'Porto Velho',
    'Roraima (RR)' : 'Boa Vista',
    'Santa Catarina (SC)' : 'Florianópolis',
    'São Paulo (SP)' : 'São Paulo',
    'Sergipe (SE)' : 'Aracaju',
    'Tocantins (TO)' : 'Palmas'
}

for quizNum in range(35):
    #Create the quiz and answer files
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')
    
    #Write out the header for the quiz file
    quizFile.write('Nome:\n\nData:\n\nSemestre:\n\n')
    quizFile.write((' '* 20) + f'Quiz das Capitais de Estados (Form{quizNum + 1})')
    quizFile.write('\n\n')
    
    #Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)
    
    #Loop throught all the 27 states, making a question for each
    for questionNum in range(27):
        
        #Get the right and wrong answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answersOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answersOptions)
        
        #Write the question and the answer options
        quizFile.write(f'{questionNum + 1}. Qual a capital de {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}. { answersOptions[i]}\n")
        
        quizFile.write('\n')
        
        #Write the answer key to a file
        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answersOptions.index(correctAnswer)]}\n")
        
    quizFile.close()
    answerKeyFile.close()
            
            
        