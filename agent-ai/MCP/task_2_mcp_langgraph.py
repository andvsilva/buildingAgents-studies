#!/usr/bin/env python3
"""Task 1: Understanding MCP Basics - Final Clean MCP Server"""

import os
import logging

# =========================
# LOGGING CONFIG
# =========================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logger = logging.getLogger(__name__)

logger.info("📡 Starting MCP Calculator Server")

# =========================
# MCP IMPORT (REAL OR MOCK)
# =========================
try:
    from mcp.server.fastmcp import FastMCP
    logger.info("✅ Using real MCP SDK")
except ImportError:
    logger.warning("⚠️ Using mock FastMCP (install with 'pip install mcp')")

    class FastMCP:
        """Mock FastMCP server for learning"""
        def __init__(self, name):
            self.name = name
            self.tools = []

        def tool(self):
            def decorator(func):
                self.tools.append({
                    'name': func.__name__,
                    'function': func
                })
                return func
            return decorator

        def run(self, transport="stdio"):
            logger.info(f"🚀 {self.name} MCP Server running (mock)")
            logger.info(f"📦 Available tools: {[t['name'] for t in self.tools]}")
            logger.info("🔁 Waiting for requests...\n")


# =========================
# INITIALIZE SERVER
# =========================
mcp = FastMCP("Calculator")


# =========================
# VALIDATION HELPER
# =========================
def validate_numbers(*args):
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError("All inputs must be numbers")


# =========================
# TOOLS
# =========================

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers"""
    validate_numbers(a, b)
    result = a + b
    logger.info(f"add({a}, {b}) = {result}")
    return result


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    validate_numbers(a, b)
    result = a * b
    logger.info(f"multiply({a}, {b}) = {result}")
    return result


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers (raises error if division by zero)"""
    validate_numbers(a, b)

    if b == 0:
        logger.error("Division by zero attempted")
        raise ValueError("Cannot divide by zero")

    result = a / b
    logger.info(f"divide({a}, {b}) = {result}")
    return result


@mcp.tool()
def power(a: float, b: float) -> float:
    """Raise a to the power of b"""
    validate_numbers(a, b)
    result = a ** b
    logger.info(f"power({a}, {b}) = {result}")
    return result


@mcp.tool()
def get_env_variable(name: str) -> str:
    """Get environment variable value"""
    if not isinstance(name, str):
        raise TypeError("Environment variable name must be a string")

    value = os.getenv(name)
    if value is None:
        raise ValueError(f"Environment variable '{name}' not found")

    logger.info(f"get_env_variable({name}) = {value}")
    return value


# =========================
# TESTING (LOCAL SIMULATION)
# =========================
def test_tools():
    logger.info("=" * 60)
    logger.info("🧪 TESTING MCP TOOLS")
    logger.info("=" * 60)

    try:
        logger.info("Test 1: Addition")
        logger.info(f"Response: {add(5, 3)}")

        logger.info("Test 2: Multiplication")
        logger.info(f"Response: {multiply(4, 7)}")

        logger.info("Test 3: Division")
        logger.info(f"Response: {divide(10, 2)}")

        logger.info("Test 4: Power")
        logger.info(f"Response: {power(2, 3)}")

        logger.info("Test 5: Division by zero (expected error)")
        try:
            divide(5, 0)
        except Exception as e:
            logger.info(f"Expected error: {e}")

    except Exception as e:
        logger.error(f"❌ Unexpected error during tests: {e}")


# =========================
# MAIN ENTRYPOINT
# =========================
if __name__ == "__main__":

    # Run tests ONLY when executed directly
    test_tools()

    # Create marker file safely
    os.makedirs("markers", exist_ok=True)
    with open("markers/task1_mcp_basics_complete.txt", "w") as f:
        f.write("TASK1_COMPLETE")

    logger.info("=" * 60)
    logger.info("💡 KEY CONCEPTS")
    logger.info("- FastMCP creates MCP servers easily")
    logger.info("- @mcp.tool() exposes functions to AI")
    logger.info("- Type hints are critical for tool usage")
    logger.info("- Errors should raise exceptions")
    logger.info("- MCP servers run continuously")
    logger.info("=" * 60)

    logger.info("🚀 STARTING MCP SERVER")
    logger.info("Server running... Press Ctrl+C to stop")

    # Start MCP server (safe for multiple versions)
    try:
        mcp.run()
    except KeyboardInterrupt:
        logger.info("🛑 Server stopped by user")