#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
task_binary=$(mktemp /tmp/elliptic-tail-scan.XXXXXX)
trap 'rm -f -- "$task_binary"' EXIT
g++ -std=c++20 -O3 -Wall -Wextra -Wconversion deep_scan.cpp -o "$task_binary"
for scale in 4 8 16 32; do
  "$task_binary" "$scale" 4194304 data
done
python analyze_tail.py > analysis.log 2>&1
cat analysis.log
