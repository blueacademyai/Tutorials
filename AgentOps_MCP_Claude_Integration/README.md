# AgentOps MCP Claude Integration

This guide will help you set up and run the **AgentOps MCP Claude** integration.


## 📌 Setup Instructions

### 1. Create Project Directory
Open **Command Prompt** in your **Documents** folder and run:
```bash
mkdir agentops_mcp_claude
cd agentops_mcp_claude
````

### 2. Copy Files

Copy and paste the provided project files into the newly created `agentops_mcp_claude` folder.

### 3. Configure Environment Variables

* Create `.env` file and replace the placeholder with your **AgentOps API key**.
  
   ```
   AGENTOPS_API_KEY=your_agentops_api_key
   ```
* Update the same API key inside `claude_desktop_config.json`.

### 4. Update Python File Path

In `claude_desktop_config.json`, set the full path to your Python file.

### 5. Apply Claude Configuration

1. Press **Win + R**, then paste:

   ```
   %APPDATA%\Claude
   ```
2. Copy `claude_desktop_config.json` into this destination folder.

### 6. Run the Python File

From the `agentops_mcp_claude` folder, execute:

```bash
python your_file.py
```

### 7. Test in Claude

Open **Claude Desktop** and try sample prompts:

* `Add 12 and 15`
* `Multiply 2 and 4`

### 8. View Traces in AgentOps

Go to the [AgentOps Dashboard](https://app.agentops.ai) → **Traces** section
to view the prompts and execution updates.

