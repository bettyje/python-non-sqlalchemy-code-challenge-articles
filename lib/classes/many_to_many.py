class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Titles must be between 5 and 50 characters")
        if not isinstance(author, Author):
            raise TypeError("authors must be of type Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazines must be of type Magazine")
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

#  Creates and returns an Article linking the Author to a valid Magazine with the given title
    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise TypeError("magazines must be of type Magazine")
        return Article(self, magazine, title)

# Returns a list of unique topic areas (categories) for all articles by the Author.
    def topic_areas(self):
        if not self.articles():
            return None
        categories = set()
        for article in self.articles():
            categories.add(article.magazine.category)
            return list(categories)


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name


# Returns a list of all the articles the author has written

    def articles(self):
        return [article for article in Article.all if article.author == self]


# Returns a unique list of magazines for which the author has contributed to

    def magazines(self):
        return list({article.magazine for article in self.articles()})


# Creates and returns a new Article instance and associates it with that author, the magazine provided

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        return Article(self, magazine, title)


# Returns a unique list of strings with the categories of the magazines the author has contributed to

    def topic_areas(self):
        return list({magazine.category for magazine in self.magazines()}) or None


class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        elif len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self.name = name

        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value


# Returns a list of all the articles the magazine has published

    def articles(self):
        return [article for article in Article.all if article.magazine == self]


# Returns a unique list of authors who have written for this magazine

    def contributors(self):
        return list({article.author for article in self.articles()})


# Returns a list of the titles strings of all articles written for that magazine

    def article_titles(self):
        return [article.title for article in self.articles()] or None

# Returns a list of authors who have written more than 2 articles for the magazine
    def contributing_authors(self):
        authors_count = {}
        for author in self.contributors():
            authors_count[author] = 0

        for article in self.articles():
            if article.author in authors_count:
                authors_count[article.author] += 1

        contributing_authors = []
        for author, count in authors_count.items():
            if count > 2:
                contributing_authors.append(author)

        if contributing_authors:
            return contributing_authors
        else:
            return None


# Returns the Magazine instance with the most articles
    # @classmethod
    # def top_publisher(cls):
    #     if not cls.all:
    #         return None

    #     return top_magazine
