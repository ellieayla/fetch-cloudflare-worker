Sometimes people post RSS/iCal feeds on web servers and then get conned into slapping Cloudflare in front. So feed readers get captchas instead of a feed.

But Cloudflare edge workers are privileged. So one can write a tiny proxy to fetch from the original website without a challenge.

Which is a whole lot of shit just to see what's happening in a local community.

## Local development

You can run the Worker defined by your new project by executing `wrangler dev` in this
directory. This will start up an HTTP server and will allow you to iterate on your
Worker without having to restart `wrangler`.
