class PreprocessLinesMixin:
    def preprocess_lines(self):
        """Preprocess lines by normalizing and cleaning text."""

        self.preprocessed_lines = [line.lower().strip() for line in self.lines]