import spacy
# Loading the advanced language model.
nlp = spacy.load('en_core_web_md')


def next_movie(description):
    movies = open("movies.txt", "r")
    # Setting up an empty list to store the movie titles and descriptions.
    movie_list = []

    # Splitting movies into title and description and appending them to the empty list.
    for movie in movies:
        movie_list.append(movie.split(':'))

    # An empty list to store the similarity values.
    similarity_list = []

    movie_description = nlp(description)

    for i in range(0, len(movie_list)):
        # Passing in a movie description and checking its similarity to each description in movies.txt.
        similarity_list.append(nlp(movie_list[i][1]).similarity(movie_description))

    most_similar = max(similarity_list)
    # Getting the index of the most similar movie.
    max_similarity_index = similarity_list.index(most_similar)

    # return movie title similar to watched movie
    return movie_list[max_similarity_index][0]

hulk = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""


print(f"You might like {next_movie(hulk)}")