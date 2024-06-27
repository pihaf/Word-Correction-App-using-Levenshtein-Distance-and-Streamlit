# Word-Correction-App-using-Levenshtein-Distance-and-Streamlit

Welcome to the Word Correction App! This application uses Levenshtein distance to provide word correction suggestions. It is built using Streamlit, a fast and easy way to create and share beautiful, custom web apps for machine learning and data science.

## Features

- **Word Input**: Enter any word you wish to check for corrections.
- **Suggestions**: The app provides a list of suggested corrections based on the Levenshtein distance.
- **User-friendly Interface**: Built with Streamlit, the app offers a simple and intuitive interface.

## Installation

To run this app locally, you'll need to have Python installed. Follow these steps to get started:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/pihaf/Word-Correction-App-using-Levenshtein-Distance-and-Streamlit.git
    cd word-correction-app
    ```

2. **Create a virtual environment** (optional):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install streamlit**:
    ```bash
    pip install streamlit
    ```
    
**Notes:** To use the app, after installation, you only need the `src` folder to run the app, other folder and files are sonarcloud configurations. You can delete other files and folders.

## Running the App

To run the app, execute the following command in your terminal:
```bash
cd src
streamlit run main.py
```
