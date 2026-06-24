import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("node", "Tis a node", [], {"href": "https://www.google.com", "target": "_blank"})
        node_return = node.props_to_html()
        expected_return = f' href="https://www.google.com" target="_blank"'
        self.assertEqual(node_return, expected_return)
    
    def test_emptyprops(self):
        node = HTMLNode("node", "it a node")
        node_return = node.props_to_html()
        expected_return = ""
        self.assertEqual(node_return, expected_return)

    def test_defaultValues(self):
        node = HTMLNode()
        node2 = HTMLNode(None, None, None, None)
        self.assertEqual(repr(node), repr(node2))

    def test_nodeAttributes(self):
        node = HTMLNode(tag="node", value="I am a node")
        self.assertEqual(node.tag, "node")
        self.assertEqual(node.value, "I am a node")