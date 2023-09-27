
# PDF Downloader with Tkinter

This Python application allows you to search for PDF files online based on a given query and download them to your local directory. It features a graphical user interface (GUI) built using Tkinter for easy interaction.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [License](#license)

## Features

- Search for PDF files online.
- Specify the number of search results to fetch.
- Download PDFs to a local directory.
- Real-time updates and error handling.
- Clear the display or exit the application with buttons.

## Getting Started

### Prerequisites

Before using this application, you need to have Python 3.x installed on your system. If Python is not already installed, you can download it from the official website: [Python Downloads](https://www.python.org/downloads/).

You'll also need to install some Python libraries, which can be done using `pip`:

```bash
pip install requests beautifulsoup4
```

### Installation

1. Clone or download this repository to your local machine.

```bash
git clone https://github.com/yourusername/pdf-downloader-tkinter.git
```

2. Navigate to the project directory.

```bash
cd pdf-downloader-tkinter
```

3. Run the application:

```bash
python main.py
```

## Usage

1. Launch the application by running `main.py`.
2. Enter your search query (topic) in the first input field.
3. Specify the number of search results you want in the second input field.
4. Click the "Search" button to start the search. The button will change to "Searching..." during the search.
5. Real-time updates will be displayed in the text widget.
6. To clear the display, click the "Clear Display" button.
7. To exit the application, click the "Exit" button.

## How It Works

- The application uses Tkinter to create a graphical user interface.
- It makes use of the `requests` library to fetch search results from Google.
- The `beautifulsoup4` library is used to parse the HTML of search results.
- PDFs are downloaded using the `requests` library.
- Updates and errors are displayed in a text widget.
- A separate thread is used for the search to prevent UI blocking.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

You can customize this README by replacing the placeholders with your specific project details and additional information. Make sure to include any usage instructions, dependencies, and licensing information that is relevant to your application.
