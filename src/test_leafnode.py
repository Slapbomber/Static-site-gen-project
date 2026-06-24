import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_props(self):
        node = LeafNode("p", "We noding", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<p href="https://www.google.com">We noding</p>')
    
    def test_leaf_to_html_notag(self):
        node = LeafNode(None, "Hi there")
        self.assertEqual(node.to_html(), "Hi there")
    
    def test_nodeAttributes(self):
        node = LeafNode(tag="node", value="I am a node")
        self.assertEqual(node.tag, "node")
        self.assertEqual(node.value, "I am a node")