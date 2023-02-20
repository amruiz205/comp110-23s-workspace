# #how to declare a vector



# my_vec = [62, 65, 71, 73, 74, 72, 68, 63, 61, 58]

# print(my_vec)
# print(my_vec[0])




# my_vec[0] = 61 #this selects the 0th index aand rpelaces it with 61

# print(my_vec[0])

# #one way to store information
# transaction_dates = ['date 1', 'date 2']
# manufacturers = ['bmw', 'toyota']
# model_year = 92021, 2022
# transactions_types = ['buy', 'sell']
# prices = [50000, 20000]

# nested_vec = [[1, 2, 3], [4, 5 ,6 ], [7, 8, 9], ]
# print(nested_vec[0])
# nested_vec[0][2] = 7
# print(nested_vec[0])

# records = [['01-03-2017', 'bmw', 2021, 'buy', 50000], [['01-03-2018', 'toyota', 2011, 'sell', 60000]]]
# print(records[0])


# for curr_record in records:
#     print(curr_record)

# with open('temp.txt', 'w') as file:
#     file.write(str(records[0]))

# with open('temp.txt', 'r') as file:
#     file.write(str(records[0])
#     )

# n: int = int(input("enter a number"))

# if n % 3 != 0:
#     print("D")
# else:
#     if n > 1:
#         print("a")



# from collections import defaultdict
# import random
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches

# def create_wordle(words, max_words=100):
#     word_counts = defaultdict(int)
#     for word in words:
#         word_counts[word] += 1
    
#     word_counts = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:max_words])
    
#     word_sizes = [count**0.5 for word, count in word_counts.items()]
#     word_sizes = [size / max(word_sizes) * 100 + 10 for size in word_sizes]
    
#     fig, ax = plt.subplots()
#     plt.axis('off')
#     for word, count, size in zip(word_counts.keys(), word_counts.values(), word_sizes):
#         x = random.uniform(0, 1)
#         y = random.uniform(0, 1)
#         ax.text(x, y, word, ha='center', va='center', fontsize=size, color='black')
    
#     plt.show()

# words = ["dog", "cat", "horse", "dog", "dog", "cat", "horse", "horse", "horse"]
# create_wordle(words)




x: int = -1
y: int = 1
z = x + y 
print(z)
