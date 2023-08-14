def count_words_in_sentence():
    sentence = input("Please enter your sentence: ")
    word_count = len(sentence.split())
    print(f"The sentence '{sentence}' contains {word_count} words.")

print("Welcome! Enter a sentence and I will tell you how many words it contains.")
count_words_in_sentence()
