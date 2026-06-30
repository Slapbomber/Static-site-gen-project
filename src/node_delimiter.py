from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:

    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        old_node_strings = old_node.text.split(delimiter)
        if len(old_node_strings) % 2 == 0:
            raise Exception("invalid markdown, check delimiters")
    
    split_nodes = []
    for i in range(len(old_node_strings)):
        if old_node_strings[i] == "":
            continue
        if i % 2 == 0:
            split_nodes.append(TextNode(old_node_strings[i], TextType.TEXT))
        else:
            split_nodes.append(TextNode(old_node_strings[i], text_type))
    new_nodes.extend(split_nodes)
    
    return new_nodes
    