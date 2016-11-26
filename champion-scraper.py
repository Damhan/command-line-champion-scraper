import bs4 as bs
import urllib.request
import re
from decimal import Decimal


winrates = []
items = []

championPick = input("What winrate would you like to check?: ")

winrate_sauce = urllib.request.urlopen("http://www.leagueofgraphs.com/champions/stats/" + championPick.replace(" ", "").lower()).read()
winrate_soup = bs.BeautifulSoup(winrate_sauce, "lxml")

item_sauce = urllib.request.urlopen("http://www.probuilds.net/champions/details/" + championPick.replace(" ","").lower()).read()
item_soup = bs.BeautifulSoup(item_sauce, "lxml")

body = winrate_soup.body

for div in body.find_all("div",class_="progress-bar-container show-for-large-up-custom"):
   winrate = re.findall(r"[4-5]\d.\d",div.text)
   if winrate:
      winrates.append(winrate[0])

for div in item_soup.find_all("div",class_="item-name gold"):
   items.append(div.text)

if items[7] == "Flash":
   boots = items[6]
   summoners = items[7:]
else:
   boots = items[6:8]
   summoners = items[8:]


def average_winrate_all_roles(winrates):
   total = 0
   avg = 0
   for val in winrates:
      total += float(val)
   avg = total / len(winrates)
   avg = round(avg,2)
   return avg


def main():
   print("\nTheir average winrate across roles better than 40% is: " + str(average_winrate_all_roles(winrates)))
   print("Their best winrate in any role is: " + max(winrates))
   print("\nCommonly built items include: ")
   for i in range(6):
      print(items[i])
   print("\nThe best boots are: ")
   if isinstance(boots, str):
      print(boots)
   else:
      for i in range(len(boots)):
         print(boots[i])
   print("\nSummoners usually taken are: ")
   for i in range(3):
      print(summoners[i])

if __name__ == "__main__":
   main()
