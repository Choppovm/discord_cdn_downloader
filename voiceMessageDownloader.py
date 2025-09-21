import requests # i despise how this library forces you to use snake_case instead of camelCase can we get someone to fix this i beg
import colorama # same here please just use anything but underscores

# Terminal formatting
colorama.init(autoreset=True)
def success(msg):
    print(f"{colorama.Style.BRIGHT}{colorama.Back.GREEN}[SUCCESS]{colorama.Style.RESET_ALL} | {msg}")
def failure(msg):
    print(f"{colorama.Style.BRIGHT}{colorama.Back.RED}[FAILURE]{colorama.Style.RESET_ALL} | {msg}")

# Reading urls from the file (MAKE SURE TXT FILE IS IN THE SAME DIRECTORY, RE-NAME AS REQUIRED)
with open ("voiceLines.txt", "r") as file:
    urls = [line.strip() for line in file if line.strip()]

for i, url in enumerate(urls, start=1):
    try:
        url = url.replace("&amp;", "&") # Sanitization for step 2
        response = requests.get(url, stream=True)
        response.raise_for_status() # checks for any errors

        # Save each file with unique name
        filename = f"voiceMessage-{i}.ogg" # change file format accordingly
        with open(filename, "wb") as fileOut:
            for chunk in response.iter_content(chunk_size=8192):
                fileOut.write(chunk)
        success(f"Downloaded {filename}.")
    except Exception as err:
        failure(f"Failed to download {url} (Error: {err})")