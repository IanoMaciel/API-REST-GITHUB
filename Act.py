
#import library
from pydriller import Repository

# Ansálise do primeiro repositório remoto
url = "https://github.com/nektos/act"

for index, commit in enumerate(Repository(url).traverse_commits()):
    print(index, "Hash: " + commit.hash)
    print("Commit: " + commit.msg)
    print("Author: " + commit.author.name)
    print("-------------------------------------\n")

