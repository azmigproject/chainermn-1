import pkg_resources

from chainermn import communicators  # NOQA
from chainermn import datasets  # NOQA
from chainermn import extensions  # NOQA
from chainermn import functions  # NOQA
from chainermn import iterators  # NOQA
from chainermn import links  # NOQA
from chainermn import optimizers  # NOQA

from chainermn.communicators import create_communicator  # NOQA
from chainermn.datasets import DataSizeError  # NOQA
from chainermn.datasets import scatter_dataset  # NOQA
from chainermn.extensions import create_multi_node_checkpointer  # NOQA
from chainermn.extensions import create_multi_node_evaluator  # NOQA
from chainermn.links import MultiNodeChainList  # NOQA
from chainermn.optimizers import create_multi_node_optimizer  # NOQA


__version__ = pkg_resources.get_distribution('chainermn').version
