#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
task_binary=$(mktemp /tmp/elliptic-research-scan.XXXXXX)
trap 'rm -f -- "$task_binary"' EXIT
g++ -std=c++20 -O3 -Wall -Wextra -Wconversion scan.cpp -o "$task_binary"
for scale in 4 8 16 24 32; do
  "$task_binary" "$scale" data
done
python analyze.py > analysis.log 2>&1
cat analysis.log
