
from homework.src._internals.count_words import CountWordsMixin
from homework.src._internals.parse_args import ParseArgsMixin
from homework.src._internals.preprocess_lines import PreprocessLinesMixin
from homework.src._internals.read_all_lines import ReadAllLinesMixin
from homework.src._internals.split_into_words import SplitIntoWordsMixin
from homework.src._internals.write_word_counts import WriteWordCountsMixin


class WordCountApp(
    ParseArgsMixin,
    ReadAllLinesMixin,
    PreprocessLinesMixin,
    SplitIntoWordsMixin,
    CountWordsMixin,
    WriteWordCountsMixin,
):
    def __init__(self):
        self.input_folder = None
        self.output_folder = None
        self.lines = None
        self.preprocessed_lines = None
        self.words = None
        self.word_counts = None

    def run(self):

        self.parse_args()
        self.read_all_lines()
        self.preprocess_lines()
        self.split_into_words()
        self.count_words()
        self.write_word_counts()


if __name__ == "__main__":
    WordCountApp().run()

    