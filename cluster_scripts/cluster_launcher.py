import os
import subprocess

from bcolors import bcolors


class ClusterLauncher:
    start_tcp_port = 22650
    start_http_port = 8080
    crdb_playground_dir = f"{os.path.expanduser('~')}/.cockroach_playground"
    crdb_launch_record_path = f"{crdb_playground_dir}/launching_record"

    @staticmethod
    def __compose_join_str(num_nodes, start_tcp_port):
        ret = []
        for listen_tcp_port in range(start_tcp_port, start_tcp_port + num_nodes):
            ret.append(f"localhost:{listen_tcp_port}")
        return ','.join(ret)

    # format of file: current working dir, node_id, port number
    @staticmethod
    def __write_launching_records(num_nodes):
        if not os.path.exists(ClusterLauncher.crdb_playground_dir):
            os.mkdir(ClusterLauncher.crdb_playground_dir)
        f = open(f"{ClusterLauncher.crdb_launch_record_path}", "w")
        cwd = os.getcwd()
        for listen_tcp_port in range(ClusterLauncher.start_tcp_port, ClusterLauncher.start_tcp_port + num_nodes):
            f.write(f"{cwd},node_{listen_tcp_port - ClusterLauncher.start_tcp_port},{listen_tcp_port}\n")
        f.close()

    @staticmethod
    def launch_cluster(num_nodes):
        print(f"{bcolors.OKGREEN}launching {num_nodes} nodes cockroachdb cluster{bcolors.ENDC}")
        for listen_tcp_port in range(ClusterLauncher.start_tcp_port, ClusterLauncher.start_tcp_port + num_nodes):
            command_line = f"cockroach start" \
                           f" --insecure" \
                           f" --store=node_{listen_tcp_port - ClusterLauncher.start_tcp_port} " \
                           f"--listen-addr=localhost:{listen_tcp_port} " \
                           f"--http-addr=localhost:{ClusterLauncher.start_http_port + listen_tcp_port - ClusterLauncher.start_tcp_port} " \
                           f"--join={ClusterLauncher.__compose_join_str(num_nodes, ClusterLauncher.start_tcp_port)} " \
                           f"--background"
            print(f"{bcolors.OKCYAN}{command_line}{bcolors.ENDC}")
            subprocess.Popen(command_line.split(" "))
        print(f"{bcolors.OKGREEN}successfully launched {num_nodes} nodes cockroachdb cluster{bcolors.ENDC}")
        ClusterLauncher.__write_launching_records(num_nodes)
