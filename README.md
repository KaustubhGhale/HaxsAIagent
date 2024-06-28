# HaxsAIagent
This repository contains the code and documentation for an AI agent capable of real-time interactions to solve real-world problems autonomously. Leveraging the capabilities of the Groq API, the AI agent can understand user objectives, generate and prioritize action items, execute tasks, and adapt based on real-time feedback.


# AI Chat Application with Flask

This repository contains a simple web-based AI chat application using Flask and the Groq API. Users can interact with an AI model via a web interface or a command-line interface (CLI).

## Features

- Web interface for chatting with the AI.
- Command-line interface for chatting with the AI.
- Easy to set up and deploy.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install flask
    pip install groq
    ```

## Usage

### Web Interface

1. Set your Groq API key in the `app.py` file:
    ```python
    client = Groq(api_key="your_api_key")
    ```

2. Run the Flask application:
    ```sh
    python app.py
    ```

3. Open your browser and navigate to `http://127.0.0.1:5000` to start chatting with the AI.

### Command-Line Interface

1. Set your Groq API key in the `app.py` file:
    ```python
    client = Groq(api_key="your_api_key")
    ```

2. Run the CLI:
    ```sh
    python cli.py
    ```

3. Follow the on-screen instructions to chat with the AI via the command line.

## Files

- `app.py`: Main Flask application file.
- `cli.py`: Command-line interface script.
- `templates/index.html`: HTML template for the web interface.
- `static/`: Directory for static files (CSS, JavaScript).


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

  
## Libraries

The following libraries are used in this project:

- Flask
- Requests
- Gunicorn (for production deployment)
- Groq (API client)

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Requests](https://docs.python-requests.org/)
- [Gunicorn](https://gunicorn.org/)
- [Groq](https://groq.com/)

