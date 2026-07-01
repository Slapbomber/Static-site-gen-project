from textnode import TextNode, TextType
from extract_links import extract_markdown_images, extract_markdown_links



def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        image_infos = extract_markdown_images(old_node.text)
        if not image_infos:
            new_nodes.append(old_node)
            continue
        for image_info in image_infos:
            (image_alt, image_link) = image_info
            sections = remaining_text.split(f"![{image_alt}]({image_link})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            remaining_text = sections[1]
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        link_infos = extract_markdown_links(old_node.text)
        if not link_infos:
            new_nodes.append(old_node)
            continue
        for link_info in link_infos:
            (link_anchor, link_url) = link_info
            sections = remaining_text.split(f"[{link_anchor}]({link_url})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link_anchor, TextType.LINK, link_url))
            remaining_text = sections[1]
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes
    