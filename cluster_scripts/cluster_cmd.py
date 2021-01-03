import sys

from bcolors import bcolors
from cluster_launcher import ClusterLauncher
from cluster_shutdown import ClusterShutdown
from cluster_repl import ClusterRepl

start_tcp_port = 22650
start_http_port = 8080


def print_help():
    print("usage:")
    print(f"{bcolors.OKGREEN}start a new cockroachdb cluster:{bcolors.ENDC} python cluster_cmd.py launch num_cluster_nodes")
    print(f"{bcolors.OKGREEN}shutdown the last-started cockroachdb cluster:{bcolors.ENDC} python cluster_cmd.py shutdown")
    print(f"{bcolors.OKGREEN}print this help:{bcolors.ENDC} python cluster_cmd.py help")


def unrecognized_usage():
    print(f"{bcolors.FAIL}unrecognizable usage, please use `python cluster_cmd.py help` to check the help{bcolors.ENDC}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        unrecognized_usage()
    else:
        if sys.argv[1] == "launch":
            if len(sys.argv) < 3:
                print_help()
            else:
                ClusterLauncher.launch_cluster(int(sys.argv[2]))
        elif sys.argv[1] == "shutdown":
            ClusterShutdown.shutdown_cluster()
        elif sys.argv[1] == "repl":
            ClusterRepl.launch_repl()
        elif sys.argv[1] == "help":
            print_help()
        else:
            unrecognized_usage()
