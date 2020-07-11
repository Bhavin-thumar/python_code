'oh what a day what a lovely day'   # oh : 1, what : 2, a : 2, day : 2, lovely : 1
"'don't stop believing"   # don't : 1, stop : 1, believing : 1

'Oh what a day what a lovely day'   # oh : 1, what : 2, a : 2, day : 2, lovely : 1
'Oh what a day, what a lovely day!'   # oh : 1, what : 2, a : 2, day : 2, lovely : 1

alphanum_list = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n',
	'o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H',
	'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
	'0','1','2','3','4','5','6','7','8','9',"'"," ")


def count_word(sentence):
	sentence_in_letters = []
	
	for letter in sentence:
		if letter in alphanum_list:
			sentence_in_letters.append(letter)

	sentence_without_punctuation = ''.join(sentence_in_letters)
	
	sentence_list = tuple(map(lambda a : a.lower(), sentence_without_punctuation.split()))
	unique_words = set(sentence_list)
	
	counting_words = {}
	
	for words in sorted(unique_words):
		counting_words[words] = sentence_list.count(words)

	return counting_words

obj_1 = count_word("don't stop believing")
print(obj_1)