import argparse
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_pdf_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        pdf_links = []

        for link in soup.find_all('a', href=True):
            href = link.get('href')
            absolute_url = urljoin(url, href)
            
            if href.endswith('.pdf'):
                pdf_links.append(absolute_url)
            elif absolute_url.startswith(url):
                pdf_links += get_pdf_links(absolute_url)

        return pdf_links
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def download_pdfs(pdf_links, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for pdf_link in pdf_links:
        try:
            response = requests.get(pdf_link)
            response.raise_for_status()
            filename = os.path.join(output_dir, os.path.basename(pdf_link))
            with open(filename, 'wb') as pdf_file:
                pdf_file.write(response.content)
            print(f"Downloaded: {filename}")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {pdf_link}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Recursive spider through a website and list/download PDFs.")
    parser.add_argument("url", help="URL of the website to spider")
    parser.add_argument("-d", "--download", action="store_true", help="Download PDFs")
    parser.add_argument("-o", "--output", default="pdfs", help="Output directory for downloaded PDFs (default: 'pdfs')")

    args = parser.parse_args()
    url = args.url
    output_dir = args.output

    pdf_links = get_pdf_links(url)

    if pdf_links:
        print("PDFs found:")
        for pdf_link in pdf_links:
            print(pdf_link)

        if args.download:
            download_pdfs(pdf_links, output_dir)
    else:
        print("No PDFs found on the website.")

if __name__ == "__main__":
    main()
