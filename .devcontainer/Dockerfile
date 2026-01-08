FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

# System deps (sqlite is already available, but keep build essentials around)
RUN apt-get update && apt-get install -y --no-install-recommends \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspaces/13f-sqlite
