#!/bin/sh
# for i in deepWalk node2vec grarep hope sdne line gf tadw
# do
# 	for j in 4 8 16 32 64 128
# 	do
# 		python -m openne --label-file data/cora/cora_labels.txt --input data/cora/cora_edgelist.txt --graph-format edgelist --feature-file data/cora/cora.features --epochs 200 --output vec_all.txt --representation-size $j --method $i
# 	done
# 	for k in 0.2 0.3 0.4 0.5 0.6 0.7 0.8
# 	do
# 		python -m openne --label-file data/cora/cora_labels.txt --input data/cora/cora_edgelist.txt --graph-format edgelist --feature-file data/cora/cora.features --epochs 200 --output vec_all.txt --clf-ratio $k --method $i
# 	done
# done

# for i in deepWalk node2vec grarep hope sdne line gf tadw
# do
# 	for j in 4 8 16 32 64 128
# 	do
# 		python -m openne --label-file data/citeseer/citeseer_labels.txt --input data/citeseer/citeseer_edgelist.txt --graph-format edgelist --feature-file data/citeseer/citeseer.features --epochs 200 --output vec_all.txt --representation-size $j --method $i
# 	done
# 	for k in 0.2 0.3 0.4 0.5 0.6 0.7 0.8
# 	do
# 		python -m openne --label-file data/citeseer/citeseer_labels.txt --input data/citeseer/citeseer_edgelist.txt --graph-format edgelist --feature-file data/citeseer/citeseer.features --epochs 200 --output vec_all.txt --clf-ratio $k --method $i
# 	done
# done

# for i in tadw
# do
# 	for k in 0.7 0.8
# 	do
# 		python -m openne --label-file data/pubmed/pubmed_labels.txt --input data/pubmed/pubmed_edgelist.txt --graph-format edgelist --feature-file data/pubmed/pubmed.features --epochs 200 --output vec_all.txt --clf-ratio $k --method $i
# 	done
# done

python -m openne --label-file data/cora/cora_labels.txt --input data/cora/cora_edgelist.txt --graph-format edgelist --feature-file data/cora/cora.features --epochs 200 --output vec_all.txt --method DeepWalk
python -m openne --label-file data/cora/cora_labels.txt --input data/cora/cora_edgelist.txt --graph-format edgelist --feature-file data/cora/cora.features --epochs 200 --output vec_all.txt --method LINE
python -m openne --label-file data/cora/cora_labels.txt --input data/cora/cora_edgelist.txt --graph-format edgelist --feature-file data/cora/cora.features --epochs 200 --output vec_all.txt --method SDNE