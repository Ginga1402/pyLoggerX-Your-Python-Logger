

# 📜 pyLoggerX - Your Python Logger


## 🔧 A high-performance, structured, and extensible Python logging library for modern applications.


---

## 🧾 Project Description


**pyLoggerX** is a high-performance, structured, and extensible Python logging library designed for modern applications.

With minimal setup, pyLoggerX offers:
- ✅ Advanced log formatting with timestamps, levels, module names, and line numbers
- ✅ Log rotation with backup support
- ✅ File and console stream handlers
- ✅ Full support for all standard log levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`)
- ✅ Optional JSON log formatting for integration with log aggregators
- ✅ Scalable and production-ready design

Ideal for developers building scalable, production-ready systems in Python.

---

## 📂 Project Structure

```

pyLoggerX/
├── logger/
│ ├── init.py
│ ├── config.py # Centralized logger configuration
│ └── custom_logger.py # Core logging logic
├── Logs/ # Auto-generated folder to store log files
├── demo.py # Demonstrates usage of the logger
└── README.md # Project documentation

```

---

## ✅ Use Cases

- 🧠 LLM pipelines (Langchain, etc.) requiring traceability
- 🌐 Web backends (Flask, FastAPI) needing structured logs
- 🛠️ Python microservices with rotating log files
- 📊 CLI utilities needing simple file/stream logs
- 🧪 General Python scripts in need of reliable logging

---

## ▶️ Usage

Import and use the logger in your module:

```python
from logger.custom_logger import get_logger

logger = get_logger("my_module")

def sample_function():
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")

sample_function()

```

Check demo.py for a complete demonstration of log levels and exception logging.


---


##🖼️ Output Sample (Log File)

```
2025-06-24 22:52:10 | DEBUG | my_module | demo:6 | Debug message
2025-06-24 22:52:10 | INFO | my_module | demo:7 | Info message
2025-06-24 22:52:10 | WARNING | my_module | demo:8 | Warning message
2025-06-24 22:52:10 | ERROR | my_module | demo:9 | Error message
2025-06-24 22:52:10 | CRITICAL | my_module | demo:10 | Critical message
2025-06-24 22:52:10 | ERROR | my_module | demo:14 | Exception occurred
Traceback (most recent call last):
  File "demo.py", line 12, in sample_function
    x = 1 / 0
ZeroDivisionError: division by zero
```

## ⚙️ Tech Stack

1. Language: Python 3.10+

2. Core: logging, logging.handlers

3. Formats: Plain text (default), JSON (optional)

4. Handlers: File handler with rotation, Stream handler (console)

   
