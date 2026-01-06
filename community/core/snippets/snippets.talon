# All snippets require "snip" prefix to avoid conflicts with Cursorless scopes and formatters
# Example: "snip if", "snip for", "snip class"
snip {user.snippet}: user.insert_snippet_by_name_with_stop_at_end(snippet)

# Snippets with phrase (e.g., "snip funk myFunction" inserts function named myFunction)
snip {user.snippet_with_phrase} <user.text>:
    user.insert_snippet_by_name_with_phrase_and_stop_at_end(snippet_with_phrase, text)

# Navigate through snippet tab stops ($1, $2, etc.)
snip next: user.move_cursor_to_next_snippet_stop()
