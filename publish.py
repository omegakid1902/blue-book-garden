import os
import frontmatter
from shutil import copy
import os

if not os.path.exists('./docs'):
    os.mkdir('./docs')

for file in os.listdir("./zettelkasten/"):
    if file.endswith(".md"):
        with open(os.path.join("./zettelkasten/", file), encoding="utf8") as f:
            content = f.read()
            metadata, content = frontmatter.parse(content)
            if 'publish' in metadata.keys():
                print("Copy publish files from zettelkasten to docs/")
                copy(os.path.join("./zettelkasten/", file), './docs/')
            else:
                pass

for root, dirs, files in os.walk("./zettelkasten/Zet/"):
    for file in files:
        if file.endswith(".md"):
            with open(os.path.join(root, file), encoding="utf8") as f:
                content = f.read()
                metadata, content = frontmatter.parse(content)
                if 'publish' in metadata.keys():
                    print("Copy publish files from zettelkasten to docs/")
                    print(os.path.join(root, file))
                    copy(os.path.join(root, file), './docs/')
                else:
                    pass
