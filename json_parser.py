import json 
import pandas as pd

my_json = """
[
    {
        "glossary": {
            "title": "example glossary",
            "GlossDiv": {
                "title": "AAA",
                "GlossList": {
                    "GlossEntry": {
                        "ID": "SGML",
                        "SortAs": "SGML",
                        "GlossTerm": "Standard Generalized Markup Language",
                        "Acronym": "SGML",
                        "Abbrev": "ISO 8879:1986",
                        "GlossDef": {
                            "para": "A meta-markup language, used to create markup languages such as DocBook.",
                            "GlossSeeAlso": ["GML", "XML"]
                        },
                        "GlossSee": "markup"
                    }
                }
            }
        }
    },
    {
        "glossary": {
            "title": "example glossary",
            "GlossDiv": {
                "title": "BBB",
                "GlossList": {
                    "GlossEntry": {
                        "ID": "SGML",
                        "SortAs": "SGML",
                        "GlossTerm": "Standard Generalized Markup Language",
                        "Acronym": "SGML",
                        "Abbrev": "ISO 8879:1986",
                        "GlossDef": {
                            "para": "A meta-markup language, used to create markup languages such as DocBook.",
                            "GlossSeeAlso": ["GML", "XML"]
                        },
                        "GlossSee": "markup"
                    }
                }
            }
        }
    },
    {
        "glossary": {
            "title": "example glossary",
            "GlossDiv": {
                "title": "CCC",
                "GlossList": {
                    "GlossEntry": {
                        "ID": "SGML",
                        "SortAs": "SGML",
                        "GlossTerm": "Standard Generalized Markup Language",
                        "Acronym": "SGML",
                        "Abbrev": "ISO 8879:1986",
                        "GlossDef": {
                            "para": "A meta-markup language, used to create markup languages such as DocBook.",
                            "GlossSeeAlso": ["GML", "XML"]
                        },
                        "GlossSee": "markup"
                    }
                }
            }
        }
    }
]
"""

json_data = json.loads(my_json)

data = []

# Flatten the json
for row in json_data:
    # get title
    glossary_title = row["glossary"]["title"]
    glossdiv_title = row["glossary"]["GlossDiv"]["title"]
    gloss_term = row["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]["GlossTerm"]
    row = {
        "glossary-title": glossary_title,
        "glossdiv-title": glossdiv_title,
        "gloss-term": gloss_term
    }
    data.append(row)

df = pd.DataFrame(data)

df.to_csv("output.csv")