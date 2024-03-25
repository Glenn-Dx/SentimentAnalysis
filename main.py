from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv

def parse_csv_utf8(file_path):
    parsed_data = []
    with open(file_path, mode='r', encoding='utf-8', errors='replace') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            parsed_data.append(row)
    return parsed_data


file_path = 'all-data.csv'
data = parse_csv_utf8(file_path)

analyzer = SentimentIntensityAnalyzer()

amount = len(data)
false_positive = 0
false_neutral = 0
false_negative = 0


for row in data:
  vs = analyzer.polarity_scores(row[1])
  # print("{:-<65} {}".format(row[1], str(vs)))
  if(vs["compound"]>= 0.05 ):
    if(row[0] != "positive"):
      false_positive += 1
  elif(vs["compound"] > -0.05 and vs["compound"] < 0.05 ):
    if(row[0] != "neutral"):
      false_neutral += 1
  elif(vs["compound"] <= -0.05 ):
    if(row[0] != "negative"):
      false_negative += 1
  else:
    print("error")

total_error = false_positive+false_neutral+false_negative 
print(amount)
print(total_error)
print (f"False Positive : {false_positive } False Neutral : {false_neutral} False Negative: {false_negative}" )
print((total_error/amount )* 100)
