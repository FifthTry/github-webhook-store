# GitHub Webhook using Flask
(In Development)

# References

[Webhooks](https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/about-webhooks)

## Setup

    - Run listener.py
    ```
    python listener.py
    ```
    - The output from ngork would be running on [http://127.0.0.1:5000/](http://127.0.0.1:5000/ )
    - Run ngork on port 5000
    ```
    ngork.exe http 5000
    ```
    - Adding webhook to Github
        - Go to `settings` -> `Webhooks` -> Click `Add webhook`
        - Paste the ngork url as the <strong>Payoad URL</strong> and choose `application/json` as content type. 
        - Let the trigger be `send me everything`
        - Add webhook
    - Doing any activity in Github would generate a `data.json`
