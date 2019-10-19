from Object_Detection import findObjectLabels
from ScrapeGoogleImage import findImageUrls
from SpeechRecognition import speechToText
from ParseText import sample_analyze_syntax

# textFromSpeech = speechToText()
def sendUrlDictThroughString(s):
    noun_list = sample_analyze_syntax(s)
    dict = {}
    for noun in noun_list:
        urls = findImageUrls(noun, 1)
        for index, url in enumerate(urls):
            labels = findObjectLabels(url)
            if len(labels) != 0 and labels[0].lower() == noun.lower():
                dict[noun] = url
                break
            elif index == len(urls) - 1:
                dict[noun] = url
    return dict

# ##logic: find the image that resembles the noun the most,
# #if not -> Find the last image, or just not even store it!
# print(sendUrlDictThroughString("dog"))
