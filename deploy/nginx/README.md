# Nginx metadata integration

The production site runs Streamlit behind Nginx. Install the snippets from the
checked-out app directory (`/opt/streamlit_app` in the current deployment):

```nginx
# /etc/nginx/nginx.conf, inside http { ... }
include /opt/streamlit_app/deploy/nginx/http-metadata-map.conf;

# Canonical HTTPS server { ... }
include /opt/streamlit_app/deploy/nginx/public-files.conf;

location / {
    # Existing proxy and websocket directives stay here.
    include /opt/streamlit_app/deploy/nginx/streamlit-location-metadata.conf;
    proxy_pass http://127.0.0.1:8501;
}
```

Remove the old `sub_filter '<head>' ...` rule that inserts the “Beat the market”
description. The new location snippet also removes it defensively during the
transition.

Validate and reload:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

Then check the raw response (social crawlers do not wait for Streamlit's
JavaScript):

```bash
curl -s https://www.prettymodels.ai/ | grep -o 'og:[^>]*'
curl -I https://www.prettymodels.ai/app/static/social-preview.png
curl -I https://www.prettymodels.ai/robots.txt
```
