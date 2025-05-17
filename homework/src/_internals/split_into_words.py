class SplitIntoWordsMixin:
    def split_into_words(self):
        """Split lines into individual words and clean punctuation."""

        words = []

        for line in self.preprocessed_lines:
            words.extend(word.strip(",.!?") for word in line.split())

        self.words = words