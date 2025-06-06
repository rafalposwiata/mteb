from __future__ import annotations

import itertools

import numpy as np
from datasets import Dataset, DatasetDict

from mteb.abstasks.AbsTaskClustering import AbsTaskClustering
from mteb.abstasks.AbsTaskClusteringFast import (
    AbsTaskClusteringFast,
    check_label_distribution,
)
from mteb.abstasks.TaskMetadata import TaskMetadata


class RedditClusteringP2P(AbsTaskClustering):
    superseded_by = "RedditClusteringP2P.v2"
    metadata = TaskMetadata(
        name="RedditClusteringP2P",
        description="Clustering of title+posts from reddit. Clustering of 10 sets of 50k paragraphs and 40 sets of 10k paragraphs.",
        reference="https://arxiv.org/abs/2104.07081",
        dataset={
            "path": "mteb/reddit-clustering-p2p",
            "revision": "385e3cb46b4cfa89021f56c4380204149d0efe33",
        },
        type="Clustering",
        category="p2p",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="v_measure",
        date=("2021-01-01", "2021-04-14"),
        domains=["Web", "Social", "Written"],
        task_subtypes=["Thematic clustering"],
        license="not specified",  # derived from pushshift
        annotations_creators="derived",
        dialect=[],
        sample_creation="found",
        bibtex_citation="""@article{geigle:2021:arxiv,
        author    = {Gregor Geigle and
                        Nils Reimers and
                        Andreas R{\"u}ckl{\'e} and
                        Iryna Gurevych},
        title     = {TWEAC: Transformer with Extendable QA Agent Classifiers},
        journal   = {arXiv preprint},
        volume    = {abs/2104.07081},
        year      = {2021},
        url       = {http://arxiv.org/abs/2104.07081},
        archivePrefix = {arXiv},
        eprint    = {2104.07081}
        }""",
        prompt="Identify the topic or theme of Reddit posts based on the titles and posts",
    )


class RedditFastClusteringP2P(AbsTaskClusteringFast):
    metadata = TaskMetadata(
        name="RedditClusteringP2P.v2",
        description="Clustering of title+posts from reddit. Clustering of 10 sets of 50k paragraphs and 40 sets of 10k paragraphs.",
        reference="https://arxiv.org/abs/2104.07081",
        dataset={
            "path": "mteb/reddit-clustering-p2p",
            "revision": "385e3cb46b4cfa89021f56c4380204149d0efe33",
        },
        type="Clustering",
        category="p2p",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="v_measure",
        date=("2021-01-01", "2021-04-14"),
        domains=["Web", "Social", "Written"],
        task_subtypes=["Thematic clustering"],
        license="not specified",
        annotations_creators="derived",
        dialect=[],
        sample_creation="found",
        bibtex_citation="""@article{geigle:2021:arxiv,
        author    = {Gregor Geigle and
                        Nils Reimers and
                        Andreas R{\"u}ckl{\'e} and
                        Iryna Gurevych},
        title     = {TWEAC: Transformer with Extendable QA Agent Classifiers},
        journal   = {arXiv preprint},
        volume    = {abs/2104.07081},
        year      = {2021},
        url       = {http://arxiv.org/abs/2104.07081},
        archivePrefix = {arXiv},
        eprint    = {2104.07081}
        }""",
        prompt="Identify the topic or theme of Reddit posts based on the titles and posts",
        adapted_from=["RedditClusteringP2P"],
    )

    def dataset_transform(self):
        ds = {}
        for split in self.metadata.eval_splits:
            labels = list(itertools.chain.from_iterable(self.dataset[split]["labels"]))
            sentences = list(
                itertools.chain.from_iterable(self.dataset[split]["sentences"])
            )

            check_label_distribution(self.dataset[split])

            # Remove sentences and labels with only 1 label example.
            unique_labels, counts = np.unique(labels, return_counts=True)
            solo_label_idx = np.where(counts == 1)
            solo_labels = unique_labels[solo_label_idx]
            for solo_label in solo_labels:
                loc = labels.index(solo_label)
                labels.pop(loc)
                sentences.pop(loc)
            ds[split] = Dataset.from_dict({"labels": labels, "sentences": sentences})

        self.dataset = DatasetDict(ds)
