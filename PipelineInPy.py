"""Example how to use toolz library to create pipeline in python.
I wanted to try this function after reading this article 
https://medium.com/@ayush-thakur02/wait-what-are-pipelines-in-python-628f4b5021fd. 
Unfortunateley there was an error in the article so I need to change syntax slightly"""
from toolz import pipe

Text = "How to use function pipe to create pipeline in Python."

result = pipe(Text,
              lambda x : x.split(" "),
              lambda x: map(lambda x: x.capitalize(),x),
              lambda x: filter(lambda x: x!='In',x),
              lambda x: "-".join(x))
print(result)
