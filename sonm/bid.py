# https://docs.sonm.com/concepts/main-entities/order
from jinja2 import Template
import os
import tempfile


class BidParams:
    def __init__(self, duration: int = 0, price: str = '0 USD/h', counterparty: str = None, blacklist: str = None,
                 identity: str = 'anonymous', tag: str = None,
                 network: 'NetworkParams' = None, benchmarks: 'Benchmarks' = None):
        """
        BID order parameters
        """
        self.duration = duration
        self.price = price
        self.counterparty = counterparty
        self.blacklist = blacklist
        self.identity = identity
        self.tag = tag
        self.network = network
        self.benchmarks = benchmarks

    def get_yaml(self) -> str:
        """
            Yaml-text of bid order
        """
        import sonm
        template_path = os.path.join(os.path.dirname(sonm.__file__), 'templates/bid.jinja2')

        with open(template_path) as f:
            template_content = f.read()

        t = Template(template_content)
        yaml = t.render(bid=self)

        return yaml

    def save_yaml(self, yaml_path: str = None):
        """
        :param yaml_path: bid.yaml result path
        """
        if not yaml_path:
            _, yaml_path = tempfile.mkstemp(prefix='bid_', suffix='.yaml')

        yaml = self.get_yaml()
        with open(yaml_path, 'w') as f:
            f.write(yaml)

        return yaml_path


class NetworkParams:
    def __init__(self, overlay: bool = None, outbound: bool = None, incoming: bool = None):
        """
        Network resources parameters
        """
        self.overlay = overlay
        self.outbound = outbound
        self.incoming = incoming


class Benchmarks:
    def __init__(self, cpu_cores: float = None, cpu_sysbench_single: int = None, cpu_sysbench_multi: int = None,
                 ram_size: int = None, storage_size: int = None, net_download: int = None, net_upload: int = None,
                 gpu_count: int = None, gpu_mem: int = None, gpu_eth_hashrate: int = None,
                 gpu_cash_hashrate: int = None, gpu_redshift: int = None):
        """
        Benchmarks resources parameters
        """
        self.cpu_cores = cpu_cores
        self.cpu_sysbench_single = cpu_sysbench_single
        self.cpu_sysbench_multi = cpu_sysbench_multi
        self.ram_size = ram_size
        self.storage_size = storage_size
        self.net_download = net_download
        self.net_upload = net_upload
        self.gpu_count = gpu_count
        self.gpu_mem = gpu_mem
        self.gpu_eth_hashrate = gpu_eth_hashrate
        self.gpu_cash_hashrate = gpu_cash_hashrate
        self.gpu_redshift = gpu_redshift

