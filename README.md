# Book Recommender System

## Overview
This project is a **Book Recommender System** built using **collaborative filtering techniques**. It suggests books to users based on their preferences and the ratings provided by other users. The goal is to help users discover books they are likely to enjoy.

## Features
- **Collaborative Filtering**: Uses user-item interaction data to provide recommendations.
- **Content-based Suggestions**: (Optional) Suggests books similar to the ones a user has liked.
- **Interactive Web Interface**: A user-friendly web application built using Flask for interacting with the recommender system.
- **Data Visualization**: Displays trends and insights based on user ratings.

## Dataset
The system uses three CSV files:
1. **Books.csv**: Contains metadata about books (e.g., title, author, publication year).
2. **Users.csv**: Contains anonymized user information.
3. **Ratings.csv**: Contains user ratings for different books.

## Techniques Used
- **Collaborative Filtering**:
  - User-based filtering: Recommends books liked by similar users.
  - Item-based filtering: Suggests books similar to those the user has rated highly.
- **Cosine Similarity**: Measures the similarity between users or items based on their ratings.
- **Data Cleaning**: Handles missing or inconsistent data to improve recommendation quality.

## Requirements
To run this project, ensure you have the following installed:

### Python Libraries:
- `pandas`
- `numpy`
- `scikit-learn`
- `Flask`
- `Jinja2`
- `matplotlib` (for optional visualization)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/vrahul2108/Book-Recommender-App.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Book-Recommender-App
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```
3. Interact with the recommender system by searching for books and viewing personalized recommendations.

## File Structure
```
Book-Recommender-App/
|-- app.py                  # Flask application
|-- Books.csv               # Book metadata
|-- Ratings.csv             # User ratings
|-- Users.csv               # User data
|-- templates/              # HTML templates for Flask
|-- static/                 # CSS and JavaScript files
|-- book-recommender-system.ipynb  # Jupyter Notebook for data exploration and model development
```

## How It Works
1. **Data Preprocessing**:
   - Load the datasets.
   - Handle missing values and outliers.
   - Normalize user ratings.

2. **Model Training**:
   - Compute similarity matrices using collaborative filtering.
   - Implement algorithms to generate recommendations.

3. **Web Application**:
   - Allow users to view recommendations and search for books.
   - Render recommendations dynamically based on user input.

## Future Enhancements
- **Hybrid Approach**: Combine collaborative filtering with content-based recommendations.
- **Real-time Data**: Allow users to provide feedback on recommendations.
- **Improved Scalability**: Use distributed systems to handle large datasets.

## Contributions
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

---

Happy coding! If you have any questions, feel free to reach out.

