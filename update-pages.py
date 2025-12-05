#!/usr/bin/env python3
"""Script to update all pages with new design"""

import re
from pathlib import Path

# Pages to update
pages = ['downloads.html', 'support.html', 'privacy.html', 'privacy-de.html',
         'terms.html', 'terms-de.html', 'impressum.html']

# CSS variables to replace
old_vars = '''--bg-color: #09090b;
            --text-color: #ffffff;
            --accent-color: #3F5E5D;
            --accent-hover: #507674;
            --secondary-text: #a1a1aa;
            --card-bg: rgba(24, 24, 27, 0.6);
            --card-border: rgba(255, 255, 255, 0.08);
            --card-hover-border: rgba(255, 255, 255, 0.15);
            --top-bar-height: 60px;'''

new_vars = '''--bg-color: #ffffff;
            --text-color: #000000;
            --accent-color: #000000;
            --accent-hover: #333333;
            --secondary-text: #666666;
            --card-bg: #f9f9f9;
            --card-border: #e5e5e5;
            --card-hover-border: #d4d4d4;
            --top-bar-height: 70px;'''

# Navigation bar CSS
old_nav = '''background: rgba(9, 9, 11, 0.7);'''
new_nav = '''background: rgba(255, 255, 255, 0.95);'''

old_logo_color = '''color: #fff;'''
new_logo_color = '''color: #000;'''

# Update each file
for page in pages:
    file_path = Path(page)
    if not file_path.exists():
        print(f"Skipping {page} - file not found")
        continue

    content = file_path.read_text()

    # Replace CSS variables
    content = content.replace(old_vars, new_vars)

    # Update navigation background
    content = content.replace('background: rgba(9, 9, 11, 0.7);',
                            'background: rgba(255, 255, 255, 0.95);')

    # Update logo styling
    content = re.sub(r'\.logo \{[^}]*font-weight: 800;[^}]*font-size: 1\.3rem;[^}]*color: #fff;',
                    '.logo {\\n            font-weight: 700;\\n            font-size: 1.5rem;\\n            color: #000;',
                    content)

    # Update nav padding
    content = content.replace('padding: 0 20px;', 'padding: 0 32px;', 1)

    # Update footer
    old_footer = '''<span style="color: #52525b;">&copy; 2025 Chuk</span>'''
    new_footer = '''<span>&copy; 2025 Chuk</span>
            <a href="./privacy.html">Privacy Policy</a>
            <a href="./terms.html">Terms of Service</a>
            <a href="./impressum.html">Impressum</a>'''
    content = content.replace(old_footer, new_footer)

    file_path.write_text(content)
    print(f"Updated {page}")

print("Done!")
