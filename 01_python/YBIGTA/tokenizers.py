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
        
        self.tokens = []
        for _ in range(n_iter):
            self.merge()

    def merge(self):
        pass

class WordTokenizer(Tokenizer):
    def __init__(self, corpus: Optional[Union[List[str], str]] = None):
        super().__init__(corpus)

    def train(self, n_iter: int = 1) -> None:
        pass