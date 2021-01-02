# usage:
# start a new cluster: python cluster_cmd.py launch num_cluster_nodes
# shutdown the whole cluster: python cluster_cmd.py shutdown

import sys

from bcolors import bcolors


def launch_cluster(num_nodes):
    print("launching {0} nodes cockroachdb cluster".format(num_nodes))


def shutdown_cluster():
    print("shutdowning cockroachdb cluster")


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
            launch_cluster(int(sys.argv[1]))
        elif sys.argv[1] == "shutdown":
            shutdown_cluster()
        elif sys.argv[1] == "help":
            print_help()
        else:
            unrecognized_usage()
