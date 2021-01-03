# cockroachdb_playground
some programs to play around cockroachdb


## start a local cluster 

```bash
python cluster_scripts/cluster_cmd.py launch cluster_size
```

## shutdown a local cluster

```bash
python cluster_scripts/cluster_cmd.py shutdown
```

## pick a random node from the cluster to run
```bash
python cluster_scripts/clsuter_cmd.py repl
```
