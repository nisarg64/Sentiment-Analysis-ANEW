import anew

with open("./csc791-sentences-random.txt", 'r') as f:
    content = f.readlines()


import csv
with open('csc791_sentiment.csv', 'wb') as csvfile:
    sentiment_writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    sentiment_writer.writerow(["Sentence", "FileName",  "Valence", "Arousal"])
    for line in content:
        if line.strip():
            line_to_word = line.split("|")
            sentiment_attributes = anew.sentiment(line_to_word[0].split())
            sentiment_writer.writerow([line_to_word[0].strip(), line_to_word[1].strip(), sentiment_attributes['valence'], sentiment_attributes['arousal']])