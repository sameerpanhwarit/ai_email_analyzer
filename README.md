# Email Analysis API

This is a Django-based API that analyzes emails for summary, sentiment, and urgency.

## Features

*   **Email Analysis:** Analyzes the content of an email.
*   **Summarization:** Provides a summary of the email content.
*   **Sentiment Analysis:** Determines the sentiment of the email (e.g., positive, negative, neutral).
*   **Urgency Detection:** Identifies the urgency of the email.

## API Endpoint

### Analyze Email

*   **URL:** `api/analyze/`
*   **Method:** `POST`
*   **Payload:**

    ```json
    {
        "text": "Your email content goes here."
    }
    ```

*   **Success Response:**

    *   **Code:** `201 CREATED`
    *   **Content:**

        ```json
        {
            "id": 1,
            "text": "Your email content goes here.",
            "summary": "This is a summary of the email.",
            "sentiment": "Positive",
            "urgency": "Low"
        }
        ```

## Technologies Used

*   **Backend:** Django, Django Rest Framework
*   **Machine Learning Models:**
    *   Summarization: `sshleifer/distilbart-cnn-12-6` (Hugging Face)
    *   Sentiment Analysis: `distilbert-base-uncased-finetuned-sst-2-english` (Hugging Face)
*   **Deployment:** Docker, Gunicorn

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**

    Create a `.env` file in the project root and add your Hugging Face API key:

    ```
    API_TOKEN=your_hugging_face_api_key
    ```

5.  **Run database migrations:**

    ```bash
    python manage.py migrate
    ```

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Docker

This project includes a `Dockerfile` for easy containerization.

1.  **Build the Docker image:**

    ```bash
    docker build -t email-analysis-api .
    ```

2.  **Run the Docker container:**

    ```bash
    docker run -p 8000:8000 -e API_TOKEN=your_hugging_face_api_key email-analysis-api
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. 