import requests

# Corrected URL of the image
url = "https://images.hindustantimes.com/img/2024/08/16/550x309/A-nurse-breaks-down-after-the-violence-at-RG-Kar-H_1723772228250_1723772241509.jpg"

# Send a HTTP request to the URL with headers
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Open a file to write the image data
    with open("marina_beach.jpg", "wb") as file:
        file.write(response.content)
    print("Image downloaded successfully.")
else:
    print(f"Failed to retrieve the image. Status code: {response.status_code}")
    print(f"Response content: {response.text}")
