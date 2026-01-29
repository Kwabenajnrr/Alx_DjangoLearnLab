## HTTPS and Security Configuration

This Django application is configured to enforce secure HTTPS connections
and follow best practices for web security.

### HTTPS Enforcement
- `SECURE_SSL_REDIRECT = True` forces all HTTP traffic to be redirected to HTTPS.
- HTTP Strict Transport Security (HSTS) is enabled using:
  - `SECURE_HSTS_SECONDS = 31536000` (1 year)
  - `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
  - `SECURE_HSTS_PRELOAD = True`
  This ensures browsers always access the site using HTTPS.

### Secure Cookies
- `SESSION_COOKIE_SECURE = True` ensures session cookies are sent only over HTTPS.
- `CSRF_COOKIE_SECURE = True` ensures CSRF cookies are sent only over HTTPS.

### Security Headers
- `X_FRAME_OPTIONS = "DENY"` protects against clickjacking attacks.
- `SECURE_CONTENT_TYPE_NOSNIFF = True` prevents MIME-type sniffing.
- `SECURE_BROWSER_XSS_FILTER = True` enables browser-level XSS protection.

### Deployment Notes
For production deployment, HTTPS must be configured at the web server level
using SSL/TLS certificates (e.g., via Nginx or Apache). Django is configured
to trust HTTPS headers from reverse proxies using:

