# settings.py
BOT_NAME = 'lowes_scraper'

SPIDER_MODULES = ['lowes_scraper.spiders']
NEWSPIDER_MODULE = 'lowes_scraper.spiders'

# User-Agent to simulate a real browser
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'

# Enable cookies
COOKIES_ENABLED = True

# Delay between requests
DOWNLOAD_DELAY = 1  # 1 second

# Other settings...
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.lowes.com",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Connection": "keep-alive",
}
DOWNLOADER_MIDDLEWARES = {
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

PROXY = 'http://198.50.244.72:8080'  # Sample public proxy


