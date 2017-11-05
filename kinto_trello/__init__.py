from kinto.core import load_default_settings

DEFAULT_SETTINGS = {
    'trello.apikey': None
}

def includeme(config):
    load_default_settings(config, DEFAULT_SETTINGS)
