import random

class StoryTemplate:

    def __init__(self, name, pattern):
        self._name = name
        self._pattern = pattern

    @property
    def name(self):
        return self._name
    
    @property
    def pattern(self):
        return self._pattern
    
    def generate(self, words):
        sentence = []

        for token in self._pattern:

            if token.startswith("{") and token.endswith("}"):
                pos = token[1:-1]

                matching_words = words.filter_by_pos(pos)

                if len(matching_words) == 0:
                    replace = f"<missing-{pos}>"
                else:
                    replace = str (random.choice(list(matching_words)))
                sentence.append(replace)
            else:
                sentence.append(token)
        
        result = " ".join(sentence)

        result = result.capitalize()

        if not result.endswith("."):
            result += "."

        return result

# Using provided examples
TEMPLATES = [
    StoryTemplate(
        "Adventure",
        [
            "The", "{adj}", "{n}", "{v}", "{adv}", 
            "{prep}", "the", "{adj}", "{n}"
        ]
    ),

    StoryTemplate(
        "Mystery",
        [
            "A", "{adj}", "{n}", "{adv}", "{v}", 
            "while", "the", "{n}", "{v}",
            "{prep}", "the", "{n}"
        ]
    ),

    StoryTemplate(
        "Simple",
        [
            "The", "{adj}", "{n}", "{v}", "{adv}"
        ]
    ),
]