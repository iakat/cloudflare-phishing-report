# cloudflare-phishing-report

CloudFlare Phishing Report API I use in combination with n8n

I use it mainly to report Steam phishing websites.

You might have to contact them to get your IP whitelisted.

## Running

1, Set the environment variables required in `api.py` in an `.env` file
2. `docker run --env-file=.env -p 80:80 chauffer/cloudflare-phishing-report`
