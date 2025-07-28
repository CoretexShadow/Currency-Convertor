# Currency Converter Project

The Currency Converter Project is designed to be a practical application leveraging the Python programming language to create a tool that allows users to convert amounts between different currencies. This project utilizes the ExchangeRate-API for fetching real-time exchange rate data and provides an interface for users to specify the amount in one currency and get the equivalent amount in another currency. Additionally, the project features a user-friendly UI using Streamlit, making it accessible for non-technical users to perform currency conversions with ease.

A solution within this project is expected to deliver the following outcomes:

- **Currency Exchange Rate Retrieval**: Users should be able to input two currencies (e.g., USD and EUR) and retrieve the current exchange rate between them using the ExchangeRate-API.
- **Currency Conversion**: Given an amount in one currency, users should be able to convert it to the equivalent amount in another currency. The program will apply the latest exchange rates to perform this calculation.
- **Graphical User Interface (GUI)**: A Streamlit-based GUI that allows users to perform the above operations through a web interface. The GUI should be intuitive and user-friendly, enabling users with no technical background to use the application with ease.

### Technical Notes
- The project implements a **TTL (Time-To-Live) cache** with a 24-hour expiration, ensuring that exchange rate data is refreshed daily for up-to-date conversions while minimizing API calls.

## Requirements
To run this project, you will need the following:

- Python 3.x installed on your machine.
- An internet connection to access the ExchangeRate-API.
- An API key from https://api.exchangerate-api.com to authenticate requests.
- Installation of required Python libraries as listed in the `requirements.txt` file.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Set up your API key in `Currency_Convertor.py`
3. Run the Streamlit app: `streamlit run gui/Gui.py`

## Project Structure
The project is structured as follows:
```
├── gui/                                        # Directory for the Streamlit GUI application
│   └── Gui.py                            # Main Streamlit application file
│   └── Constants.py                   # File containing the list of supported currency codes
├── src/                                        # Directory for source code
│   └── Currency_Convertor.py # Logic for currency conversion and API interactions
├── .gitignore                              # File to specify intentionally untracked files for Git
├── LICENSE                            # Project license information
├── README.md                     # Project  documentation and overview
├── requirements.txt                  # List of Python dependencies required to run the project
```

## Future Enhancements
The project has been designed with expandability in mind. Future enhancements could include:

- Extending the Streamlit UI to include historical exchange rate data and graphs.
- Adding functionality to alert users when an exchange rate reaches a certain threshold.
- Incorporating a database to store user queries and perform analytics.
