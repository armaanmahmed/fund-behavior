#!/bin/bash
# Unzip zipped data into directories. Run this from the repository root.

set -e

cd data/raw

for z in *.zip; do
  filename="${z%.zip}"
  base="${filename%_form13f}"
  mkdir -p "${base}"
  unzip -o "${z}" -d "${base}"
done

cd ../..