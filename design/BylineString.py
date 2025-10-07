"""
New York Times Interview Question

Write a function that, given an object representing by-line data, returns a valid byline HTML string.

Requirements
    - The function must accept a valid object format.
    - The function must remove invalid objects.
    - The function must output a valid byline HTML string.
    - A byline string must start with a "By".
    - Authors must be separated by a comma "," if there are more than 2.
    - The last Author must be separated by an "and".
    - The Author must be wrapped by the style specified in the "block" parameter.
    - Assume the we support the `<em>` and `<strong>` html tags.

The example input below should return:
   "By <strong>Jonah Engel Bromwich</strong>, <em>Matthew Schneier</em> and Niraj Chokshi"
"""

from typing import Dict, List, Optional


class BylineString:
    HTML_MAPPER = {
        'Bold': ('<strong>', '</strong>'),
        'Italics': ('<em>', '</em>'),
        None: ('', '')
    }

    VALID_KEYS = {"firstName", "middleName", "lastName", "block"}

    def __init__(self, bylines: Dict[str, List]):
        self.bylines = bylines
        self.authors = self._clean_authors()

    def _is_valid_author(self, author: dict) -> bool:
        """Check if the author has all required keys and at least a first and last name."""
        if not isinstance(author, dict):
            return False
        keys_present = self.VALID_KEYS.issubset(author.keys())
        has_name = author.get("firstName") and author.get("lastName")
        return keys_present and has_name

    def _clean_authors(self) -> List[dict]:
        """Remove invalid author entries."""
        return [a for a in self.bylines.get("authors", []) if self._is_valid_author(a)]

    def _format_name(self, author: dict) -> str:
        """Create a full name with proper capitalization."""
        first = author.get("firstName", "").title()
        middle = author.get("middleName", "").title()
        last = author.get("lastName", "").title()
        full_name = " ".join(part for part in [first, middle, last] if part)
        return full_name

    def _wrap_with_html(self, name: str, block_type: Optional[str]) -> str:
        """Wrap the name in HTML tags based on block type."""
        start_tag, end_tag = self.HTML_MAPPER.get(block_type, ("", ""))
        return f"{start_tag}{name}{end_tag}"

    def _format_authors(self) -> List[str]:
        """Format all valid authors with their HTML tags."""
        formatted = []
        for author in self.authors:
            name = self._format_name(author)
            block_type = author.get("block", {}).get("__typename")
            formatted.append(self._wrap_with_html(name, block_type))
        return formatted

    def create(self) -> str:
        """Create the final byline string."""
        if not self.authors:
            return ""

        formatted_authors = self._format_authors()
        num_authors = len(formatted_authors)

        if num_authors == 1:
            return f"By {formatted_authors[0]}"
        elif num_authors == 2:
            return f"By {formatted_authors[0]} and {formatted_authors[1]}"
        else:
            return "By " + ", ".join(formatted_authors[:-1]) + " and " + formatted_authors[-1]


if __name__ == "__main__":
    example_bylines = {
        'authors': [
            {
                'firstName': 'jonah',
                'middleName': 'Engel',
                'lastName': 'bromwich',
                'block': {
                    '__typename': 'Bold'
                }
            },
            { 'random': 'node' },
            {},
            {
                'firstName': 'matthew',
                'middleName': '',
                'lastName': 'sChneier',
                'block': {
                    '__typename': 'Italics'
                }
            },
            {
                'firstName': 'Niraj',
                'middleName': '',
                'lastName': 'chokshi',
                'block': {}
            }
        ]
    }

    expected = "By <strong>Jonah Engel Bromwich</strong>, <em>Matthew Schneier</em> and Niraj Chokshi"
    byline = BylineString(example_bylines)
    result = byline.create()
    assert result == expected
