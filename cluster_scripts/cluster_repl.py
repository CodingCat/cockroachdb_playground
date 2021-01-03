import random
from bcolors import bcolors

from cluster_launcher import ClusterLauncher


class ClusterRepl:
    @staticmethod
    def launch_repl():
        all_nodes = []
        cockroachdb_launch_record = open(f"{ClusterLauncher.crdb_launch_record_path}", "r")
        for line in cockroachdb_launch_record.readlines():
            s = f"localhost:{line.split(',')[2].strip()}"
            all_nodes.append(s)
        cmd = f"cockroach sql --insecure --host={all_nodes[random.randint(0, len(all_nodes) - 1)]}"
        print(f"{bcolors.OKGREEN}{cmd}{bcolors.ENDC}")