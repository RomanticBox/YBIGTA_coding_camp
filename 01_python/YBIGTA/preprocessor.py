import re

class Preprocessor(type='str'):
    @staticmethod
    def __init__(self, input_string):
        self.input_string = input_string
        self.split_alphabet = ['^a-zA-Z\d\s:']

    @staticmethod
    def split_string(self, input_string):
        if input_string[-4:] =='.txt':
            try:
                txt_to_str = open(input_string, 'r').read()
                input_string = txt_to_str
            except FileNotFoundError:
                print(f'FileNotFoundError: {input_string} is not in the directory.
                        Please check the file name and the directory.')
        preprocess_list = []
        input_string = input_string.lower()
        # all possible cases for split
        input_string = input_string.split(self.split_alphabet)
        
        for i in range(len(input_string)):
            if "'" in input_string[i]:
                first, second = self.single_quote_handle(input_string[i])
                preprocess_list.append(first)
                if not second:
                    preprocess_list.append(second)
            else:
                preprocess_list.append(input_string[i].split(input_string[i]))
            preprocess_list[-1] += '<\w>'
            preprocess_list[-1] = list(preprocess_list[-1])
            preprocess_list[-1] = " ".join(preprocess_list[-1])
        
        return preprocess_list
    # [^a-zA-Z\d\s:]

    @staticmethod
    def single_quote_handle(self, single_string):
        ''' Handling with single quotation mark ( ' )
        divide cases, and divide the words by each cases
        '''
        
        while "'" in single_string:
            if single_string.startswith("'"):
                single_string = single_string[1:]
            elif single_string.endswith("'"):
                single_string = single_string[:-1]
            else:
                break
        if "'" in single_string:
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
            return first, second
        else:
            print(f'special case that does not fit in the cases: 
                    {single_string}')
            return single_string, None
            
    @staticmethod
    def letter_splitter(self, word):
        ''' split the word by each letter
        '''
        return [char for char in word]
