class CountWordsMixin:
    def count_words(self):
        """Count occurrences of each word using a plain dictionary."""
        word_counts = {}
        for word in self.words:
            word_counts[word] = word_counts.get(word, 0) + 1
        self.word_counts = word_counts