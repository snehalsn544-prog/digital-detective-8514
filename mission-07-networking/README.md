# Mission 7 — Networking

**Goal:** explain how computers communicate and understand the basic jobs of IP addresses, DNS, routers, switches and web protocols.

## 1. What is a computer network?

A computer network is a group of connected devices that exchange data and share resources. Connections may use cables, Wi-Fi, or other communication links.

- **LAN (Local Area Network):** covers a limited area such as a home, school or office.
- **WAN (Wide Area Network):** connects networks across large geographic areas. The Internet is a global network of networks.

## 2. Important network terms

- **IP address:** a numerical address used to identify an interface on an IP network and route packets. IPv4 examples use four numbers; IPv6 uses hexadecimal groups.
- **Domain name:** a human-readable name such as `example.com`.
- **DNS (Domain Name System):** looks up records that associate domain names with information such as IP addresses.
- **Router:** forwards packets between different networks.
- **Switch:** connects devices within a local network and forwards Ethernet frames within that network.
- **Packet:** a formatted unit of data carried across a network.

An IP address may be private (used inside a local network) or public (routable on the public Internet). Do not publish your own network details in this assignment.

## 3. What happens when you open a website?

At a simplified level:

1. You enter a domain name in the browser.
2. The device obtains the needed DNS information, often using a cached answer or a DNS resolver.
3. The device establishes a connection to the server. Modern web connections commonly use TCP or QUIC, depending on the protocol.
4. With HTTPS, TLS helps authenticate the server and encrypt the connection.
5. The browser sends an HTTP request.
6. The server returns an HTTP response, often containing HTML, CSS, JavaScript or data.
7. The browser processes the response and displays the page.

This is a simplified overview; real connections can involve caches, proxies, content-delivery networks and multiple requests.

## 4. HTTP and HTTPS

- **HTTP** is the application protocol used for web requests and responses.
- **HTTPS** is HTTP protected by TLS. It helps provide encryption, integrity and server authentication.
- The padlock/security indicator in a browser indicates a protected connection, not that every claim or download on the site is trustworthy.

## 5. Safe, read-only practice on macOS

These commands inspect your own device or contact a public example domain:

```bash
ping -c 4 example.com
```

This sends a small number of test packets and reports whether replies arrive. Some networks block ping, so no reply does not automatically mean the website is down.

```bash
nslookup example.com
```

This asks DNS for information about the example domain. The returned addresses can change over time.

Optional:

```bash
traceroute example.com
```

This attempts to show network hops toward the destination. Some hops may not respond. Do not scan networks or devices you do not own or have permission to test.

## 6. Quick comparison

| Component | Main job |
|---|---|
| DNS | Finds records for a domain name |
| Router | Moves packets between networks |
| Switch | Connects devices on a local network |
| IP | Provides addressing for network communication |
| HTTP | Defines web request/response messages |
| TLS | Protects a connection with encryption and authentication |

## 7. Questions

1. What is one difference between a LAN and a WAN?
2. Why are domain names useful?
3. What does DNS do?
4. How is a router different from a switch?
5. What extra protection does HTTPS provide compared with plain HTTP?
6. Why might `ping` fail even when a website can be opened?

**Suggested answers:** A LAN covers a smaller local area while a WAN connects networks over larger distances. Domain names are easier for people to remember. DNS resolves names to records such as IP addresses. Routers connect networks; switches connect devices within a LAN. HTTPS protects HTTP using TLS. Ping may be filtered or blocked even when web traffic is allowed.

## Experiment results (assistant environment)

I attempted safe read-only checks against the public example domain from the assistant's execution environment.

| Test | Observed result |
|---|---|
| DNS lookup for `example.com` | Could not complete: temporary failure in name resolution |
| `ping -c 2 example.com` | Could not run: this environment does not permit raw ICMP sockets (`Operation not permitted`) |
| Traceroute | Not attempted because network access was unavailable |

**Interpretation:** these failures describe restrictions in the assistant's sandbox, not a fault with `example.com` and not the state of the student's network. A failed ping or DNS attempt in this restricted environment cannot be used to conclude that a website or network is down. No private IP addresses or network details are recorded.

## Reflection

In my own words, describe the main steps between entering a website address and seeing the page.

## Completion checklist

- [ ] Explained LAN, WAN, IP and domain names.
- [ ] Explained DNS, routers and switches.
- [ ] Compared HTTP and HTTPS.
- [ ] Ran at least one safe network command.
- [ ] Completed the observation log and reflection.

**Privacy and safety:** Do not publish Wi-Fi passwords, public or private IP addresses belonging to your home/school, router admin details, network maps or other private network information.
