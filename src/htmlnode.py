class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("children will update this method to render as html")

    def props_to_html(self):
        prop_string = ""
        if not self.props:
            return prop_string
        for prop_name, prop_value in self.props.items():
            prop_string += f' {prop_name}="{prop_value}"'
        return prop_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
