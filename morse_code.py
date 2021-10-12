import argparse

parser = argparse.ArgumentParser(description='Translate between morse code and plain text')
parser.add_argument("input", type=str, help="either plain text or morse code")
args = parser.parse_args()

morse = {
	"A" : "·−","B" : "−···","C" : "−·−·","D" : "−··","E" : "·","F" : "··−·","G" : "−−·","H" : "····","I" : "··","J" : "·−−−","K" : "−·−","L" : "·−··","M" : "−−","N" : "−·","O" : "−−−","P" : "·−−·","Q" : "−−·−","R" : "·−·","S" : "···","T" : "−","U" : "··−","V" : "···−","W" : "·
  inv_morse = {v: k for k, v in morse.items()}

def replace_none_with_leer(list):
	return ['  ' if v is None else v for v in list]

def translate(text):
	if "·" in text or "−" in text:
		chars = list(text.split(' '))
		translation = list(map(inv_morse.get, chars))
		translation = replace_none_with_leer(translation)
		translation = ''.join(translation)
	else:
		chars = list(text.upper())
		translation = list(map(morse.get, chars))
		translation = replace_none_with_leer(translation)
		translation = ' '.join(translation)
	return translation

if _name_ == "_main_":
	print(translate(args.input))
