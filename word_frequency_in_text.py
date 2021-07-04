from collections import Counter

text="Google LLC is an American multinational technology company that specializes in Internet-related services and products,"\
     "which include online advertising technologies, a search engine, cloud computing, software, and hardware."\
     "It is considered one of the big four Internet stocks along with Amazon, Facebook, and Apple."

words=text.split()

counter=Counter(words)
top3=counter.most_common(3)
print(top3)
