# Python Security Learning Tools

Six early scripts for authorized reconnaissance and web-security practice.

| Script | Purpose | Status |
|---|---|---|
| `scanner.py` | Recursive crawler, form submission, and reflected-XSS checks | Learning prototype |
| `vulnrability_scanner.py` | Runner for `Scanner` | Requires an authorized target |
| `subdomain_enumeration.py` | Wordlist-based HTTPS subdomain checks | Hard-coded example target/path |
| `scrawler.py` | Wordlist-based page discovery | Hard-coded lab address/path |
| `web_crawler_subdomainenumeration_pagesFinder.py` | Page finder for a PortSwigger lab host | Contains indentation/path issues |
| `post.py` | Form discovery and POST experiment | Incomplete; references an undefined `value` |

## Dependencies

```bash
python -m pip install requests beautifulsoup4
```

## Important limitations

These scripts are preserved as learning artifacts, not production scanners. Several use hard-coded targets or local wordlist paths and some contain known bugs. Review and parameterize them before use.

## Authorized use only

Run against PortSwigger Academy, your own lab, or a target for which you have explicit written permission.

