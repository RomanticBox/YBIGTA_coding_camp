from typing import Optional, Union, List

class Tokenizer:
    def __init__(self, corpus: Optional[Union[List[str], str]] = None):
        self.corpus = corpus
        self.tokens = []

    def get_corpus(self):
        return self.corpus

    def add_corpus(self, corpus: Optional[Union[List[str], str]] = None) -> None:
        if corpus is not None:
            if isinstance(self.corpus, str):
                self.corpus = [self.corpus]

            if isinstance(corpus, str):
                self.corpus.append(corpus)
            else:
                self.corpus += corpus
    
    def train(self, n_iter: int) -> None:
        pass

    def tokenize(self,
                 text: Union[List[str], str],
                 padding: bool = False,
                 max_length: Optional[int] = None
    ) -> Union[List[List[int]], List[int]]:
        # Need to convert text to token
        

        # Need to convert from token to token ID


        # Need to add padding token if necessary

class BPETokenizer(Tokenizer):
    def __init__(self, corpus: Optional[Union[List[str], str]] = None):
        super().__init__(corpus)

class WordTokenizer(Tokenizer):
    def __init__(self, corpus: Optional[Union[List[str], str]] = None):
        super().__init__(corpus)