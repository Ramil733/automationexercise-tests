import sys
import os

# Добавляем корень проекта в sys.path, чтобы import fixtures.pages работал
sys.path.insert(0, os.path.dirname(__file__))

pytest_plugins = [
    "fixtures.pages",
    "fixtures.users"
]