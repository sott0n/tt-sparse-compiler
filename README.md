# tt-sparse-compiler

This project is an experimental sparsity compiler for Tenstorrent device.

## How to build

This project depends on [torch-mlir](https://github.com/llvm/torch-mlir), and it builds bot MLIR and torch-mlir from source. Follow the steps below to set up your environment are build the project. 

### 1. Clone and Update Submodule

Make sure all submodules are initialized are updated:

```bash
git submodule update --init --recursive --progress
```

To keep submodules always updated in future clones:

```bash
git config --global submodule.recurse true
```

### 2. Setup Python Virtual Environment

It is recommended to use a virtual environment to isolate dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Set PYTHONPATH
Export paths so Python can locate both the torch-mlir Python package and this project's module:

```bash
export PYTHONPATH=$(pwd)/tt-sparse-compiler/build/tools/torch-mlir/python_packages/torch_mlir:$(pwd)/tt-sparse-compiler/spcomp
```

### 4. Install Python Dependencies

Install all required Python packages for torch-mlir:

```bash
python -m pip install --upgrade pip
python -m pip install -r externals/torch-mlir/requirements.txt
python -m pip install -r externals/torch-mlir/torchvision-requirements.txt
```

### 5. Build the Project

This project performs an in-tree build of both MLIR and torch-mlir.

```bash
cmake -GNinja -Bbuild \
  -DCMAKE_BUILD_TYPE=Release \
  -DPython3_FIND_VIRTUALENV=ONLY \
  -DLLVM_ENABLE_PROJECTS=mlir \
  -DLLVM_EXTERNAL_PROJECTS="torch-mlir" \
  -DLLVM_EXTERNAL_TORCH_MLIR_SOURCE_DIR="${PWD}/externals/torch-mlir" \
  -DLLVM_TARGETS_TO_BUILD=host \
  -DMLIR_ENABLE_BINDINGS_PYTHON=ON \
  externals/torch-mlir/externals/llvm-project/llvm
```

Then build:

```bash
cmake --build build
```
