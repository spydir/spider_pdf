```markdown
# PDF Spider and Downloader

## Overview

This Python script is a simple web spider that crawls a website and lists all the PDF files it finds. Additionally, it provides an option to download these PDF files.

## Features

- Spider through a website and list all PDF files.
- Download PDF files with the `-d` or `--download` option.

## Usage

### Prerequisites

Before running the script, make sure you have Python 3.x installed on your system.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/pdf-spider.git
   ```

2. Navigate to the project directory:

   ```bash
   cd pdf-spider
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Script

To list all PDF files on a website:

```bash
python pdf_spider.py https://example.com
```

To download all PDF files:

```bash
python pdf_spider.py https://example.com -d
```

### Options

- `-d` or `--download`: Download PDF files.

## License

This project is open-source and available under the [MIT License](LICENSE). You are free to use, modify, and distribute this software for any purpose. See the [LICENSE](LICENSE) file for more details.

## Contribution

Contributions are welcome! If you find a bug or have an enhancement in mind, please open an issue or submit a pull request.

## Acknowledgments

Special thanks to the open-source community for providing the libraries used in this project.

```

Remember to replace `"https://example.com"` with the actual website URL where you want to spider for PDF files. Additionally, replace `"yourusername/pdf-spider"` in the clone step with the actual URL of your GitHub repository.

You can use this `README.md` as a starting point and customize it further to provide more specific information about your Python script and its usage.