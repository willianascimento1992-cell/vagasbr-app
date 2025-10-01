buildozer_content = '''
[app]
title = Vagas BR
package.name = vagasbr
package.domain = com.vagasbr.app

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0
requirements = python3,kivy==2.1.0,kivymd

[buildozer]
log_level = 2

[android]
api = 30
minapi = 21

[android:permissions]
INTERNET

[android:entry_point]
main.py
'''

print("📋 ARQUIVO 1: buildozer.spec")
print("🎯 COMO CRIAR NO GITHUB:")
print("1. No seu repositório, clique 'Add file' → 'Create new file'")
print("2. Nome do arquivo: buildozer.spec")
print("3. Cole o conteúdo acima")
print("4. Commit: 'Adicionando configuração Android'")
print("5. Clique 'Commit new file'")
