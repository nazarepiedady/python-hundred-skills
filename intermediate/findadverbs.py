import re

sentence = 'Clearly, he felt she was inexcusably wrong'

for word_match in re.finditer(r'\w+ly', sentence):
    print('%d-%d: %s' % (
            word_match.start(), word_match.end(), word_match.group(0)
        )
    )
