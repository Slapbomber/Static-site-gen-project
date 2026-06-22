from enum import Enum
from textnode import TextType, TextNode

def main():
    dummy_test = TextNode("This is a placeholder", TextType.LINK, "https://google.com")
    print(dummy_test)




main()