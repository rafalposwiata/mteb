from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskSTS import AbsTaskSTS


class STS13STS(AbsTaskSTS):
    metadata = TaskMetadata(
        name="STS13",
        dataset={
            "path": "mteb/sts13-sts",
            "revision": "7e90230a92c190f1bf69ae9002b8cea547a64cca",
        },
        description="SemEval STS 2013 dataset.",
        reference="https://www.aclweb.org/anthology/S13-1004/",
        type="STS",
        category="s2s",
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="cosine_spearman",
        date=None,
        form=None,
        domains=None,
        task_subtypes=None,
        license=None,
        socioeconomic_status=None,
        annotations_creators=None,
        dialect=None,
        text_creation=None,
        bibtex_citation="""@inproceedings{Agirre2013SEM2S,
  title={*SEM 2013 shared task: Semantic Textual Similarity},
  author={Eneko Agirre and Daniel Matthew Cer and Mona T. Diab and Aitor Gonzalez-Agirre and Weiwei Guo},
  booktitle={International Workshop on Semantic Evaluation},
  year={2013},
  url={https://api.semanticscholar.org/CorpusID:10241043}
}""",
        n_samples=None,
        avg_character_length=None,
    )

    @property
    def metadata_dict(self) -> dict[str, str]:
        metadata_dict = super().metadata_dict
        metadata_dict["min_score"] = 0
        metadata_dict["max_score"] = 5
        return metadata_dict
