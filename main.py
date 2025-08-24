import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()["value"]
        return joke
    else:
        return "Sorry, couldn't fetch a joke right now."

# Example usage:
print(get_chuck_norris_joke())

