# GRLL (Graph Representation Learning Library)

Scripts to reproduce results in [Graph Representation Learning: A Survey](https://arxiv.org/abs/1909.00958).

We use [OpenNE](https://github.com/thunlp/OpenNE) to train and evaluate different network embedding algorithms.
Follow the steps in [this repo](https://github.com/thunlp/OpenNE) to install openne.
Multiple benchmark datasets are included in [data](./data).

## Usage

#### Run

    source ./examples/accuracy.sh

#### Input
If you want to run on your own datasets, follow the input format below. The supported input format is an edgelist or an adjlist:

    edgelist: node1 node2 <weight_float, optional>
    adjlist: node n1 n2 n3 ... nk
The graph is assumed to be undirected and unweighted by default. These options can be changed by setting the appropriate flags.

If the model needs additional features, the supported feature input format is as follow (**feature_i** should be a float number):

    node feature_1 feature_2 ... feature_n


#### Output
The output file has *n+1* lines for a graph with *n* nodes. 
The first line has the following format:

    num_of_nodes dim_of_representation

The next *n* lines are as follows:
    
    node_id dim1 dim2 ... dimd

where dim1, ... , dimd is the *d*-dimensional representation learned by *OpenNE*.

#### Evaluation

If you want to evaluate the learned node representations, you can input the node labels. It will use a portion (default: 50%) of nodes to train a classifier and calculate F1-score on the rest dataset.

The supported input label format is

    node label1 label2 label3...

## Citing

If you find *GRLL* is useful for your research, please consider citing the following papers:

    @article{chen2020graph,
      title={Graph representation learning: a survey},
      author={Chen, Fenxiao and Wang, Yun-Cheng and Wang, Bin and Kuo, C-C Jay},
      journal={APSIPA Transactions on Signal and Information Processing},
      volume={9},
      year={2020},
      publisher={Cambridge University Press}
    }

    @InProceedings{perozzi2014deepwalk,
      Title                    = {Deepwalk: Online learning of social representations},
      Author                   = {Perozzi, Bryan and Al-Rfou, Rami and Skiena, Steven},
      Booktitle                = {Proceedings of KDD},
      Year                     = {2014},
      Pages                    = {701--710}
    }
    
    @InProceedings{tang2015line,
      Title                    = {Line: Large-scale information network embedding},
      Author                   = {Tang, Jian and Qu, Meng and Wang, Mingzhe and Zhang, Ming and Yan, Jun and Mei, Qiaozhu},
      Booktitle                = {Proceedings of WWW},
      Year                     = {2015},
      Pages                    = {1067--1077}
    }
    
    @InProceedings{grover2016node2vec,
      Title                    = {node2vec: Scalable feature learning for networks},
      Author                   = {Grover, Aditya and Leskovec, Jure},
      Booktitle                = {Proceedings of KDD},
      Year                     = {2016},
      Pages                    = {855--864}
    }
    
    @article{kipf2016semi,
      Title                    = {Semi-Supervised Classification with Graph Convolutional Networks},
      Author                   = {Kipf, Thomas N and Welling, Max},
      journal                  = {arXiv preprint arXiv:1609.02907},
      Year                     = {2016}
    }
    
    @InProceedings{cao2015grarep,
      Title                    = {Grarep: Learning graph representations with global structural information},
      Author                   = {Cao, Shaosheng and Lu, Wei and Xu, Qiongkai},
      Booktitle                = {Proceedings of CIKM},
      Year                     = {2015},
      Pages                    = {891--900}
    }
    
    @InProceedings{yang2015network,
      Title                    = {Network representation learning with rich text information},
      Author                   = {Yang, Cheng and Liu, Zhiyuan and Zhao, Deli and Sun, Maosong and Chang, Edward},
      Booktitle                = {Proceedings of IJCAI},
      Year                     = {2015}
    }
    
    @Article{tu2017network,
      Title                    = {Network representation learning: an overview},
      Author                   = {TU, Cunchao and YANG, Cheng and LIU, Zhiyuan and SUN, Maosong},
      Journal                  = {SCIENTIA SINICA Informationis},
      Volume                   = {47},
      Number                   = {8},
      Pages                    = {980--996},
      Year                     = {2017}
    }
    
    @inproceedings{ou2016asymmetric,
      title                    = {Asymmetric transitivity preserving graph embedding},
      author                   = {Ou, Mingdong and Cui, Peng and Pei, Jian and Zhang, Ziwei and Zhu, Wenwu},
      booktitle                = {Proceedings of the 22nd ACM SIGKDD},
      pages                    = {1105--1114},
      year                     = {2016},
      organization             = {ACM}
    }

    @inproceedings{belkin2002laplacian,
      title                    = {Laplacian eigenmaps and spectral techniques for embedding and clustering},
      author                   = {Belkin, Mikhail and Niyogi, Partha},
      booktitle                = {Advances in neural information processing systems},
      pages                    = {585--591},
      year                     = {2002}
    }

    @inproceedings{ahmed2013distributed,
      title                    = {Distributed large-scale natural graph factorization},
      author                   = {Ahmed, Amr and Shervashidze, Nino and Narayanamurthy, Shravan and Josifovski, Vanja and Smola, Alexander J},
      booktitle                = {Proceedings of the 22nd international conference on World Wide Web},
      pages                    = {37--48},
      year                     = {2013},
      organization             = {ACM}
    }

    @inproceedings{wang2016structural,
      title                    = {Structural deep network embedding},
      author                   = {Wang, Daixin and Cui, Peng and Zhu, Wenwu},
      booktitle                = {Proceedings of the 22nd ACM SIGKDD international conference on Knowledge discovery and data mining},
      pages                    = {1225--1234},
      year                     = {2016},
      organization             = {ACM}
    }
