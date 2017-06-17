"""
PyHP++# CIC written in Python 3.
This should be constantly updated with the spec.
Until some necessary additions are made to the spec, some temporary solutions are made.
For example, there is no official out function, so print is used.
Be warned that once an official addition is made, temporary functions WILL be deprecated or changed.

This does not support templating.
"""

# Stuff for parser
from arpeggio import *
from arpeggio import RegExMatch as _

# Grammar

# WARN: A specification for symbols has not been set. 
def symbol():
	return _(r"[A-Za-z_][A-Za-z_0-9]*")

# WARN: A specification for numbers has not been set.
def number():
	return _(r"\d*\.\d*|\d+")

# TODO: String support.
def literal():
	return [number]

def expression():
	return [literal, function_call]

# WARN: A specification for expression lists has not been set. For all I know, it could end up being separated by fucking greek commas.
#		...please don't do that.
def expression_list():
	return expression, ZeroOrMore(",", expression)

# WARN: A specification for calling has not been set, but is implied from example code.
def function_call():
	return symbol, "(", expression_list, ");"

def language():
	return ZeroOrMore([expression]), EOF

class PyHP_PPH_Visitor(PTNodeVisitor):
	pass

def pyhpp_run_string(code):
	parser = ParserPython(language)
	parse_tree = parser.parse(code)
	ast = visit_parse_tree(parse_tree, PyHP_PPH_Visitor())

	print(ast)

if __name__ == "__main__":
	import sys

	try:
		source = open(sys.argv[1], "r")
	except KeyError:
		print("cic.py filename")
		sys.exit()
	except FileNotFoundError:
		print("Could not find file.")
		sys.exit()

	code = source.read()
	source.close()

	pyhpp_run_string(code)
