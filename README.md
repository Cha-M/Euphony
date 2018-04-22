# Euphony
Python/tkinter GUI application to generate random words using customised rules.

Words follow a randomly chosen pattern concatenating randomly chosen strings each from a list keyed to the character in the pattern.

Rules can be generated from the text in the text box or a utf-8 .txt file, or created by editing a CSV file in the same format.
Included are some examples.
Generated rules can be saved as CSV.

'Invisibles' is used to mean characters used in the word pattern which are not used to select a random string.

A list of Banned strings can be included whereby the function will pass over generated words which include one of the aforementioned strings and pick another.

Text can also be put through a cipher, creating a pseudo-translation.
