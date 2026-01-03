🌐 Language Detection Using Python

A simple and efficient Language Detection System built using Python that automatically identifies the language of a given text input. The project leverages Natural Language Processing (NLP) techniques to detect the language and displays both the ISO 639-1 language code and the full language name with colored terminal output for better readability.

📌 Features

🔍 Automatically detects the language of input text

🌎 Supports multiple languages (English, Tamil, Hindi, French, German, Japanese, Telugu, Kannada, Korean, Arabic, etc.)

🎨 Colored terminal output using colorama

🧠 Uses NLP-based language detection

🧩 Simple, modular, and easy-to-extend code

🛠️ Technologies Used

Python

langdetect – Language detection library based on NLP

colorama – Colored terminal output

📂 Project Structure
Language-Detection-Using-Python/
│
├── language_detection.py
├── README.md
└── requirements.txt

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/your-username/Language-Detection-Using-Python.git
cd Language-Detection-Using-Python


Install required dependencies

pip install langdetect colorama


Run the program

python language_detection.py

🧪 Example Usage
text = "வணக்கம்"


Output:

Detected language code: ta
Detected language: Tamil

🌍 Supported Languages

The system supports several commonly used languages including:

English

Tamil

Hindi

French

German

Japanese

Telugu

Kannada

Korean

Arabic

Marathi

Bangla
(and more)

🚀 Use Cases

Multilingual chatbots

Social media text analysis

Language-based content filtering

Translation pipelines

Document classification systems

🔮 Future Enhancements

GUI or Web-based interface

Batch language detection

Confidence score for predictions

Integration with translation APIs

REST API support

🤝 Contributing

Contributions are welcome!
Feel free to fork the repository, create a new branch, and submit a pull request.

📄 License

This project is open-source and available under the MIT License.

⭐ Acknowledgments

langdetect for language detection

colorama for terminal styling
