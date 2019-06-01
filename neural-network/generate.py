from random import randint
from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import json

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

def format_text(text):
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
    'albus'
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
    ['dont', 'dont\'t'],
    ['youre', 'you\'re']
  ]

  text = ' ' + text + ' '

  for replacement in replacements:
    text = text.replace(' ' + replacement[0] + ' ', ' ' + replacement[1] + ' ')

  for name in names:
    text = text.replace(' ' + name + ' ', ' ' + name.capitalize() + ' ')
    text = text.replace(' ' + name + 's ', ' ' + name.capitalize() + '\'s ')

  punctuation = punc[randint(0, len(punc) - 1)]

  text = text[1:][:-1]

  while len(text) + len(punctuation) > 140:
    text = text.rsplit(' ', 1)[0]

  text = text[0].capitalize() + text[1:] + punctuation

  return text

# load cleaned text sequences
in_filename = 'tmp/data_sequences.txt'
doc = load_doc(in_filename)
lines = doc.split('\n')
seq_length = len(lines[0].split()) - 1

# load the model
model = load_model('tmp/model.h5')

# load the tokenizer
tokenizer = load(open('tmp/tokenizer.pkl', 'rb'))

# generate new text
generated = []
num_vals = 500
for i in range(num_vals):
  # select a seed text
  seed_text = lines[randint(0, len(lines))]
  # append generated text
  generated.append(format_text(generate_seq(model, tokenizer, seq_length, seed_text, 30)))
  print('.', end='', flush=True)

with open('../data/data.json', 'w') as outfile:
  json.dump(generated, outfile)

print()
print('Generated', num_vals, 'tweets')