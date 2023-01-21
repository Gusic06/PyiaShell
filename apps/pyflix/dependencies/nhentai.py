def nhentai(tag: str, username: str, password: str):

    """
    Wrapper for downloading torrents from nhentai.

    param: tag -> parameter for the tag of the post you want to download (463921 is an example of what the tag may look like)
    param: username -> parameter for the name of you account (email would work aswell)
    param: password -> parameter for the password of your account (Case Sensitive (obviously))
    """

    if not isinstance(tag, str):
        raise TypeError(f"Invalid type: Expected {str} but got {type(tag)} instead.")

    if not isinstance(username, str):
        raise TypeError(f"Invalid type: Expected {str} but got {type(username)} instead.")

    if not isinstance(password, str):
        raise TypeError(f"Invalid type: Expected {str} but got {type(password)} instead.")
    
    try:
        import requests
        import os
        import sys

    except ImportError:
        raise ImportError("Do you have all the required modules downloaded?")

    download = requests.get(f"https://nhentai.net/g/{tag}/download", auth=(f"{username}", f"{password}"))
    print(download)
    with open(f"{tag}.torrent", "wb")as file:
        file.write(download)

if __name__ == "__main__":
    nhentai("272863", "gussy", "2LLL08QCU")