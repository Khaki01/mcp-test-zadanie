# server.py

import os
import time
from pathlib import Path
from typing import Any, Dict, List

from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("fast-demo", log_level="ERROR")

@mcp.tool()
def search_files(fragment: str) -> List[Dict[str, Any]]:
    count = 0
    results = []
    search_root = Path.home() / "Desktop" # Искать в домашней директории
    
    for root, _, files in os.walk(search_root):
        if count > 20:
            # лимит на резы для удобства тз
            break
        for file in files:
            full_path = Path(root) / file
            if fragment in str(full_path):
                try:
                    stat = full_path.stat()
                    results.append({
                        "name": file,
                        "path": str(full_path),
                        "size": stat.st_size,
                        "created": time.strftime(
                            "%Y-%m-%d %H:%M:%S", 
                            time.localtime(stat.st_ctime)
                        )
                    })
                    count += 1
                except Exception as e:
                    continue
    return results

if __name__ == "__main__":
    mcp.run()