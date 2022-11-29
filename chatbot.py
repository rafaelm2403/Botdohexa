from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'Richarlison',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Ainda não aprendi uma resposta para isso.',
            'maximum_similarity_threshold': 0.65
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

training_data_quesans = open('treinamento/perguntas_respostas.txt').read().splitlines()
training_data_personal = open('treinamento/perguntas_pessoais.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer = ListTrainer(chatbot)
trainer.train(training_data)

trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.portuguese'
    ) 