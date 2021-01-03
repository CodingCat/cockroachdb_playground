import subprocess

from cluster_launcher import ClusterLauncher
from bcolors import bcolors


class ClusterShutdown:
    @staticmethod
    def shutdown_cluster():
        print(f"{bcolors.WARNING}shutdowning cockroachdb cluster{bcolors.ENDC}")
        cockroachdb_launch_record = open(f"{ClusterLauncher.crdb_launch_record_path}", "r")
        for line in cockroachdb_launch_record.readlines():
            port = line.split(",")[2].strip()
            command_line = f"cockroach quit --insecure --host=localhost:{port}"
            print(f"{bcolors.WARNING}{command_line}{bcolors.ENDC}")
            process = subprocess.Popen(command_line.split(" "))
            stdout, std_err = process.communicate()
            print(stdout)
            print(std_err)
        print(f"{bcolors.OKGREEN}successfully shutdown cluster{bcolors.ENDC}")