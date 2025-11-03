
class Review:
    def __init__(self, text, label):
        self.text = text
        self.label = label

    def is_positive(self):
        return self.label.lower() == "positive"

    def word_count(self):
        words = self.text.split()
        return len(words)
