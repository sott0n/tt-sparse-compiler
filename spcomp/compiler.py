import torch
from torch.export import export

from torch_mlir import ir
from torch_mlir.dialects import torch as torch_dialect
from torch_mlir.extras.fx_importer import FxImporter


def compile(mod, *args, **kwargs):
    exported_prog: torch.export.ExportedProgram = export(mod, args, kwargs)

    print("debug:")
    print(exported_prog)
    print("-" * 50)

    ctx = ir.Context()
    torch_dialect.register_dialect(ctx)
    fx_importer = FxImporter(context=ctx)
    fx_importer.import_frozen_program(exported_prog)

    return fx_importer.module


def compile_and_run(mod, *args, **kwargs):
    compiled_mod = compile(mod, *args, **kwargs)
    print(compiled_mod)


class Add(torch.nn.Module):
    def forward(self, x, y):
        return torch.add(x, y)

add = Add()
compile_and_run(add, torch.randn(3, 4), torch.randn(3, 4))