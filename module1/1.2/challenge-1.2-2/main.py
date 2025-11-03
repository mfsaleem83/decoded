from review import Review

review1 = Review("Great!", "positive")
review2 = Review("Bad!", "negative")

print(review1.text, review1.is_positive())
print(review1.word_count())
print(review2.word_count())
