from workers import Response, Request, WorkerEntrypoint, fetch
from urllib.parse import ParseResult, urlparse, urlunparse


class Default(WorkerEntrypoint):
    async def fetch(self, request: Request):
        request_url: ParseResult = urlparse(request.url)

        request_url_component: ParseResult = urlparse(f"https:/{request_url.path}")

        if request_url_component.hostname not in (
            "www.cycleto.ca",
            "www.everyonerides.org",
        ):
            unsupported = f"unsupported domain {request_url_component.hostname}"
            return Response(
                body=unsupported,
                status_text=unsupported,
                status=403,
            )

        upstream_url_components: ParseResult = ParseResult(
            scheme="https",
            netloc=request_url_component.netloc,
            path=request_url_component.path,
            params=request_url.params,
            query=request_url.query,
            fragment="",
        )
        upstream_url = urlunparse(upstream_url_components)
        return await fetch(upstream_url)
