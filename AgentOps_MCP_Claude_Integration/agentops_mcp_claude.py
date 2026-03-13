from mcp.server.fastmcp import FastMCP
import agentops
import os
from dotenv import load_dotenv
from agentops.sdk.decorators import trace, tool

# Load environment variables
load_dotenv()

# Initialize AgentOps with proper configuration
agentops.init(
    api_key=os.getenv("AGENTOPS_API_KEY"),
    default_tags=["mcp", "calculator", "test"],
    auto_start_session=False,  # We'll manage traces manually
    trace_name="calculator-mcp-test"
)

# Initialize MCP Server
mcp = FastMCP("Test Calculator Server")

# Simple calculator tool with proper AgentOps tracing
@mcp.tool("add")
@tool(cost=0.01)  # Track cost in AgentOps
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together"""
    print(f"Tool called: add({a}, {b})")
    
    # Create a trace for this operation
    trace = agentops.start_trace("addition-operation", tags=["math", "addition"])
    
    try:
        result = a + b
        
        # Update trace metadata with operation details
        agentops.update_trace_metadata({
            "operation_type": "addition",
            "input_a": a,
            "input_b": b,
            "result": result,
            "status": "success"
        })
        
        print(f"Addition result: {result}")
        
        # End trace successfully
        agentops.end_trace(trace, "Success")
        
        return result
        
    except Exception as e:
        print(f"Addition error: {e}")
        
        # Update trace with error info
        agentops.update_trace_metadata({
            "operation_type": "addition",
            "input_a": a,
            "input_b": b,
            "error": str(e),
            "status": "error"
        })
        
        # End trace with error
        agentops.end_trace(trace, "Error")
        raise

@mcp.tool("multiply")
@tool(cost=0.01)
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together"""
    print(f"Tool called: multiply({a}, {b})")
    
    # Create a trace for this operation
    trace = agentops.start_trace("multiplication-operation", tags=["math", "multiplication"])
    
    try:
        result = a * b
        
        # Update trace metadata
        agentops.update_trace_metadata({
            "operation_type": "multiplication",
            "input_a": a,
            "input_b": b,
            "result": result,
            "status": "success"
        })
        
        print(f"Multiplication result: {result}")
        
        # End trace successfully
        agentops.end_trace(trace, "Success")
        
        return result
        
    except Exception as e:
        print(f"Multiplication error: {e}")
        
        agentops.update_trace_metadata({
            "operation_type": "multiplication",
            "input_a": a,
            "input_b": b,
            "error": str(e),
            "status": "error"
        })
        
        agentops.end_trace(trace, "Error")
        raise

# Simple greeting resource
@mcp.resource("test://hello")
@trace
def hello_world() -> str:
    """Return a simple hello message"""
    print("Hello resource called")
    
    agentops.update_trace_metadata({
        "resource_type": "greeting",
        "message": "Hello from AgentOps MCP!"
    })
    
    return "Hello from AgentOps MCP Server!"

if __name__ == "__main__":
    print("=== AgentOps MCP Test Server Starting ===")
    print("This server will create proper traces for AgentOps")
    
    # Start main server trace
    server_trace = agentops.start_trace("mcp-server-session", tags=["server", "mcp", "test"])
    
    agentops.update_trace_metadata({
        "server_name": "Test Calculator MCP",
        "server_status": "starting"
    })
    
    try:
        print("Server running and ready for connections...")
        mcp.run(transport="stdio")
        
    except KeyboardInterrupt:
        print("\n=== Server Shutting Down ===")
        agentops.update_trace_metadata({
            "server_status": "shutdown",
            "shutdown_reason": "user_interrupt"
        })
        agentops.end_trace(server_trace, "Success")
        
    except Exception as e:
        print(f"=== Server Error: {e} ===")
        agentops.update_trace_metadata({
            "server_status": "error",
            "error": str(e)
        })
        agentops.end_trace(server_trace, "Error")