#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
# author = Author("Carry Bradshaw")
# print("Author Name:", author.name)

# magazine = Magazine("Vogue", "Fashion")
# print("Magazine Name:", magazine.name)
# print("Magazine Category:", magazine.category)

# author = Author("Carry Bradshaw")
# magazine = Magazine("Vogue", "Fashion")
# article = Article(author, magazine,
#                   "How to wear a tutu")
# print("Article Title:", article.title)
# print("Article Author:", article.author.name)
# print("Article Magazine:", article.magazine.name)
# print("Magazine Category:", magazine.category)


# author_2 = Author("Nathaniel Hawthorne")
# article_2 = Article(author_2, magazine, "Dating life in NYC")
