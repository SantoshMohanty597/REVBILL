"Test Billboard"

from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/"+date

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}

response = requests.get(url=URL, headers=header)

soup = BeautifulSoup(response.text, "html.parser")
container = soup.select(".o-chart-results-list-row-container")

songs_list = [item.find(name="h3", id="title-of-a-story").getText().strip() for item in container]
artists_list = [item.find(name="h3", id="title-of-a-story").parent.span.getText().strip() for item in container]


print(songs_list)
print(artists_list)

# 1 one way of joining
Song_Artist=[" : ".join([songs_list[k],artists_list[k]]) for k in range(len(songs_list))]
print(Song_Artist)

# 2 one way of joining - Combine them using zip and join
# combined = [":".join(pair) for pair in zip(songs_list, artists_list)]

'''html format'''

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Billboard 100</title>
    <style>
    body {{ font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; }}
    h1 {{ text-align: center; color: #333; }}
    ul {{ max-width: 600px; margin: auto; padding: 0; list-style-type: decimal; }}
    li {{ background: white; margin: 8px 0; padding: 10px; border-radius: 5px; box-shadow: 0 0 5px #ccc; }}
    </style>
</head>
<body>
    <h1> Billboard 100 On Year :- {date_value}</h1>
    <ul>
        {song_list}
    </ul>
</body>
</html>
"""

# Final HTML
final_html = html_template.format(song_list=Song_Artist,date_value=date)

# Write to an HTML file
with open("Billboard_100.html", mode="w", encoding="utf-8") as file:
    file.write(final_html)

print("HTML file created: Billboard_100.html")





































































