import sys
from bs4 import BeautifulSoup
import requests
import re
import urllib.request
import os
from pydub import AudioSegment
from urllib.request import urlopen
import tempfile

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
update_url = input("Enter Newspost URL: ")
# update_url = "https://secure.runescape.com/m=news/gielinor-gazette---february-2022?oldschool=1"
response = requests.get(update_url, headers=headers)
sp = BeautifulSoup(response.text, "html.parser")
up = sp.find("h2", class_="news-article-header__title")
up_name = up.text


def convert_audio_to_ogg(file_url, name):
    data = urlopen(file_url).read()
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(data)
    match file_url.split(".")[-1:][0]:
        case "wav":
            AudioSegment.from_wav(f.name).export(name, format="ogg")
        case "mp3":
            AudioSegment.from_mp3(f.name).export(name, format="ogg")
        case "flv":
            AudioSegment.from_flv(f.name).export(name, format="ogg")
    f.close()


def get_image_count():
    l = []
    img_tags = sp.find_all(["img", "source"])
    img_tags_n = sp.find_all(id="osrsSummaryImage")
    f = str(img_tags_n)
    urls = [img["src"] for img in img_tags]
    first_image = str(f).split("\n")[1].split('src="')[1].split('"')[0]
    l.append(first_image)
    for url in urls:
        if re.search("newspost", url):
            l.append(url)
        elif re.search("thumbnail/Button", url):
            l.append(url)
    # print(list(dict.fromkeys(l)))
    return len(l), len(set(l)), list(dict.fromkeys(l))


def make_valid_filename():
    new_name = str(get_update_name()).replace("/", "-")
    return new_name


def get_update_name():
    header_tag = sp.find("h2", class_="news-article-header__title")
    replaced_name = str(header_tag.text).replace(":", "-")

    return replaced_name


def download_images():
    with_duplicates, without_duplicates, files = get_image_count()
    no_dupes = []
    [no_dupes.append(x) for x in files if x not in no_dupes]
    file_and_folder_name = make_valid_filename()
    print(f"{with_duplicates} files found on update '{up_name}' with {with_duplicates - without_duplicates} duplicates")
    print(f"Files will be renamed to {make_valid_filename()}")
    if not os.path.exists(f"./{file_and_folder_name}"):
        os.mkdir(f"./{file_and_folder_name}")
        print(f"Update Directory not found - Creating it")
    os.chdir(f"./{file_and_folder_name}")
    print("------------Downloading & Renaming Files-------------")
    image_counter = 0
    for url in no_dupes:
        if str(url).endswith(" "):
            url = str(url[:-1])
        url2 = str(url).replace(" ", "%20")
        file_ending = url.split(".")[-1:]
        file_name1 = url.split("/")[-1:]
        # print("file_name1: ", file_name1)
        file_name = file_name1[0].split(".")


        if image_counter == 0:
            new_name = f"{make_valid_filename()} newspost.{str(file_ending[0]).lower()}"
            urllib.request.urlretrieve(url2, new_name)
            print(f"{url.split('/')[-1:]} → {new_name}")
            image_counter += 1
        else:
            new_name = f"{make_valid_filename()} ({image_counter}).{str(file_ending[0]).lower()}"
            if str(file_ending[0]).lower() == "wav" or str(file_ending[0]).lower() == "mp3" or str(file_ending[0]).lower() == "flv":
                print(f"Found Audio File '{url.split('/')[-1:][0]}' - converting to .ogg")
                convert_audio_to_ogg(url2, f"{make_valid_filename()} ({image_counter}).ogg")
                print(f"{url.split('/')[-1:]} → {make_valid_filename()} ({image_counter}).ogg")
                image_counter += 1
            else:
                urllib.request.urlretrieve(url2, new_name)
                print(f"{url.split('/')[-1:]} → {new_name}")
                image_counter += 1

    input("------------------------Done-------------------------")

try:
    download_images()
except:
    input(f"***** {sys.exc_info()[1]} - DM Brok#0001 *****")
