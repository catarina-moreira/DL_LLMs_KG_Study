# load the shakespear dataset
import os
import urllib.request  # For handling URL requests
import urllib.parse 


def load_shakespeare( path ):

    if not os.path.exists( path + 'shakespeare.txt'):
        print("Downloading shakespeare.txt...")
        shakespeare_url = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'
        urllib.request.urlretrieve(shakespeare_url, path + 'shakespeare.txt')
    with open(path + 'shakespeare.txt', 'r') as f:
        text = f.read()
    return text
