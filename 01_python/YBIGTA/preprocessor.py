
class Preprocessor():

    def __init__(self, input_string):
        self.input_string = input_string
        self.split_alphabet = ['.', ',', '!', '?', ' ', "'", '"', ':', ';', '[', ']', '|', '*', '(', ')', '>', '<',]

    def split_string(self, input_string):
        preprocess_list = []
        input_string = input_string.lower()
        # all possible cases for split
        input_string = input_string.split(' ', '!', '?', ',', '.', 
                                          ':', ';', '"', '|', '*',
                                          '(', ')', '>', '<')
        
        for i in range(len(input_string)):
            if "'" in input_string[i]:
                first, second = self.single_quote_handle(input_string[i])
                preprocess_list.append(first)
                preprocess_list.append(second)
                
            else:
                preprocess_list.append(input_string[i].split(input_string[i]))
            preprocess_list[-1] += '·'
        
        return preprocess_list
    
    def single_quote_handle(self, single_string):
        ''' Handling with single quotation mark ( ' )
        divide cases, and divide the words by each cases
        '''
        # abbreviation of not (n't)
        if single_string.endswith("n't") \
            or single_string.endswith("'ve") \
            or single_string.endswith("'ll") \
            or single_string.endswith("'re"):
            first = single_string[:-3]
            second = single_string[-3:]
        
        elif single_string.endswith("'d") \
            or single_string.endswith("'m") \
            or single_string.endswith("'s"):
            first = single_string[:-2]
            second = single_string[-2:]
        else:
            print(f'special case that does not fit in the cases: 
                  {single_string}')
        return first, second
    
    def letter_splitter(self, word):
        ''' split the word by each letter
        '''
        return [char for char in word]

'''
cases for using single quotation mark ( ' )
1. quotation mark
'I'm a student.' -> I / 'm / a / student / .

2. abbreviation
'I'm a student.'
Can't = Cannot -> ca / n't
Don't = Do not -> do / n't
Isn't = Is not -> is / n't
Won't = Will not -> wo / n't
I've = I have -> I / 've
I'll = I will -> I / 'll
I'd = I would -> I / 'd
I'm = I am -> I / 'm
You'are = You are -> You / 're
ain't = is not -> ai / n't

3. possessive case
It's John's book. -> It / 's / John / 's / book / .
Johannsons' house is very big. -> Johannsons / ' / house / is / very / big / .

4. quotation mark in quotation mark
"He said, 'I'm a student.'"

5. quotation mark in abbreviation
"He said, 'I'm a student.'"


'''
