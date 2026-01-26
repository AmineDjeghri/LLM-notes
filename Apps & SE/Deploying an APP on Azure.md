---
date modified: Saturday, January 24th 2026, 3:56:40 pm
---
#### Deploy the app on Azure  
  
##### 1. Azure Network & Domain Configuration  
  
You need to configure the Network Security Group (NSG) in the Azure Portal for proper access:  
  
* **Application Ports:** Open inbound ports **8080** and **3000** if you need direct HTTP access to the apps.  
* **SSH Access:** Open port **22** for remote management.  
* Authorize AXA's IPs and your domestic IP.  
> **⚠️ AXA Network Note:** Standard SSH access is blocked while connected to the AXA corporate VPN. You must disconnect from the VPN to SSH into the VM.  
- Try to SSH from AXA's computer to the server without the VPN.  
  
##### 1. Launching the Application  
  
You have two options to deploy the application:  
  
* **Via Make:** Run `make run-webui` directly from the repository or add it to ubuntu services to automatically start.  
* **Via Docker:** Use the provided docker compose file.  
  
Try to access to the web app from your domestic IP (on a phone for example to test if it works on the VM-IP:8080)  
If you can access the web app, it means your VM is configured correctly and HTTP works.  
* **Domain Name Setup:** AXA security policies block web browsing directly to public IP addresses. You must assign an Azure DNS label (e.g., `your-app.westeurope.cloudapp.azure.com`) to your VM's public IP to access the web UI.  
  
### 3. Setting Up HTTPS (Caddy)  
  
To secure the application with HTTPS, use the provided `Caddyfile`.  
  
**Step 1: Temporary Port Opening**  
To generate the free Let's Encrypt SSL certificate, Let's Encrypt needs to verify your server. You must temporarily **open port 443 to "Everyone" (Any)** in your Azure NSG.  
  
**Step 2: Start Caddy**  
  
* **For Testing:** Run `sudo caddy run` in your project folder. This uses the local `Caddyfile` and runs in the foreground.  
* **For Production (Recommended):** Caddy should run as a background system service. The system service strictly looks for the configuration file at `/etc/caddy/Caddyfile`.  
```bash  
# Copy your project's Caddyfile to the system directory  
sudo cp Caddyfile /etc/caddy/Caddyfile  
  
# Start the Caddy service  
sudo systemctl enable --now caddy  
  
```  
  
  
**Step 3: Secure the Port**  
Once HTTPS is working, you can restrict port 443 to just your own IP address for security.  
  
* **Maintenance Note:** Certificates expire every 90 days. Caddy automatically tries to renew them after 60 days. You will need to briefly open port 443 to "Everyone" again at that time to allow the renewal.  
  
---  
  
### 💡 Useful Pro-Tips & Troubleshooting  
  
* **Zero-Downtime Reloads:** If you change the `Caddyfile` in the future, don't restart the service (which causes downtime). Instead, reload the configuration gracefully:  
```bash  
sudo systemctl reload caddy  
```  
  
* **Python app as a service:** If you want to run the python app as a service, you can use `systemd` to create a service for it. Do the following:  
```bash  
sudo nano /etc/systemd/system/webui.service```  
And fill it with the app information :   
```  
[Unit]  
Description=Run app via make run-webui  
After=network.target  
  
[Service]  
Type=simple  
User=azureuser  
Environment="HOME=/home/azureuser"  
Environment="PATH=/usr/local/bin:/usr/bin:/bin"  
WorkingDirectory=/home/azureuser/genai-model-assessment  
ExecStart=/usr/bin/env bash -lc 'cd "$HOME/genai-model-assessment" && make run-webui'  
Restart=on-failure  
RestartSec=10  
  
[Install]  
WantedBy=multi-user.target  
```  
  
- Then, enable and start the service:  
```bash  
sudo systemctl enable --now webuisudo systemctl status webui```  
- check the logs with : `sudo journalctl -u webui -f`  
	- `-u` (Unit) Without `-u`, Linux would dump every single log from the entire server (boot sequences, firewall blocks, network updates, other apps). By using `-u webui.service`, you filter out the noise and only see the output from your specific Python app.
	
	 - `-f` (Follow) : Without `-f`, the command just prints the past logs and returns you to the command prompt. With `-f`, the terminal stays open and prints new log messages in real-time as your app generates them. It is exactly like `tail -f` in standard Linux.

* **Checking Caddy Logs:** If something goes wrong, you can view the live system logs with:  
```bash  
sudo journalctl -u caddy --no-pager | tail -n 50  
```  
  
* **Permanent Fix for Port 443 (DNS Challenge):** If you want to keep Port 443 locked down permanently without needing to open it every 60 days, you can configure Caddy to use the "DNS Challenge". This verifies your domain via Azure DNS APIs instead of incoming web traffic.