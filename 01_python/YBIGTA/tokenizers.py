from typing import Optional, Union, List
from tokenizer import Tokenizer

class BPETokenizer(Tokenizer):
    def __init__(self, corpus: Optional[Union[List[str], str]] = None):
        super().__init__(corpus)

    def train(self, n_iter: int) -> None:
        if not isinstance(n_iter, int) or n_iter < 1:
            raise TypeError('number of iterations (n_iter) needs to be a positive integer')
        
        for _ in range(n_iter):
            self.merge()

    def merge(self):
        pass

class WordTokenizer(Tokenizer):
    def __init__(self, corpus: Optional[Union[List[str], str]] = None):
        super().__init__(corpus)

    def train(self, n_iter: int = 1) -> None:
        pass