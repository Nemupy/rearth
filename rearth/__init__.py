import requests
from bs4 import BeautifulSoup


class Town:
    def __init__(self, town):
        url = "https://rearthserver.net/map/"
        response = requests.get(url, allow_redirects=True)
        redirected_url = response.url
        print(redirected_url)
        endpoint_url = f"{redirected_url}tiles/_markers_/marker_world.json"
        response = requests.get(endpoint_url)

        data = response.json()

        town_data = data["sets"]["towny.markerset"]["areas"][f"{town}__0"]

        desc_html = town_data["desc"]
        desc_soup = BeautifulSoup(desc_html, "html.parser")
        desc_dict = {
            "title": desc_soup.find("span", style="font-size:120%").text,
            "mayor": desc_soup.find("span", style="font-weight:bold").text,
            "associates": [assoc.text for assoc in desc_soup.find_all("span", style="font-weight:bold")[1:]],
            "flags": {
                flag.text.split(":")[0].strip(): flag.text.split(":")[1].strip()
                for flag in desc_soup.find_all("span", style="font-weight:bold")[4:]
            }
        }

        self.markup = town_data["markup"]
        self.x = town_data["x"]
        self.weight = town_data["weight"]
        self.z = town_data["z"]
        self.ybottom = town_data["ybottom"]
        self.label = town_data["label"]
        self.opacity = town_data["opacity"]
        self.fillopacity = town_data["fillopacity"]
        self.title = desc_dict["title"]
        self.mayor = desc_dict["mayor"]
        self.associates = desc_dict["associates"]
        self.flags = desc_dict["flags"]

    def markup(self):
        return self.markup

    def x(self):
        return self.x

    def weight(self):
        return self.weight

    def z(self):
        return self.z

    def ybottom(self):
        return self.ybottom

    def label(self):
        return self.label

    def opacity(self):
        return self.opacity

    def fillopacity(self):
        return self.fillopacity

    def title(self):
        return self.title

    def mayor(self):
        return self.mayor

    def associates(self):
        return self.associates

    def flags(self):
        return self.flags
