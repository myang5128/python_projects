import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv(r"Nato Alphabet\nato_phonetic_alphabet.csv")
phon_dict = {row.letter:row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word to be translated: ").upper()
result = [phon_dict[letter] for letter in word]
print(result)