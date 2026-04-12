# brushcue

Python bindings for the Matisse graph computation system, built with PyO3 + maturin.

## Build

```bash
cd py/brushcue
uv sync                  # recommended — resolves deps and builds the extension
# or manually:
python -m venv .venv
source .venv/bin/activate
pip install maturin jupyter ipykernel
maturin develop          # dev build (faster, editable)
# or
./build_python.sh        # release build
```

> Built against Python's stable ABI (`abi3-py311`), so the compiled extension works on Python 3.11+.

## Jupyter Notebook

After building, register the venv as a Jupyter kernel and launch:

```bash
python -m ipykernel install --user --name brushcue --display-name "brushcue"
jupyter notebook
```

Select the **brushcue** kernel in the notebook UI, then:

```python
import brushcue

ctx = brushcue.Context()
handle = brushcue.Handle()

# Build a simple graph and execute
result = brushcue.Graph.int_constant(42).execute(ctx, handle)
print(result.as_int())   # 42

# Project round-trip
p = brushcue.Project()
p.add_graph(brushcue.Graph.int_constant(99))

data = p.serialize(ctx)          # returns bytes
p2 = brushcue.Project.deserialize(ctx, data)
print("round-trip OK, nodes:", len(p2.all_nodes()))
```

All methods are synchronous — no `await` or event loop needed.
