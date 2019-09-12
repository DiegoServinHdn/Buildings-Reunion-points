import re


def search_elements(rule, text):
    compiled_rule = re.compile(rule)
    matches = compiled_rule.findall(text)
    return matches
