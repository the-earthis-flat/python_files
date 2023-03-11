from newspaper import Article
import random
import string
import numpy as np
import warnings
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn .metrics.pairwise import cosine_similarity
warnings.filterwarnings("ignore")

#download the punkt package
nltk.download('punkt', quiet=True)

#Get the artical
article = Article('https://www.iflscience.com/odds-of-a-quantum-tunneling-event-are-one-in-a-hundred-billion-67820','https://science.nasa.gov/astrophysics/focus-areas/what-is-dark-energy', 'https://science.nasa.gov/astrophysics')
article.download()
article.parse()
article.nlp()
corpus = article.text



#tokenization
text = corpus
sentence_list = nltk.sent_tokenize(text) #list of sentences

#a function to return a random greeting resonse to a user's greeting
def greeting_response(text):
    text = text.lower()

    #Bots greeting response
    bot_greetings = ["Hello, how may I help you?"]
    #uses greeting response
    user_greetings = ['howdy','hello', 'hey', 'how are you', 'hi', 'whats up', "what's up", "hows it going", "how is it going?", "how's it going", "hows it going?", "hola"]

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)
    
def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                #Swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp

    return list_index
    
#create the bots response
def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ' '
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1],cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0

    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response+" "+sentence_list[index[i]]
            response_flag = 1
            j = j+1
        if j > 2:
            break
    
    if  response_flag == 0:
        bot_response = bot_response+" "+"I apologize, but I don't understand this yet."

    sentence_list.remove(user_input)
    return bot_response

#start Chat
print("lmm-Bot: I am a Chat Bot owned by 'lmm', and I will answer your queries as much as to my knowledge (Remember, I am still learning). If you would like to Exit, please type 'bye' to leave this chat.")

exit_list = ['exit', 'see you later', 'bye', 'break', 'end', 'quit', 'close']

while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print("lmm-Bot: Hope we can talk again")
        break
    else:
        if greeting_response(user_input) != None:
            print("lmm-Bot: "+ greeting_response(user_input))
        else:
            print('lmm-Bot: ' + bot_response(user_input))