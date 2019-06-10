from numpy import array
from pickle import dump
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding
from keras.callbacks import Callback

# load doc into memory
def load_doc(filename):
  # open the file as read only
  file = open(filename, 'r')
  # read all text
  text = file.read()
  # close the file
  file.close()
  return text

class EarlyStoppingByAccuracy(Callback):
  def __init__(self, monitor='acc', value=0.98, verbose=0):
    super(Callback, self).__init__()
    self.monitor = monitor
    self.value = value
    self.verbose = verbose

  def on_epoch_end(self, epoch, logs={}):
    current = logs.get(self.monitor)
    if current is None:
      print("Early stopping requires %s available!" % self.monitor, RuntimeWarning)

    if current >= self.value:
      if self.verbose > 0:
        print("Epoch %d: early stopping" % epoch)
      self.model.stop_training = True

def train_model(lines, accuracy):
  # integer encode sequences of words
  tokenizer = Tokenizer()
  tokenizer.fit_on_texts(lines)
  sequences = tokenizer.texts_to_sequences(lines)
  # vocabulary size
  vocab_size = len(tokenizer.word_index) + 1

  # separate into input and output
  sequences = array(sequences)
  X, y = sequences[:,:-1], sequences[:,-1]
  y = to_categorical(y, num_classes=vocab_size)
  seq_length = X.shape[1]

  # define model
  model = Sequential()
  model.add(Embedding(vocab_size, 50, input_length=seq_length))
  model.add(LSTM(100, return_sequences=True))
  model.add(LSTM(100))
  model.add(Dense(100, activation='relu'))
  model.add(Dense(vocab_size, activation='softmax'))

  # early stopping
  callbacks = [
    EarlyStoppingByAccuracy(monitor='acc', value=accuracy, verbose=1),
  ]

  print(model.summary())
  # compile model
  model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
  # fit model
  model.fit(X, y, batch_size=128, epochs=500, verbose=1, callbacks=callbacks)
  return model, tokenizer

def export_model(model, tokenizer, accuracy):
  # save the model to file
  model.save('tmp/model-' + accuracy + '.h5')
  # save the tokenizer
  dump(tokenizer, open('tmp/tokenizer-' + accuracy + '.pkl', 'wb'))

# load
in_filename = 'tmp/data_sequences.txt'
doc = load_doc(in_filename)
lines = doc.split('\n')

accuracy = 0.1

for i in range(1, 10):
  accuracy = i / 10
  accuracy_str = str(accuracy)

  model, tokenizer = train_model(lines, accuracy)
  print('Generated model with around', accuracy, 'accuracy')

  export_model(model, tokenizer, accuracy_str)
  print('Exported model to tmp/model-' + accuracy_str + '.h5 and tokenizer to tmp/tokenizer-' + accuracy_str + '.pkl')