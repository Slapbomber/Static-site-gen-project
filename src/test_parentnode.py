import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_emptychildren(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")
    
    def test_to_html_with_emptychildrenandprops(self):
        parent_node = ParentNode("div", [], {"href": "https://www.google.com"})
        self.assertEqual(parent_node.to_html(), '<div href="https://www.google.com"></div>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_proppedchildren(self):
        child_node = LeafNode("b", "child", {"href": "https://www.google.com"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><b href="https://www.google.com">child</b></div>')

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_grandgrandchildren(self):
        grandgrandchild_node = LeafNode("b", "grandgrandchild")
        grandchild_node = ParentNode("spam", [grandgrandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><spam><b>grandgrandchild</b></spam></span></div>",
        )
    
    def test_to_html_with_multiplechildren(self):
        child_node = LeafNode("a", "child")
        child_node2 = LeafNode("b", "child2")
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><a>child</a><b>child2</b></div>")