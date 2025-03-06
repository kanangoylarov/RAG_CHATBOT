Cocktail Chatbot - FastAPI Project
This project is a Cocktail Chatbot application integrated with Pinecone and built with FastAPI. Users can ask questions about cocktails and get suggestions based on their queries.

🚀 Getting Started
Prerequisites
Python 3.7+
FastAPI
Uvicorn
Pinecone
Sentence-Transformers
Pandas
HTML (for static files)
📦 Installation
Clone the Repository
Clone the repository to your local machine using the following command:

git clone https://github.com/your_username/cocktail-chatbot.git
cd cocktail-chatbot
Install Dependencies
Create a virtual environment and install the required Python packages:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
🔧 Configuration
Set up Pinecone API Key
To use Pinecone, you will need an API key. Sign up for Pinecone, get your API key, and add it to the .env file:

PINECONE_API_KEY=YOUR_API_KEY
Index Configuration
If you haven't created a Pinecone index yet, the application will automatically create one when it runs. Make sure to set the correct dimension for the vectors.

🏃‍♂️ Running the Application
Start with Uvicorn
To run the FastAPI application, use the following command:
uvicorn main:app --reload
This will start the FastAPI app and run it locally.

Test the API
Once the application is running, you can test it via Swagger UI:

Swagger UI: http://127.0.0.1:8000/docs
Redoc UI: http://127.0.0.1:8000/redoc
🌍 Access the Web Page
You can access the HTML page at http://127.0.0.1:8000/static/index.html. The page will take user queries and query the Pinecone database for cocktail suggestions.

📑 API Endpoints
1. /query
The API endpoint that processes a cocktail query and returns the most relevant results.

Method: POST
Request Body:
json
Copy
Edit
{
  "query": "Generate a cocktail with Gin and Lemon Juice"
}
Response:
json
Copy
Edit
{
  "matches": [
    {
      "id": "1",
      "score": 0.98,
      "text": "Gin and Lemon Juice cocktail recipe"
    }
  ]
}
🔄 Database
Pinecone
Pinecone is used to store cocktail data as vectors. You can add new data to Pinecone and query it as needed.

📝 Contributing
Fork the repo.
Create a new branch (git checkout -b feature/feature_name).
Make your changes and commit them (git commit -am 'Add new feature').
Push your branch (git push origin feature/feature_name).
Create a pull request.
📄 License
This project is licensed under the MIT License.

Feel free to open an issue if you have any questions or contribute to the project!
