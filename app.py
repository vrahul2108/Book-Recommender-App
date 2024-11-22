from flask import Flask, render_template, request
import pickle
import numpy as np


# Load the pre-saved pickle files
def load_pickle_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


popular_df = load_pickle_file('popular.pkl')
pt = load_pickle_file('pt.pkl')
books = load_pickle_file('books.pkl')
similarity_scores = load_pickle_file('similarity_scores.pkl')

# Initialize the Flask application
app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=popular_df['Book-Title'].to_list(),
        author=popular_df['Book-Author'].to_list(),
        image=popular_df['Image-URL-M'].to_list(),
        votes=popular_df['num_ratings'].to_list(),
        rating=popular_df['avg_rating'].to_list()
    )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')

    # Check if user input exists in the pivot table
    if user_input not in pt.index:
        return render_template(
            'recommend.html',
            data=[],
            message="Book not found in our database. Please try another book."
        )

    # Fetch similar items based on the similarity scores
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True
    )[1:5]

    data = []
    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')
        if not temp_df.empty:
            item = [
                temp_df['Book-Title'].values[0],
                temp_df['Book-Author'].values[0],
                temp_df['Image-URL-M'].values[0]
            ]
            data.append(item)

    return render_template('recommend.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
