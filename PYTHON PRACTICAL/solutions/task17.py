class Gallows:
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if self.game_over:
            return "game over"

        if not self.words:
            self.words.append(word)
            return self.words

        last_word = self.words[-1]
        if word in self.words or word[0] != last_word[-1]:
            self.game_over = True
            return "game over"

        self.words.append(word)
        return self.words

    def restart(self):
        self.words = []
        self.game_over = False
        return "game restarted"
