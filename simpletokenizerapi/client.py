import simpletokenizer

# /tokenize/
def handle_tokenize(input):
    return {"tokens": simpletokenizer.tokenize(input)}

# /count-tokens/
def handle_count_tokens(input):
    return {"count": simpletokenizer.count_tokens(input)}

# /get-unique-words/
def handle_get_unique_words(input):
    return {"unique-words": simpletokenizer.get_unique_words(input)}

