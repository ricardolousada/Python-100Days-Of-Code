sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

list_of_sentences = sentence.split()

result = {sentence:len(sentence) for sentence in list_of_sentences}

print(result)