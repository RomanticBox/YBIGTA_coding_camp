from typing import Optional, Union, List

class Tokenizer:
    def __init__(self, corpus: Optional[Union[List[str], str]] = None):
        # Initialize self.corpus
        self.corpus = {}
        self.add_corpus(corpus)

    def add_corpus(self, corpus: Optional[Union[List[str], str]] = None) -> None:
        if isinstance(corpus, str):
            if corpus in self.corpus:
                self.corpus[corpus] += 1
            else:
                self.corpus[corpus] = 1
        elif isinstance(corpus, list):
            for word in corpus:
                if word in self.corpus:
                    self.corpus[word] += 1
                else:
                    self.corpus[word] = 1
        else:
            raise TypeError('corpus is neither a string nor a list of strings')
        
    def get_corpus(self):
        return self.corpus
    
    def train(self, n_iter: int) -> None:
        pass

    def tokenize(self,
                 text: Union[List[str], str],
                 padding: bool = False,
                 max_length: Optional[int] = None
    ) -> Union[List[List[int]], List[int]]:
        # Need to convert text to token and truncate if necessary
        text_tokens = []
        if isinstance(text, str):
            word_tokens = self.text_to_tokens(text)
            if len(word_tokens) <= max_length:
                text_tokens.append(word_tokens)
            else:
                text_tokens.append(word_tokens[:max_length])
        elif isinstance(text, str):
            for word in text:
                word_tokens = self.text_to_tokens(word)
                if len(word_tokens) <= max_length:
                    text_tokens.append(word_tokens)
                else:
                    text_tokens.append(word_tokens[:max_length])
        else:
            raise TypeError('text is neither a string nor a list of strings')

        # Need to convert from token to token ID
        text_tokenIDs = []
        for word_tokens in text_tokens:
            text_tokenIDs.append(self.tokens_to_tokenIDs(word_tokens))

        # Need to add padding token if necessary
        if padding:
            token_padding = 1
            max_length_word_tokens = 0
            for word_tokens in text_tokens:
                max_length_word_tokens = max(max_length_word_tokens, len(word_tokens))
            for i in range(len(text_tokenIDs)):
                for _ in range(max_length_word_tokens - len(text_tokenIDs[i])):
                    text_tokenIDs[i].append(token_padding)
        
        return text_tokenIDs

    def text_to_tokens(self, word):
        word_tokens = []
        cur_token = ''
        for i in range(len(word)):
            if i+1 == len(word) or str(cur_token + word[i]) not in self.tokens:
                word_tokens.append(cur_token)
                cur_token = ''
            else:
                cur_token += word[i]
        return word_tokens
    
    def tokens_to_tokenIDs(self, word_tokens):
        word_tokenIDs = []
        for i in range(len(word_tokens)):
            word_tokenIDs.append(self.tokens.index(word_tokens[i]))
        return word_tokenIDs