"""CLI entry point for Digital Literacy Bridge."""

import uvicorn
from digital_literacy_bridge.api.app import app


def main() -> None:
    """Run the Digital Literacy Bridge server."""
    uvicorn.run(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
