# Import the necessary library
from googlesearch import search

# Get the user's search query
query = input("Enter your search query: ")

# Perform the Google search and print the results
for j in search(query, num=10, stop=10, pause=2):
    print(j)
