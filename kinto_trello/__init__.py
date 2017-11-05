DEFAULT_SETTINGS = {
    'trello.apikey': None
}

def includeme(config):
    settings = config.get_settings()

    defaults = {k: v for k, v in DEFAULT_SETTINGS.items() if k not in settings}
    config.add_settings(defaults)
