import os
import frontmatter
from shutil import copy

os.mkdir('./publish')

for root, dirs, files in os.walk("./Zet/"):
    for file in files:
        if file.endswith(".md"):
            with open(os.path.join(root, file), encoding="utf8") as f:
                content = f.read()
                metadata, content = frontmatter.parse(content)
                if 'publish' in metadata.keys():
                    print(metadata['title'])
                    copy(os.path.join(root, file), './publish/')
                else:
                    pass
