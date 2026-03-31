"""
Preprocessing script for MkDocs build.
Strips GitBook-specific syntax from Markdown files so MkDocs can render them cleanly.

Handles:
  {% content-ref url="foo.md" %}...{% endcontent-ref %}  → [foo.md](foo.md)
  {% hint style="info" %}...{% endhint %}               → > blockquote
  {% ... %} / {% end... %}                               → removed

Run as part of the GitHub Actions build — operates on a copy of the source,
never modifies the original files.
"""

import re
import sys
import os
import shutil


def convert_content_ref(match):
    """Convert {% content-ref url="foo.md" %}...{% endcontent-ref %} to a markdown link."""
    url_match = re.search(r'url="([^"]+)"', match.group(0))
    if url_match:
        url = url_match.group(1)
        label = os.path.basename(url).replace(".md", "").replace("-", " ").title()
        return f"- [{label}]({url})"
    return ""


def convert_hint(match):
    """Convert {% hint style="..." %}...{% endhint %} to a blockquote."""
    inner = match.group(1).strip()
    lines = inner.splitlines()
    return "\n".join(f"> {line}" if line.strip() else ">" for line in lines)


def preprocess(content):
    # {% content-ref url="..." %}\n[inner text]\n{% endcontent-ref %}
    content = re.sub(
        r'\{%\s*content-ref[^%]*%\}.*?\{%\s*endcontent-ref\s*%\}',
        convert_content_ref,
        content,
        flags=re.DOTALL
    )

    # {% hint style="..." %}\n[inner text]\n{% endhint %}
    content = re.sub(
        r'\{%\s*hint[^%]*%\}(.*?)\{%\s*endhint\s*%\}',
        convert_hint,
        content,
        flags=re.DOTALL
    )

    # Remove any remaining {% ... %} tags (tabs, tab, etc.)
    content = re.sub(r'\{%[^%]*%\}', '', content)

    # Clean up excessive blank lines left behind
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content


def process_directory(src_dir, dst_dir):
    for root, dirs, files in os.walk(src_dir):
        # Skip node_modules and hidden dirs
        dirs[:] = [d for d in dirs if d != 'node_modules' and not d.startswith('.')]

        rel = os.path.relpath(root, src_dir)
        dst_root = os.path.join(dst_dir, rel)
        os.makedirs(dst_root, exist_ok=True)

        for fname in files:
            src_path = os.path.join(root, fname)
            dst_path = os.path.join(dst_root, fname)

            if fname.endswith('.md'):
                with open(src_path, 'r', encoding='utf-8', errors='replace') as f:
                    content = f.read()
                content = preprocess(content)
                with open(dst_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            else:
                shutil.copy2(src_path, dst_path)


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "."
    dst = sys.argv[2] if len(sys.argv) > 2 else "_docs_processed"
    print(f"Preprocessing: {src} → {dst}")
    if os.path.exists(dst):
        shutil.rmtree(dst)
    process_directory(src, dst)
    print("Done.")
