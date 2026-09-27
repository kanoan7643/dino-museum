"""Wrap dino-museum.html (artifact source, no <html>/<head>) into a standalone index.html for GitHub Pages."""
s = open('dino-museum.html', encoding='utf-8').read()
s = s.replace('<meta charset="utf-8">\n', '', 1)
head, sep, rest = s.partition('</style>\n')
doc = ('<!doctype html>\n<html lang="zh-Hant">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       + head + sep + '</head>\n<body>\n' + rest.rstrip() + '\n</body>\n</html>\n')
doc = doc.replace('body{background:var(--bg);', 'body{margin:0;background:var(--bg);', 1)
open('index.html', 'w', encoding='utf-8').write(doc)
print('index.html written', len(doc))
