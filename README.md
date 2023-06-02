# AI Hackfest 2023 - Receipt Analyzer

> **Note: This project is still in progress and is currently at the MVP stage.**

## Description

The AI Hackfest 2023 Receipt Analyzer is a Flask web application developed as part of the AI Hackfest organized by Major League Hackers (MLH). The goal of this project is to create a receipt scanning and categorization tool using Optical Character Recognition (OCR), a Large Language Model (GPT 3.5), and a MongoDB database for data storage. Additionally, it provides analytics capabilities using the Pandas library in Python.

## Technologies Used

The following technologies were used to develop the AI Hackfest 2023 Receipt Analyzer:

- Python
- HTML & CSS
- Flask
- EasyOCR
- GPT (Large Language Model)
- MongoDB

## Dependencies

Make sure the following dependencies are installed:

- Python
- Flask
- EasyOCR
- GPT
- MongoDB

## Features

The Receipt Analyzer web application offers the following features:

1. Receipt Scanning: Users can upload images of receipts, which are then processed using Optical Character Recognition (OCR) to extract text from the images.
2. Purchase Categorization: The extracted text is then passed through a Large Language Model (GPT 3.5) to categorize the purchases mentioned in the receipt.
3. Data Storage: The categorized purchase data is stored in a MongoDB database for future retrieval and analysis.
4. Analytics: The application provides analytics capabilities using the Pandas library in Python. Users can generate reports, perform data analysis, and visualize the purchase data.

## Installation and Usage

To run the AI Hackfest 2023 Receipt Analyzer locally, please follow these steps:

1. Clone the repository: `git clone https://github.com/shayaansultan/ai-hackfest-2023.git`
2. Navigate to the project directory: `cd ai-hackfest-2023`
3. Install the required dependencies mentioned above.
4. Set up a MongoDB database and update the database configuration in `config.py`.
5. Run the Flask application: `python app.py`
6. Access the web application in your browser at `http://localhost:5000`.

## Future Enhancements

While the AI Hackfest 2023 Receipt Analyzer is currently at the MVP stage, there are several areas for future enhancement:

- Improved OCR Accuracy: Enhancing the OCR process to improve accuracy and handle various types of receipts.
- Refining Categorization: Further training the Large Language Model (GPT 3.5) to better categorize purchases and handle a wider range of receipt formats.
- User Authentication: Implementing user authentication and authorization to secure the application and enable personalized experiences.
- Advanced Analytics: Adding advanced data visualization and analytics features to provide deeper insights into purchase patterns and trends.
- Deployment: Deploying the application to a cloud hosting platform to make it accessible from anywhere.

## Contributing

Contributions to the AI Hackfest 2023 Receipt Analyzer project are welcome. If you have any ideas, suggestions, or bug reports, please feel free to open an issue or submit a pull request.

## License

The AI Hackfest 2023 Receipt Analyzer project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

We would like to thank Major League Hackers (MLH) for organizing the AI Hackfest 2023 and providing the opportunity to develop this project. I would also like to thank @YuvBindal for his contributions to this project.

Special thanks to the creators and maintainers of the following libraries used in this project:

- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- EasyOCR: [https://github.com/JaidedAI/EasyOCR](https://github.com/JaidedAI/EasyOCR)
- GPT: [https://github.com/openai/gpt-3.5](https://github.com/openai/gpt-3.5)
