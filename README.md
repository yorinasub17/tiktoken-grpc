# tiktoken-grpc

`tiktoken-grpc` is a [gRPC](https://grpc.io) service that wraps the [tiktoken](https://github.com/openai/tiktoken)
Python library offered by OpenAI.

This is most useful as a side car to integrate `tiktoken` into non-Python based projects.


## Quickstart

### Local

> **Prerequisite**
>
> You must have python 3.8+ setup, and [poetry](https://python-poetry.org/).

To run the grpc service locally, first clone this repository:

```
git clone https://github.com/yorinasub17/tiktoken-grpc.git
```

Then, install dependencies using [poetry](https://python-poetry.org/) and start the serve with the `serve` run task:

```
# Omit the --only flag if you also want to contribute code
poetry install --only main

# See --help for all the options
poetry run poe serve --no-tls
```

You should now be able to connect to the server using one of [the supported clients below](#client-libraries), on
`localhost:50051`.

### Docker

```
docker run --rm -p 50051:50051 ghcr.io/yorinasub17/tiktoken-grpc
```


## Client Libraries

- [Go: tiktoken-grpc-go](https://github.com/yorinasub17/tiktoken-grpc-go)


## Acknowledgements

Thanks to the OpenAI team for providing the tiktoken encoding files and the
[tiktoken](https://github.com/openai/tiktoken) library.


## License

This project is licensed under the [3-clause BSD License](/LICENSE).
