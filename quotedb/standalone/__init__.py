import os
import envdir

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotedb.standalone.settings")

CONFIG_DIR = os.path.expanduser("~/.config/quotedb")

if os.path.exists(CONFIG_DIR):
    envdir.open(CONFIG_DIR)
