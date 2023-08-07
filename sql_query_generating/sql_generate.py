import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('punkt')

def generate_sql_condition(pos_tags):
    column = None
    operator = None
    value = None

    word_to_column = {
        'name': 'user_name',
        'age': 'user_age',
        # Add more mappings as needed
    }

    word_to_operator = {
        'greater than': '>',
        'less than': '<',
        # Add more mappings as needed
    }

    for word, tag in pos_tags:
        if tag == 'NN' and word in word_to_column:
            column = word_to_column[word]
        elif tag == 'VB' and word in word_to_operator:
            operator = word_to_operator[word]
        elif tag == 'CD':  # CD is the tag for numbers
            value = word
    
    if column and operator and value:
        sql_condition = f"{column} {operator} {value}"
        return sql_condition
    else:
        return None

user_input = input("Enter your natural language query: ")
tokens = word_tokenize(user_input)
pos_tags = pos_tag(tokens)

sql_condition = generate_sql_condition(pos_tags)

if sql_condition:
    database_name = input("Enter your database name: ")
    query = f"SELECT * FROM {database_name}.users WHERE {sql_condition}"
    print("Generated SQL query:")
    print(query)
else:
    print("Unable to generate a valid SQL condition.")
