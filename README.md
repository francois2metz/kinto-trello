# Kinto for Trello

This project implement an authentifcation policy for [Kinto][] using [Trello][] tokens.

[kinto]: https://www.kinto-storage.org/
[trello]: http://trello.com/

## Install

    pip install kinto-trello

## Usage

Update `kinto.includes` to add kinto_trello

    kinto.includes = kinto_trello

Add to your config file:

    multiauth.policies = trello
    multiauth.policy.trello.use = kinto_trello.authentication.TrelloAuthenticationPolicy
    trello.apikey = 'YOUR_API_KEY' # FROM https://trello.com/app-key

## License

MIT
