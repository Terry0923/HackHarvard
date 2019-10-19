import os
from google.cloud import language_v1
from google.cloud.language_v1 import enums as parse_enums

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="My First Project-854b30065e6e.json"

def sample_analyze_syntax(text_content):
    """
    Analyzing Syntax in a String

    Args:
      text_content The text content to analyze
    """
    noun_arr = []
    client = language_v1.LanguageServiceClient()
    type_ = parse_enums.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = parse_enums.EncodingType.UTF8

    response = client.analyze_syntax(document, encoding_type=encoding_type)
    for token in response.tokens:
        text = token.text
        part_of_speech = token.part_of_speech
        if parse_enums.PartOfSpeech.Tag(part_of_speech.tag).name == "NOUN":
            noun_arr.append(token.text.content)
    return noun_arr
