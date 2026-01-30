'''
Docstring for chatbot
steps:
1. input 
2. process / decide
3. output
'''

greet_words = ['hi', 'hello', 'yo', 'hey']
bye_words = ['bye', 'good bye', 'ta ta']
bad_words = ['dog', 'pocha', 'faul']


def listen():
    return input('Say Something: ')


def decide(command):
    # print(command)
    command = command.lower()
    broken_words = command.split(" ")
    # print(broken_words)

    for word in broken_words:
        if word in greet_words:
            talkback('Hi Man')
            break

        elif word in bye_words:
            talkback('Ok, ta ta.')
            break

        elif word in bad_words:
            talkback("You talk badly, you are bad guy. Behave yourself!")

def talkback(response):
    print(response)


while True:
    command = listen()
    decide(command)