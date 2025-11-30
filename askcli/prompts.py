from typing import List
from .models import PageContent

SYSTEM_PROMPT = """You are a concise technical research assistant.
You must answer using the provided web content when it exists.
If web content is insufficient, say so clearly and mark which parts are assumptions.
Always respond in markdown with the following sections:

## TL;DR (2–4 bullet points)

## Explanation

## Key Points (bulleted)

## Sources (numbered list of URLs with short labels)"""


def build_user_prompt(query: str, pages: List[PageContent]) -> str:
    """Build user prompt with query and web content."""
    parts = [f"User question:\n{query}\n"]
    
    if pages:
        parts.append("Web results:\n")
        for i, page in enumerate(pages, 1):
            parts.append(
                f"[{i}] Title: {page.title}\n"
                f"URL: {page.url}\n"
                f"Content:\n{page.text}\n\n"
            )
        parts.append(
            "Using only the information above (and general knowledge only when absolutely needed), "
            "write a structured answer in markdown with the specified sections."
        )
    else:
        parts.append(
            "No web content provided. Answer using your general knowledge and "
            "write a structured answer in markdown with the specified sections."
        )
    
    return "\n".join(parts)