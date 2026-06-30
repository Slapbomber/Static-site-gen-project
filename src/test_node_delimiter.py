import unittest
from textnode import TextNode, TextType
from node_delimiter import split_nodes_delimiter

class TestNodeDelimiter(unittest.TestCase):
    def test_notTextTypeTextandBold(self):
        new_nodes = split_nodes_delimiter([TextNode("**This is bold text**", TextType.BOLD), TextNode("This is **bold** text", TextType.TEXT)], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("**This is bold text**", TextType.BOLD), TextNode("This is ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" text", TextType.TEXT)])
    
    def test_CodeAndSplitEdgecase(self):
        new_nodes = split_nodes_delimiter([TextNode("`Code` is written here", TextType.TEXT)], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("Code", TextType.CODE), TextNode(" is written here", TextType.TEXT)])
    
    def test_TextTypeItalic(self):
        new_nodes = split_nodes_delimiter([TextNode("This is _italic_ text", TextType.TEXT)], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("This is ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" text", TextType.TEXT)])