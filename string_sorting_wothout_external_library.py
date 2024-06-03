# 1. given a string input, read in all the contents
# 2. count the total words
# 3. get the number of occurrences of each word
# 4. sort the words based on frequency from largest to smallest
 
# Here’s the input: The quick brown fox jumped over the brown fence the fence is high and the fence is wide

# Approach 1:

class WordFrequencySortingImplementation:
    def __init__(self, input_string):
        self.input_string = input_string
        self.words = []
        self.word_count_dict = {}
        self.total_words = 0
        self.sorted_count = []


    def split_string_in_words(self):
        word = ""

        for char in self.input_string:
            if char.isalpha():
                word += char
            elif word:
                self.words.append(word.lower())
                word = ""
        if word:
            self.words.append(word.lower())
    
    def count_word_occurances(self):
        for word in self.words:
            if word in self.word_count_dict:
                self.word_count_dict[word] += 1
            else:
                self.word_count_dict[word] = 1
        self.total_words = len(self.words)
    
    def quick_sort(self, items):
        if len(items) <= 1:
            return items
        
        pivot = items[len(items) // 2][1]
        left = [item for item in items if item[1] > pivot]
        middle = [item for item in items if item[1] == pivot]
        right = [item for item in items if item[1] < pivot]

        return self.quick_sort(left) + middle + self.quick_sort(right)

    def sort_words_by_frequency(self):
        word_count_items = list(self.word_count_dict.items())
        self.sorted_count = self.quick_sort(word_count_items)

    def analyze_words(self):
        self.split_string_in_words()
        self.count_word_occurances()
        self.sort_words_by_frequency()
    
    def results(self):
        return self.total_words, self.sorted_count
    


input_string = "The quick brown fox jumped over the brown fence the fence is high and the fence is wide"
word_analyser = WordFrequencySortingImplementation(input_string)
word_analyser.analyze_words()
total_words, sorted_word_count = word_analyser.results()

print(f"Total words: {total_words}")
print("Sorted words count:")
for word, frequency in sorted_word_count:
    print(f"{word}: {frequency}")


# Approach 2

class WordFrequencyAnalyzer2:
    def __init__(self, input_string):
        self.input_string = input_string
        self.word_count = {}
        self.total_words = 0
        self.sorted_word_count = []

    def split_and_count(self):
        word = ""
        for char in self.input_string:
            if char.isalpha():
                word += char
            elif word:
                word_lower = word.lower()
                if word_lower in self.word_count:
                    self.word_count[word_lower] += 1
                else:
                    self.word_count[word_lower] = 1
                word = ""
        if word:
            word_lower = word.lower()
            if word_lower in self.word_count:
                self.word_count[word_lower] += 1
            else:
                self.word_count[word_lower] = 1

        self.total_words = sum(self.word_count.values())

    def quicksort(self, items):
        if len(items) <= 1:
            return items
        pivot = items[len(items) // 2][1]
        left = [item for item in items if item[1] > pivot]
        middle = [item for item in items if item[1] == pivot]
        right = [item for item in items if item[1] < pivot]
        return self.quicksort(left) + middle + self.quicksort(right)

    def sort_by_frequency(self):
        word_count_items = list(self.word_count.items())
        self.sorted_word_count = self.quicksort(word_count_items)

    def analyze(self):
        self.split_and_count()
        self.sort_by_frequency()

    def get_results(self):
        return self.total_words, self.sorted_word_count

# Input string
input_string = "The quick brown fox jumped over the brown fence the fence is high and the fence is wide"

# Create an instance of WordFrequencyAnalyzer
analyzer = WordFrequencyAnalyzer2(input_string)

# Perform the analysis
analyzer.analyze()

# Get results
total_words, sorted_word_count = analyzer.get_results()

# Print results
print(f"Total words: {total_words}")
print("Word frequencies sorted by frequency:")
for word, freq in sorted_word_count:
    print(f"{word}: {freq}")