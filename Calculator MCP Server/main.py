import random
from fastmcp import FastMCP

#Create a FastMCP Server instance
mcp = FastMCP(name = "DEMO Server")

@mcp.tool
def roll_dice(n_dice: int = 1) -> list[int]:
    """Roll a specified number of six-sided dice and return the results."""
    return [random.randint(1,6) for _ in range(n_dice)]


@mcp.tool
def add_numbers(a: float,b: float) -> float:
    """Add two numbers and return the result."""
    return a + b

@mcp.tool
def subtract_numbers(a: float,b: float) -> float:
    """Subtract two numbers and return the result."""
    return a - b

@mcp.tool
def multiply_numbers(a: float,b: float) -> float:
    """Multiply two numbers and return the result."""
    return a * b

@mcp.tool
def divide_numbers(a: float,b: float) -> float:
    """Divide two numbers and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@mcp.tool
def modulus_numbers(a: int,b: int) -> int:
    """Return the modulus of two integers."""
    return a % b

if __name__ == "__main__":
    mcp.run()