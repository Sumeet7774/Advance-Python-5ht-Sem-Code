import datetime
import os
import collections

valid = 0
invalid = 0
format = '%Y-%m-%d'

def isValid(review):
    if len(review) < 4:
        return False
    if not review[0].isalnum() or not len(review[0]) == 6:
        return False
    if not review[1].isalnum() or not len(review[1]) == 10:
        return False
    try:
        datetime.datetime.strptime(review[2], format)
    except ValueError:
        return False
    if int(review[3]) not in range(1, 6):
        return False
    return True

def read_reviews(filename):
    global valid, invalid
    reviews = []
    with open(filename, 'r') as file:
        for line in file:
            review = line.strip().split(' ', 4)
            if isValid(review):
                reviews.append(review[0:4])
                valid += 1
            else:
                invalid += 1
    return reviews

def calc_avg_rating(reviews):
    product_ratings = collections.defaultdict(list)
    for review in reviews:
        product_ratings[review[1]].append(int(review[3]))

    avg_rating = {k : sum(v) / len(v) for k, v in product_ratings.items()}
    return avg_rating

folder_path = 'G:\Codes\College\Sem 5\Advance Python\Lab Codes'
all_reviews = []

for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        all_reviews.extend(read_reviews(file_path))

avg_rating = calc_avg_rating(all_reviews)
for k, v in avg_rating.items():
    print('Product Id: {}    Average Rating: {:.2f}'.format(k, v))

top3_products = sorted(avg_rating.items(), key = lambda i : i[1], reverse = True)[:3]

print("\nTop 3 Products with Highest Average Ratings:")
for product, rating in top3_products:
    print('Product ID: {}    Average Rating: {:.2f}'.format(product, rating))

print('\nValid reviews: {}\nInvalid reviews: {}'.format(valid, invalid))

with open('summary.txt', 'w') as file:
    file.write('Total Reviews Processed: {}\n'.format(valid+invalid))
    file.write('Valid Reviews: {}\n'.format(valid))
    file.write('Invalid Reviews: {}\n\n'.format(invalid))
    file.write('Top 3 Products with Highest Average Ratings:\n')
    for product, rating in top3_products:
        file.write('Product ID: {}    Average Rating: {:.2f}\n'.format(product, rating))

print("\nSummary written to summary.txt")
