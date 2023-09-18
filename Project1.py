import requests
import sys

def download_and_save_text(url, output_file):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the entire text content of the page
            text_data = response.text

            # Save the text data to the output file
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(text_data)
            
            print(f"Content from {url} has been saved to {output_file}.")
        else:
            print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__== "__main__":
    if len(sys.argv) != 3:
        print("Usage: python your_program_name.py URL output_file.txt")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2]

    download_and_save_text(url, output_file)