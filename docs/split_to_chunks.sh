# inside the repo’s docs/ folder
gcsplit -f tmp_ -b "%02d.md" sonar_schema.graphql '/^type/' '{*}' && \
for f in tmp_*.md; do
  { printf '```graphql\n'; cat "$f"; printf '\n```\n'; } > "${f#tmp_}"
done && rm tmp_*.md