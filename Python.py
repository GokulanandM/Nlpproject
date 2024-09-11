import urllib.request

# Download the tiny shakespeare dataset
url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
filename = "input.txt"
urllib.request.urlretrieve(url, filename)

# Read and inspect the dataset
with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()

# Display the length of the dataset in characters
print("Length of dataset in characters: ", len(text))

# Display the first 1000 characters of the dataset
print("\nFirst 1000 characters of the dataset:\n")
print(text[:1000])
# here are all the unique characters that occur in this text
chars = sorted(list(set(text)))
vocab_size = len(chars)
print(''.join(chars))
print(vocab_size)# create a mapping from characters to integers
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s] # encoder: take a string, output a list of integers
decode = lambda l: ''.join([itos[i] for i in l]) # decoder: take a list of integers, output a string

print(encode("hii there"))
print(decode(encode("hii there")))