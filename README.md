# Ikcon Protobuf

## Installation

Run the [pip](https://pip.pypa.io/en/stable/) command to install the latest version:
```bash
 pip install https://github.com/sitmena/ikcon-protobuf.git
```

## Recompile The Messages

Go to the root of the project and run the following commands:

```bash
 cd ikcon_protobuf
 protoc order.proto --python_out=.
 protoc cogs.proto --python_out=.
```
