
# Webpage Email Scraper

<a>
  <img src="https://example.com/email-scraper-logo.png" alt="Logo" height="350" width="650" />
</a>

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshot](#screenshot)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [Author](#author)

## Description
`Email Scraper` is a Python script designed to scrape email addresses from a given webpage URL. Using the `requests` library for making HTTP requests and `BeautifulSoup` for parsing HTML content, this tool extracts email addresses and allows you to export the results in both CSV and JSON formats.

## Features
- **Email Extraction:** Identifies and extracts email addresses from the webpage.
- **CSV Export:** Exports extracted email addresses to a CSV file.
- **JSON Export:** Exports extracted email addresses to a JSON file.

## Installation
To install and run this project, follow these steps:

```sh
pip install requests
pip install beautifulsoup4
pip install pandas
```

## Usage
To use the `Email Scraper` script, follow these steps:

1. **Run the Script:**
   ```sh
   python email_scraper.py
   ```

2. **Enter URL:**
   When prompted, enter the URL of the webpage you want to scrape for email addresses.

3. **Choose Export Format:**
   You will be asked to choose the export format (`csv` or `json`). The script will save the extracted email addresses accordingly.

   Example:
   ```python
   Enter the URL to scrape: https://example.com
   Choose export format (csv/json): csv
   ```

4. **Check Output Files:**
   The script will generate `emails.csv` or `emails.json` with the extracted email addresses.

## Screenshot

<a>
  <img src="#" alt="Screenshot" width="650" />
</a>

## Future Enhancements

### 1. **Advanced Email Detection**
   - **Description**: Implement additional techniques to detect email addresses more accurately, including handling obfuscated emails.
   - **Benefit**: Improves the accuracy of email extraction.

### 2. **Multi-page Scraping**
   - **Description**: Extend the tool to scrape multiple pages or follow links to extract emails from entire websites.
   - **Benefit**: Increases the scope of email extraction.

### 3. **Customizable Export Options**
   - **Description**: Add options for customizing the format of the exported data, such as adding filters or choosing specific fields.
   - **Benefit**: Provides more flexibility for users.

### 4. **Error Handling and Logging**
   - **Description**: Implement robust error handling and logging to manage issues like failed requests or invalid URLs.
   - **Benefit**: Enhances the reliability and usability of the tool.

### 5. **User Interface**
   - **Description**: Develop a graphical user interface (GUI) for easier interaction with the tool.
   - **Benefit**: Provides a more user-friendly experience.

## Contributing

Feel free to submit issues and enhancement requests. Pull requests are also welcome.


## Author

#### Vincent Chimaobi (CyberGhoxt)

Connect with me on 
- [GitHub](https://www.github.com/VincentRitchie/VincentRitchie)
- [LinkedIn](https://www.linkedin.com/in/vincent-chimaobi-53b458216?trk=contact-info)
- [X](https://x.com/vin_chimaobi042)
