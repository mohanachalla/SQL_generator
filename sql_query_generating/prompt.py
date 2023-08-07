import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_sql_query(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.7,  # Adjust the randomness as needed
    )
    return response.choices[0].message["content"]

def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_sql_query(prompt)  # Use the SQL generator function
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))

    return pn.Column(*panels)

import panel as pn
pn.extension()

panels = []  # Collect display

context = [{'role': 'system', 'content': """
You are SQLBot, an automated service to assist users in generating SQL queries. \
You can help users create SELECT queries to retrieve data from a database. \
Provide the necessary information like the tables, columns, conditions, and sorting. \
Remember to provide clear instructions and examples. \
For example, "Retrieve all customers from the 'orders' table where the total amount is greater than 100." \
Feel free to ask for additional details to refine the query. \
"""}]  # Accumulate messages

inp = pn.widgets.TextInput(value="Generate an SQL query", placeholder='Enter query here…')
button_conversation = pn.widgets.Button(name="Generate!")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard
