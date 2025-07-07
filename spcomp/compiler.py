import torch
from torch.export import export

def compile(mod, *args, **kwargs):
    exported_prog: torch.export.ExportedProgram = export(mod, args, kwargs)


def compile_and_run(mod, *args, **kwargs):
    invoker, program = compile(mod, *args, **kwargs)