class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        words = self.input_string.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

    def set_string(self, new_string):
        self.input_string = new_string

    def get_string(self):
        return self.input_string

if __name__ == "__main__":
    sentence = "Hello world this is Python"
    reverser = StringReverser(sentence)
    print("Original string:", reverser.get_string())
    print("Reversed word by word:", reverser.reverse_words())
