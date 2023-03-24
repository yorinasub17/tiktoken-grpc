#------------------------------------------------------------------------------
# Docker image containing the tiktoken-grpc service
#
# This image uses a multi-stage docker build to try to keep the final image as
# small as possible. To do this we rely on the pex utility to package the
# app and its dependencies into a single executable bundle that we then copy over
# to a slim image that doesn't contain all the build tools, and invoke it there.
#------------------------------------------------------------------------------

# Stage 1: build step - compiles the python app down to a single pex executable.
FROM python:3.11.2-buster AS build

RUN python -m pip install --upgrade pip && pip install poetry
RUN mkdir -p /build/build
WORKDIR /build

# Ideally we don't need to copy in the README, but it's necessary to be able to install the package using pex so...
COPY ./README.md ./pyproject.toml ./poetry.lock /build

RUN poetry install --no-root

COPY ./tiktokengrpc /build/tiktokengrpc

RUN poetry run poe build && ls -lah


# Stage 2: copy the pex executable into the slim container
FROM python:3.11.2-slim-bullseye

COPY --from=build /build/build/tiktoken-grpc.pex /app/tiktoken-grpc.pex
EXPOSE 50051
ENTRYPOINT ["python3", "/app/tiktoken-grpc.pex"]
CMD ["--no-tls"]
