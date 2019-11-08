import networkx
st=networkx.star_graph(5)
from dimod.reference.samplers import ExactSolver
sampler = ExactSolver()
import time
start=time.clock()
import dwave_networkx as dnx
print(dnx.min_vertex_cover(st, sampler))
end=time.clock()
print(end-start)
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())
start=time.clock()
print(dnx.min_vertex_cover(st, sampler))
end=time.clock()
print(end-start)
