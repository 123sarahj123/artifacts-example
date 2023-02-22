#!/bin/bash

set -eu

echo "Very important file 2" > important_file.txt

buildkite-agent meta-data set "foo2" < important_file.txt
