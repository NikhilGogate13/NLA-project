from utils.Bytepair import Encoder
import nltk
import argparse
import os.path
import json

nltk.download('punkt')

parser = argparse.ArgumentParser(description='document parser')

dim = 300

parser.add_argument("--input", type=str, help="input file")
parser.add_argument("--output", type=str, help="output file")
parser.add_argument("--output_text", type=str, help="output file")
my_path = os.path.abspath(os.path.dirname(__file__))
params = parser.parse_args()
params.input = os.path.join(my_path, params.input)
params.output = os.path.join(my_path, params.output)
params.output_text = os.path.join(my_path, params.output_text)


encoder = Encoder(dim)
with open(params.input, "r") as input_file:
    text = input_file.read()
    sents = nltk.sent_tokenize(text)
encoder.fit(sents)
with open(params.output, "w") as fp:
    json.dump(encoder.vocabs_to_dict(), fp)

with open(params.input, "r") as input_file, open(params.output_text, "w") as output_file:
