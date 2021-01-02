# usage:
# start a new cluster: python cluster_cmd.py launch num_cluster_nodes
# shutdown the whole cluster: python cluster_cmd.py shutdown

import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


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
