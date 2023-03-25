<h1 align="center">tiktoken-grpc</h1>

<p align="center">
  <a href="https://github.com/yorinasub17/tiktoken-grpc/blob/main/LICENSE">
    <img alt="LICENSE" src="https://img.shields.io/github/license/yorinasub17/tiktoken-grpc?style=for-the-badge">
  </a>
  <a href="https://github.com/yorinasub17/tiktoken-grpc/actions/workflows/lint-test-publish.yml?query=branch%3Amain">
    <img alt="main branch CI" src="https://img.shields.io/github/actions/workflow/status/yorinasub17/tiktoken-grpc/lint-test-publish.yml?branch=main&logo=github&label=CI&style=for-the-badge">
  </a>
  <a href="https://app.circleci.com/pipelines/github/yorinasub17/tiktoken-grpc?branch=main">
    <img alt="main branch CircleCI" src="https://img.shields.io/circleci/build/github/yorinasub17/tiktoken-grpc/main?style=for-the-badge">
  </a>
  <a href="https://github.com/yorinasub17/tiktoken-grpc/releases/latest">
    <img alt="latest release" src="https://img.shields.io/github/v/release/yorinasub17/tiktoken-grpc?style=for-the-badge">
  </a>
</p>


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
docker run --rm -p 50051:50051 yorinasub17/tiktoken-grpc:main
```

(Alternatively, you can use the image from ghcr - `ghcr.io/yorinasub17/tiktoken-grpc:main`)


## Client Libraries

- [Go: tiktoken-grpc-go](https://github.com/yorinasub17/tiktoken-grpc-go)


## Acknowledgements

Thanks to the OpenAI team for providing the tiktoken encoding files and the
[tiktoken](https://github.com/openai/tiktoken) library.
