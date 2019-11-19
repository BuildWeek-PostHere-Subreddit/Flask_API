def jsonConversion(json_obj):
    """Return: string combination of title and text."""
    title = json_obj["title"]
    text = json_obj["text"]

    return " ".join([title, text])
