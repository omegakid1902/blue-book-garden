import os
import frontmatter
from shutil import *
import os

zet_folder = "../zettelkasten/"

rmtree('./docs')
os.mkdir('./docs')

original = "../zettelkasten/Spaces/Projects/Bible Study Kit/Scripture (BPT)/"
target = "./docs/"
move(original, target)

'''
original = "../zettelkasten/Zet"
move(original, target)
'''
for file in os.listdir(zet_folder):
    if file.endswith(".md"):
        with open(os.path.join(zet_folder, file), encoding="utf8") as f:
            content = f.read()
            metadata, content = frontmatter.parse(content)
            if 'publish' in metadata.keys():
                print("Copy publish files from zettelkasten to docs/")
                copy(os.path.join(zet_folder, file), './docs/')
            else:
                pass

for root, dirs, files in os.walk(zet_folder + "Zet/"):
    for file in files:
        if file.endswith(".md"):
            with open(os.path.join(root, file), encoding="utf8") as f:
                content = f.read()
                metadata, content = frontmatter.parse(content)
                if 'publish' in metadata.keys() and metadata['publish'] == True:
                    print("Copy publish files from zettelkasten to docs/")
                    print(os.path.join(root, file))
                    copy(os.path.join(root, file), './docs/')
                else:
                    pass

