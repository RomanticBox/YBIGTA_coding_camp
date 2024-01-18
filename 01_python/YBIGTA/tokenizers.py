from typing import Optional, Union, List
from YBIGTA.tokenizer import Tokenizer

class BPETokenizer(Tokenizer):
    def __init__(self, 
                 corpus: Optional[Union[List[str], str]] = None):
        '''
        Args:
            corpus (List[str], str): preprocessed string
        Returns:
            None
        '''
        super().__init__(corpus)

    def train(self, 
              n_iter: int
    ) -> None:
        '''
        Perform merge operation n_iter times in order to find
        a list of tokens
        Args:
            n_iter (int): number of iterations
        Returns:
            None
        '''
        if not isinstance(n_iter, int) or n_iter < 1:
            raise TypeError('number of iterations (n_iter) needs to be a positive integer')
        
        # Need to intialize self.tokens by separating words into characters
        self.tokens = []
        self.word_freq_temp = {}
        for key, value in self.word_freq.items():
            self.word_freq_temp[" ".join(key)] = value
        self.word_freq = self.word_freq_temp

        for _ in range(n_iter):
            pairs_freq, pairs_idx = self.get_stats()
            max_pair = max(pairs_freq, key = pairs_freq.get)
            self.word_freq = self.merge(max_pair, pairs_idx[max_pair])

        self.create_tokens()

    def get_stats(self):
        pairs_freq, pairs_idx = {}, {}
        for i, (word, freq) in enumerate(self.word_freq.items(), 0):
            symbols = word.split()
            for j in range(len(symbols)-1):
                cur_pair = symbols[j], symbols[j+1]
                if cur_pair not in pairs_freq:
                    pairs_freq[cur_pair] = 0
                    pairs_idx[cur_pair] = []
                pairs_freq[cur_pair] += freq
                pairs_idx[cur_pair].append([i, j])
        return pairs_freq, pairs_idx
    
    def merge(self, max_pair, indices):
        idx = 0
        new_word_freq = {}
        for i, (word, value) in enumerate(self.word_freq.items()):
            if idx < len(indices) and i == indices[idx][0]:
                symbols = word.split()
                new_word = []
                prev_idx = 0
                while idx < len(indices) and i == indices[idx][0]:
                    new_word += symbols[prev_idx:indices[idx][1]]
                    new_word.append(max_pair[0] + max_pair[1])
                    prev_idx = indices[idx][1] + 2
                    idx += 1
                if prev_idx < len(symbols):
                    new_word += symbols[prev_idx:]
                new_word_freq[" ".join(new_word)] = value
            else:
                new_word_freq[word] = value
        
        return new_word_freq
    
    def create_tokens(self):
        self.tokens = []
        for word in self.word_freq:
            symbols = word.split()
            for symbol in symbols:
                if symbol not in self.tokens:
                    self.tokens.append(symbol)
        self.tokens.append('*')


class WordTokenizer(Tokenizer):
    def __init__(self, corpus: Optional[Union[List[str], str]] = None):
        super().__init__(corpus)

    def train(self, n_iter: int = 1) -> None:
        pass