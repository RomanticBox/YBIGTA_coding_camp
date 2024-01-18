import re

class Preprocessor:
    def __init__(self,
                 input_string=None):
        '''
        Args:
            input_string: input string, default is None
        Returns:
            None
        '''
        self.input_string = input_string
        self.complement_alphabet = r' [`\-=[];,./~!@#$%^&*()_+{\}|:"<>?]'
        self.combined_alphabet = f'{self.complement_alphabet}'
        
    def split_string(self, input_string) -> list[str]:
        '''
        Basic preprocessing for input string
        and return list of strings
        Args:
            input_string: input string, recommended to be string,
                        but edge case handling codes included.
        Returns:
            preprocess_list: list of strings after preprocessing
        '''
        preprocess_list = []

        # change list as string
        if isinstance(input_string, list):
            input_string = input_string[0]
        
        # change file as string
        if input_string.endswith('.txt') \
            or input_string.endswith('.story') \
            or input_string.endswith('.data'):
            try:
                txt_to_str = open(input_string, 'r', encoding='utf-8').read()
                input_string = txt_to_str
            except FileNotFoundError:
                print(f'FileNotFoundError: {input_string} is not in the directory. \
                        Please check the file name and the directory.')
        
        input_string = input_string.lower() # Remove capital letters.

        # Rll possible cases for split
        input_string = re.split(r'[' + re.escape(self.complement_alphabet) + ']', input_string)
        
        # Remove empty strings
        temp_string = []
        for s in input_string:
            if s != '':
                temp_string.append(s)
        input_string = temp_string
        
        # Remove special characters
        for i in input_string:
            if "'" in i:
                first, second = self.single_quote_handle(i)
                preprocess_list.append(first)

                if second is not None:
                    preprocess_list.append(second)
            else:
                preprocess_list.append(i)

            # Add blank space between each words and add <\w> at the end of each words.
            preprocess_list[-1] = " ".join(list(preprocess_list[-1]))
            tmp = preprocess_list[-1] + ' <\w>'
            preprocess_list[-1] = tmp
        return preprocess_list

    @staticmethod
    def single_quote_handle(single_string) -> tuple[str, str]:
        ''' Handling with single quotation mark ( ' )
        divide cases, and divide the words by each cases
        Args:
            single_string: string that contains single quotation mark ( ' )
        Returns:
            first: first part of the word
            second: second part of the word (possible to be None)
        '''
        first = single_string
        second = None

        # Remove normal [ ' ] from the word
        while "'" in single_string:
            if single_string.startswith("'"):
                single_string = single_string[1:]
            elif (single_string.endswith("'") \
                and not single_string.endswith("s'")):
                single_string = single_string[:-1]
            else:
                break
        
        # Handle with edge cases
        if "'" in single_string:
            if single_string.endswith("n't") \
                or single_string.endswith("'ve") \
                or single_string.endswith("'ll") \
                or single_string.endswith("'re"):
                first = single_string[:-3]
                second = single_string[-3:]
            
            elif single_string.endswith("'d") \
                or single_string.endswith("'m") \
                or single_string.endswith("'s") \
                or single_string.endswith("s'"):
                first = single_string[:-2]
                second = single_string[-2:]
        else:
            print(f'special case that does not fit in ordinary cases: \
                  {single_string}')
            first = single_string
            second = None
        return first, second
            
    @staticmethod
    def letter_splitter(word):
        ''' split the word by each letter
        '''
        return [char for char in word]
