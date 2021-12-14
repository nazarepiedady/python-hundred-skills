import re

items_list = [
    'techotd(.com)', 'theverge(.com)',
    'edx(.org)', 'github(.com)', 'stackoverflow(.com)'
]

for item in items_list:
    print(re.sub(r' ?\([^)]+\)', '', item))
