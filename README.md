# GraphEmb

This is the official repository of the paper "Towards a more inductive world for drug repurposing approaches". 

<p align="center" width="100%">
    <img width="50%" src="https://raw.githubusercontent.com/ubioinformat/GraphEmb/main/imgs/graphical_abstract.png">
</p>

To facilitate the benchmark process, we assembled tools and code along this work and presented them as a package, as we believe it can address many limitations of current design and benchmarking processes within the development of *in-sillico* drug repurposing approaches (see Figure 1-G).

The rapid growth of machine learning within the graph embedding and drug repurposing areas has motivated a quick development of methodologies, promoting the fast deprecation of older approaches. This work revealed that some models dependencies have conflicts with recent python packages, or provide uncompleted and unmaintained code. To be able to run all the methods, we *dockerized* them allowing an easy execution on any machine. 

Similarly, building the required complementary matrices for every model is a highly demanding task. Most of the databases used at the moment of the method development are now updated, and this data needs to be retrieved in different ways (e.g., xml, tsv, APIs) with different identifiers (e.g., DrugBank, SIDER, PubChem, Uniprot). Moreover, the code necessary to access this information is often not included within the repositories of the models. For this reason, we provide a GitHub repository that includes the code to generate all the necessary matrices, allowing reproducibility of the drug repurposing evaluation.

Finally, the necessity of graph embedding tools for benchmarking drug repurposing methodologies became evident during the study. For this reason, we developed a Python package (named *GraphGuest*, available at https://github.com/ubioinformat/GraphGuest) to perform relevant tasks such as splitting the data, testing different criteria or handling negative subsampling. This package can ease the comparison of graph embedding approaches not only for DTIs, but also for other types of graph data. 




