from random import randint
from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import json
import re

# load doc into memory
def load_doc(filename):
  # open the file as read only
  file = open(filename, 'r')
  # read all text
  text = file.read()
  # close the file
  file.close()
  return text

# generate a sequence from a language model
def generate_seq(model, tokenizer, seq_length, seed_text, n_words):
  result = list()
  in_text = seed_text
  # generate a fixed number of words
  for _ in range(n_words):
    # encode the text as integer
    encoded = tokenizer.texts_to_sequences([in_text])[0]
    # truncate sequences to a fixed length
    encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
    # predict probabilities for each word
    yhat = model.predict_classes(encoded, verbose=0)
    # map predicted word index to word
    out_word = ''
    for word, index in tokenizer.word_index.items():
      if index == yhat:
        out_word = word
        break
    # append to input
    in_text += ' ' + out_word
    result.append(out_word)
  return ' '.join(result)

def format_text(input_text):
  punc = ['.', '!', '?', '...']
  names = [
    'harry',
    'draco',
    'snape',
    'michael',
    'anthony',
    'goldstein',
    'vernon',
    'russell',
    'crookshanks',
    'mcgonagall',
    'scamander',
    'newt',
    'warren',
    'queenie',
    'ron',
    'fred',
    'remus',
    'clarkson',
    'jack',
    'gary',
    'voldemort',
    'hagrid',
    'trump',
    'donald',
    'tonks',
    'dean',
    'thomas',
    'lupin',
    'elizabeth',
    'luna',
    'harambe',
    'teddy',
    'myrtle',
    'jim',
    'moaning',
    'dumbledore',
    'muggle',
    'salem',
    'arthur',
    'graves',
    'grindelwald',
    'norris',
    'sirius',
    'black',
    'rowling',
    'albus',
    'lily',
    'dursley'
  ]
  replacements = [
    ['its', 'it\'s'],
    ['i', 'I'],
    ['hogwarts', 'Hogwarts'],
    ['theyre', 'they\'re'],
    ['american', 'American'],
    ['america', 'America'],
    ['scottish', 'Scottish'],
    ['scotland', 'Scotland'],
    ['england', 'England'],
    ['italy', 'Italy'],
    ['gryffindor', 'Gryffindor'],
    ['gryffindors', 'Gryffindors'],
    ['slytherin', 'Slytherin'],
    ['slytherins', 'Slytherins'],
    ['hufflepuff', 'Hufflepuff'],
    ['hufflepuffs', 'Hufflepuffs'],
    ['ravenclaw', 'Ravenclaw'],
    ['lgbt', 'LGBT'],
    ['nomaj', 'no-maj'],
    ['mrs', 'Mrs'],
    ['scotlandteam', 'Scotland Rugby Team'],
    ['timetravelling', 'time-travelling'],
    ['horcrux', 'Horcrux'],
    ['uk', 'UK'],
    ['phoenix', 'Phoenix'],
    ['thats', 'that\'s'],
    ['youd', 'you\'d'],
    ['horcruxreceptacle', 'Horcrux receptacle'],
    ['theyve', 'they\'ve'],
    ['shes', 'she\'s'],
    ['nomajes', 'no-majes'],
    ['philosophers', 'Philosophers'],
    ['couldnt', 'couldn\'t'],
    ['jewish', 'Jewish'],
    ['new york', 'New York'],
    ['arent', 'aren\'t'],
    ['im', 'I\'m'],
    ['cant', 'can\'t'],
    ['jk', 'JK'],
    ['dont', 'don\'t'],
    ['youre', 'you\'re'],
    ['wouldnt', 'wouldn\'t']
  ]

  puncreplacements = [
    ['puncfullstoppunc', '.'],
    ['punccommapunc', ','],
    ['puncexclamationpunc', '!'],
    ['puncquestionpunc', '?'],
    ['puncelipsispunc', '...'],
    ['punccolonpunc', ':'],
    ['puncsemicolonpunc', ';'],
    ['puncampersandpunc', ' &'],
    ['puncstoppunc', '\n']
  ]

  text = ''

  while (text == ''):
    text = ' ' + input_text + ' '

    for replacement in replacements:
      text = text.replace(' ' + replacement[0] + ' ', ' ' + replacement[1] + ' ')

    for name in names:
      text = text.replace(' ' + name + ' ', ' ' + name.capitalize() + ' ')
      text = text.replace(' ' + name + 's ', ' ' + name.capitalize() + '\'s ')
    
    for puncreplacements in puncreplacements:
      text = text.replace(' ' + puncreplacements[0], puncreplacements[1])

    text = re.sub(r'([.!?]) ([a-zA-Z0-9])', sub_match, text)

    punctuation = punc[randint(0, len(punc) - 1)]

    text = text[:-1].lstrip(' .,!?:;&')

    while len(text) + len(punctuation) > 140:
      text = text.rsplit(' ', 1)[0]
      

  text = text[0].capitalize() + text[1:] + punctuation

  return text

def sub_match(match):
  return match.group(1) + ' ' + match.group(2).upper()


def generate_text(model, tokenizer, seq_length, lines, n_words):
  data = ''
  while (data == ''):
    seed_text = lines[randint(0, len(lines) - 1)]
    data = format_text(generate_seq(model, tokenizer, seq_length, seed_text, n_words)).split('\n')[0]

  return data

# load cleaned text sequences
in_filename = 'tmp/data_sequences.txt'
doc = load_doc(in_filename)
lines = doc.split('\n')
seq_length = len(lines[0].split()) - 1

generated = {}

for i in range(1, 10):
  accuracy = i / 10
  accuracy_str = str(accuracy)

  # load the model
  model = load_model('tmp/model-' + accuracy_str + '.h5')
  # load the tokenizer
  tokenizer = load(open('tmp/tokenizer-' + accuracy_str + '.pkl', 'rb'))

  generated[accuracy_str] = []

  # generate new text
  num_vals = 500
  for i in range(num_vals):
    # append generated text
    generated_text = generate_text(model, tokenizer, seq_length, lines, 30)
    generated[accuracy_str].append(generated_text)
    print('.', end='', flush=True)

  print()
  print('Generated', num_vals, 'tweets at', accuracy_str, 'accuracy')
  print('Example:')
  print(generated[accuracy_str][randint(0, len(generated[accuracy_str]) - 1)])

with open('../data/data.json', 'w') as outfile:
  json.dump(generated, outfile)