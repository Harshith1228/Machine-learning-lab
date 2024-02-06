def one_hot_encoding(categories):
    unique_categories = list(set(categories))
    num_categories = len(unique_categories)
    encoding_map = {category: i for i, category in enumerate(unique_categories)}

    encoded_data = []
    for category in categories:
        encoding = [0] * num_categories
        encoding[encoding_map[category]] = 1
        encoded_data.append(encoding)

    return encoded_data

categories = ['cat', 'dog', 'cat', 'bird', 'dog']
encoded_data = one_hot_encoding(categories)
print(encoded_data)
