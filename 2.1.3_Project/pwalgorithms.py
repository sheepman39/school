# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("./2.1.3_Project/dictionary.txt")
  for line in dictionary_file:
    # store word, ommitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

def two_word(password):
  words = get_dictionary()
  guesses = 0

  for i in words:
    if(i in password):
      for w in words:
        if(w in password):
          guesses += 1
          if (w + i == password):
            return True, guesses
  return False, guesses

def two_words_and_digit (password):
  words = get_dictionary()
  guesses = 0
  for i in words:
    if(i in password):
      for w in words:
        if(w in password):
          for j in "1234567890":
            if(j in password:
              guesses += 1
              if (j + w + i == password):
                return True, guesses
              elif (w + i + j == password):
                return True, guesses
  return False, guesses