
import json

LANGUAGE_SCHEMA = json.loads("""{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Language",
  "type": "object",
  "required": ["code", "name", "emoji", "translations"],
  "properties": {
    "code": {
      "type": "string",
      "pattern": "^[a-z]{2}(-[A-Z]{2})?$",
      "description": "ISO 639-1 language code (e.g., 'es', 'en', 'pt-BR')"
    },
    "name": {
      "type": "string",
      "description": "Language name in its own language (e.g., 'español', 'English')"
    },
    "emoji": {
      "type": "string",
      "description": "An emoji that visually represents the language (commonly a flag)"
    },
    "translations": {
      "type": "object",
      "description": "Language name translated into other languages",
      "additionalProperties": {
        "type": "string"
      },
      "examples": [
        {
          "en": "Spanish",
          "fr": "Espagnol",
          "de": "Spanisch"
        }
      ]
    }
  }
}
""")