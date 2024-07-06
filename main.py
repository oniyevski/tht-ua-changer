import asyncio
from mitmproxy import options, http
from mitmproxy.tools import dump
from rich.console import Console

launcher_version = "0.0.1"
console = Console(width=100)
console.print(f"[bold dark_orange]THT UA CHANGER v{launcher_version}[/bold dark_orange]", no_wrap=True)
console.print("[bold cyan1](...) Your actions are expected.[/bold cyan1]", no_wrap=True)

class RequestLogger:
    async def request(self, flow: http.HTTPFlow):
        url = flow.request.url
        flow.request.headers["User-Agent"] = "TURK HACK TEAM 57. ALAY KULUBU"
        console.print(f"Client: {url}")

async def start_proxy(host, port):
    opts = options.Options(listen_host=host, listen_port=port)
    master = dump.DumpMaster(
        opts,
        with_termlog=False,
        with_dumper=False,
    )
    master.addons.add(RequestLogger())
    await master.run()
    return master

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

async def create_tasks_func(host, port):
    tasks = []
    tasks.append(asyncio.create_task(start_proxy(host, port)))
    await asyncio.wait(tasks)

def main():
    try:
        loop.run_until_complete(create_tasks_func('192.168.1.34', 1889))
        loop.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()