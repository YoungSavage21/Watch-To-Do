# Watch To Do

Watch To Do is a web app that allows you to search for movies and add them to your watchlist. It's built using HTML, CSS, Bootstrap, Python, Flask, SQLite3, and gets its data from TMDB API.

## What I learned

Through building this project, I had the opportunity to learn and apply several key skills:

- **Python, Flask, and Jinja:** I gained proficiency in Python programming and using the Flask framework for web development. Jinja templating helped me seamlessly integrate dynamic content into HTML templates.
- **API Integration:** I learned how to interact with external APIs, specifically the TMDB API, to fetch real-time movie data and display it to users.
- **Bootstrap:** While working on the front end, I gained a basic understanding of Bootstrap, enabling me to create responsive and visually appealing pages.

## Installation

To run the project, you'll need to have Python and Flask installed. Additionally, make sure you have the CS50 Python library installed. Follow these steps to set up and run the app:

1. Clone the repository to your local machine.
2. Install Flask by running: `pip install Flask`.
3. Install the CS50 library by running: `pip install cs50`.
4. Navigate to the project directory in your terminal.
5. Run the app by executing: `python app.py`.

The app will start and provide you with a local server address to access the app in your web browser.

## Files and Components

- `app.py`: This is the heart of the project, where Flask handles routing and serves as the backbone of the web app.
- `api.py`: This file is responsible for making requests to the TMDB API to fetch movie data based on user searches.
- `list.db`: This SQLite database stores user watchlist information, ensuring that their added movies are remembered.
- `templates`: This folder contains the HTML templates for each page in the web app, including `layout.html` which serves as the base layout for all pages.
- `static`: This folder houses `style.css`, which defines the custom styling for the app, and a default image used for movies without poster images.

## Challenges and Solutions

During development, I encountered various challenges that pushed me to expand my problem-solving skills. The robust resources available on the internet, including Google, YouTube tutorials, and ChatGPT, played a significant role in helping me overcome these hurdles.

## Future Plans

I have exciting plans to enhance Watch To Do further:

- **TV Show Support:** I intend to extend the app's functionality to include TV show searches and watchlists.
- **Filtering Options:** I'm planning to implement filtering options, allowing users to refine their searches based on criteria like genre, release year, and more.

Happy movie watching with Watch To Do!

![Screenshot (214)](https://github.com/YoungSavage21/Watch-To-Do/assets/128630865/572f95d9-764d-48ac-936d-990477027c74)

![Screenshot (215)](https://github.com/YoungSavage21/Watch-To-Do/assets/128630865/f64bde39-96a6-481f-81e7-ad9aad09db0e)

![Screenshot (216)](https://github.com/YoungSavage21/Watch-To-Do/assets/128630865/34404c09-83be-42d1-8a4b-c9bcac7a28dc)

![Screenshot (217)](https://github.com/YoungSavage21/Watch-To-Do/assets/128630865/69f57d89-b3fa-4009-8d8f-5ed633a0f93f)
