#!/usr/bin/env bash 
set -e

python manage.py migrate --noinput

repo=$GITHUB_REPO
token=$GITHUB_TOKEN

curl -X POST \

     -H "Accept: application/vnd.github.v3+json" \
     -H "Authorization: Bearer $token" \

     https://api.github.com/repos/$repo/dispatches \

     -d '{"event_type":"production-release"}'

echo "Done."
