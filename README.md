# luckyrandomjokes
A simple web application that generates random lottery numbers and a joke on each page reload. The app is built using Flask for the backend, Bootstrap for styling, and includes dynamic content rendering.

# Lottery & Jokes Web App

## Overview
This is a simple web application that generates random lottery numbers and a joke on each page reload. The app is built using Flask for the backend, Bootstrap for styling, and includes dynamic content rendering.

## Features
- Generates a set of random lottery numbers.
- Displays a random joke.
- Uses Flask as the web framework.
- Styled with Bootstrap and custom CSS.
- Refresh button to generate new results.

## Project Structure


📦 Project Root
├── 📄 main.py         # Flask application logic
├── 📂 templates
│   ├── 📄 index.html  # Main HTML page
├── 📂 static
│   ├── 📄 styles.css  # Custom styling
└── 📄 README.md       # Documentation

## Installation & Setup
### Prerequisites

Ensure you have Python installed (preferably Python 3.7+).

### Steps
1. Clone the repository:
   git clone <repository-url>
   cd <project-directory>


2. Create a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows


3. Install dependencies:
   pip install flask


4. Run the Flask application:
   python main.py


5. Open a web browser and visit:
   http://127.0.0.1:5000/


## File Details

### `main.py`
- Initializes the Flask application.
- Generates random lottery numbers.
- Fetches a random joke.
- Renders the `index.html` template with generated data.

### `index.html`
- HTML template that displays lottery numbers and a joke.
- Uses Flask templating to dynamically insert content.
- Includes Bootstrap for styling and Font Awesome for icons.

### `styles.css`
- Custom styles for the page.
- Uses a gradient background.
- Styles the lottery numbers and joke text.

## Technologies Used

- **Python** (Flask)
- **HTML/CSS** (Bootstrap for layout)
- **JavaScript** (for interactivity)
- **Font Awesome** (icons)

## Future Enhancements

- Add API integration for fetching live jokes.
- Allow users to pick custom lottery number ranges.
- Implement a dark mode toggle.

## License

This project is licensed under the MIT License.
