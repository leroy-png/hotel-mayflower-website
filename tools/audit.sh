#!/bin/bash
# Fact audit — flags forbidden amenity claims in the HTML.
# Every hit must be a NEGATIVE statement (e.g. "does not have an elevator").
# Run from the website root: bash tools/audit.sh
cd "$(dirname "$0")/.." || exit 1
echo "=== Occurrences of sensitive amenity terms (verify each is a negative/honest statement) ==="
grep -rinoE '(breakfast|ontbijt|room service|roomservice|bike rental|fietsverhuur|air.?condition|airco\b|elevator|\blift\b|private parking|eigen parkeer|24.(hour|uur|h).{0,12}(reception|receptie)|swimming pool|zwembad|\bspa\b|\bgym\b|fitness|pet|huisdier|restaurant)' \
  en nl --include="*.html" | grep -viE 'restaurants|huisdieren zijn.*niet|pets are not|no elevator|geen lift|not have an elevator|does not have|geen eigen|no private|not air conditioning|geen airconditioning'
echo ""
echo "=== Raw counts per term ==="
for t in breakfast ontbijt "room service" "bike" "aircondition" "elevator" "lift" "zwembad" "spa" "gym" "pet" "huisdier"; do
  c=$(grep -rioE "$t" en nl --include="*.html" | wc -l | tr -d ' ')
  echo "$t: $c"
done
echo ""
echo "Review the first list above: every line must be an honest/negative statement or a neighbourhood recommendation."
