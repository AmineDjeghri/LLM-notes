---
date modified: Tuesday, January 20th 2026, 5:36:10 pm
---
> [!note]
> This is a template of a guide. Copy paste the template and use it. 
> This template is compatible with the AI Tool 
> Delete this note when editing it. 


```table-of-contents

```
## News and updates
- item 1
## Easy guides
### Tunnel : how cloudflare tunnel  works without opening ports  ?
The reason Cloudflare Tunnel can work without you touching your router's firewall is based on a fundamental rule of networking: **Firewalls block unsolicited _incoming_ connections, but they allow _outgoing_ connections.**

Here is the breakdown of how it works, the "trick" it uses, and the specific architecture involved.
#### 1. The Core Concept: "Call Out, Don't Wait for a Call"

In a traditional setup (Port Forwarding), your server sits and waits for a stranger (the internet) to knock on your door (Port 80/443). Your firewall hates this and blocks it unless you poke a hole in it.

Cloudflare Tunnel reverses this.1 Instead of waiting for a knock, your server **calls Cloudflare first**.
- Since your server initiates the conversation from _inside_ the network, your firewall sees this as "safe" outbound traffic (just like when you browse the web from your laptop).
    
- Once this connection is established, Cloudflare uses this _already open_ line to send data back to you.
#### 2. The Architecture: How it Connects

To make this happen, you install a small piece of software called `cloudflared` (the daemon) on your server.

1. **Initialization:** When you start `cloudflared`, it immediately creates an **outbound** encrypted connection to the nearest Cloudflare data center.
    
2. **The Protocol:** It usually connects via HTTP/2 or HTTP/3 (QUIC) on port 7844 (or the standard 443).3 Because this is an outbound request, your firewall allows it automatically.
3. **The "Tunnel":** This connection is kept open permanently. It becomes a persistent "pipe."5
    
4. **Multiplexing:** Cloudflare can now push thousands of different web requests down this single open pipe.
#### 3. Step-by-Step Traffic Flow

Here is what happens when someone visits your website:

1. **The User:** A user types `www.yoursite.com`. Their request goes to Cloudflare's Edge Network (not your home IP).6
    
2. **Cloudflare Edge:** Cloudflare receives the request, decrypts it, and checks which Tunnel ID handles that domain.
    
3. **The Tunnel:** Cloudflare finds the open connection (tunnel) that your `cloudflared` daemon established earlier. It wraps the user's request inside a packet and shoots it down that pre-established tunnel.7
    
4. **Your Network:** The data enters your network through the connection your server already opened. The firewall lets it pass because it is part of an "established session."
    
5. **The Daemon:** `cloudflared` receives the package, unwraps it, and forwards the request to your actual web app (e.g., `localhost:8080`).
    
6. **The Return:** Your app responds, `cloudflared` wraps the response and sends it back up the tunnel to Cloudflare, which delivers it to the user.
#### 4. Why is this more secure?

|**Traditional Port Forwarding**|**Cloudflare Tunnel**|
|---|---|
|**Open Ports:** Requires opening Port 80/443 on your router.|**Closed Ports:** No ports open. Firewall remains in "Deny All" mode.|
|**Public IP:** Your home/server IP is exposed to the world.|**Hidden IP:** Your IP is hidden; users only see Cloudflare's IP.|
|**Attack Surface:** Bots can scan your IP and attack your router directly.|**Attack Surface:** Attackers hit Cloudflare first (which has DDoS protection).|

### How SSH works
SSH acts as a secure, encrypted pipe for sending text commands to a remote computer.1 It is the industry standard for managing servers.

#### 1. How SSH Works (The "Secret Handshake")

SSH is designed to allow two computers to talk safely over an unsafe network (like the internet).2 It uses a **Client-Server model**.

1. **The Negotiation:** When you run `ssh user@server`, your client contacts the server. They exchange public encryption keys to verify they are talking to the right machine (avoiding "Man-in-the-Middle" attacks).4
    
2. **The Encryption:** They negotiate a shared "Session Key." All data sent after this point is encrypted.5 If someone intercepts the data, it looks like gibberish.
    
3. **Authentication:** The server asks, "Are you allowed in?" You prove your identity using a **Password** or (much better) an **SSH Key Pair**.6
    
4. **The Shell:** Once logged in, the server gives you a shell (command prompt).7

#### 2. Does it require Port 22 to be open on the router?

**The short answer:**

- **For local access (LAN):** **No.** If you are sitting on your couch and SSH-ing into a Raspberry Pi in the kitchen, you do not need to touch your router settings.
    
- **For internet access (WAN):** **Yes.** If you want to SSH into your home computer from a coffee shop, you **must** log into your router and set up **Port Forwarding** for Port 22.

Why?

Your router uses NAT (Network Address Translation). When a request comes from the internet on Port 22, your router doesn't know which device in your house it's meant for (your laptop? your phone? your server?). Port Forwarding tells the router: "Any traffic hitting Port 22 comes to me, send it to the server at 192.168.1.50."8

#### 3. Is Port 22 open by default?

There are two layers to check here: the Router and the Computer (OS).

##### A. On the Router (The Front Door)

- **Default Status: CLOSED.**
    
- Almost all consumer routers block **all** incoming unsolicited traffic by default. Even if your computer is ready to accept SSH connections, the router will drop the packet before it even reaches your computer unless you explicitly open it.
##### B. On the Computer/Server (The Room Door)

- **Windows/macOS:** **Closed/Disabled by default.** You usually have to go into settings (e.g., "Remote Login" on Mac) to turn it on.
    
- **Ubuntu/Linux Desktop:** **Closed/Not Installed.** You usually have to install `openssh-server`.
    
- **Linux Server (e.g., VPS):** **Open.** Because servers are designed to be managed remotely, the SSH service is usually running out of the box.

---
#### Port 22 is closed on the client
- **Client (You):** Can send messages _out_ from any port.
- **Server :** Must listen _in_ on Port 22.
SSH tunnel needs only the port 22 to be open on the server and not the client.

- **The Outbound Request:** Your Windows laptop picks a random, temporary port (called an **Ephemeral Port**, like 54321) to act as the "sender." It sent a message saying: _"Hello, I am calling from Port 54321. I need to speak to Port 22."_
    
- **The Firewall Rule:** Your Windows firewall blocks _incoming_ strangers, but it allows almost all _outgoing_ requests. Since you initiated the call, the firewall let it out.
    
- **The Connection:** The Ubuntu server received the packet on Port 22 since it’s open, saw it came from your IP at Port 54321, and replied back to that specific port.

Rule: any request from A to B, needs something open on B and not A. (That’s why cloudflare tunnel for example work)
#### ⚠️ Critical Security Warning

Opening Port 22 on your router to the wide internet is risky.

Botnets constantly scan the entire internet for open Port 22s and try to brute-force passwords. If you open Port 22, you should never use a simple password.

**Better Alternatives to Opening Port 22:**

1. **Cloudflare Tunnel:** As we discussed, you can actually route SSH through Cloudflare Tunnel.9 This lets you SSH from anywhere **without** opening Port 22 on your router.
    
2. **VPN:** Host a VPN server (like WireGuard) at home. Connect to the VPN first, then SSH as if you were on the local network.
## Tools / libraries 
- item 1

## Papers and research
- item 1

## Other resources 
- item 1