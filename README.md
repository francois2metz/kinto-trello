# Kinto for Trello

This project implement an authentication policy for [Kinto][] using [Trello][] tokens.

[kinto]: https://www.kinto-storage.org/
[trello]: http://trello.com/

## Install

    pip install kinto-trello

## Configuration

Update `kinto.includes` to add kinto_trello

    kinto.includes = kinto_trello

Add to your config file:

    multiauth.policies = trello
    multiauth.policy.trello.use = kinto_trello.authentication.TrelloAuthenticationPolicy
    trello.apikey = 'YOUR_API_KEY' # FROM https://trello.com/app-key

## Usage

In the `Authorization` header, set the trello token:


    Authorization: Trello <token>

## License

MIT
