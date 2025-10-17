---
date modified: Friday, October 17th 2025, 1:34:34 pm
---
```table-of-contents
```

## Easy guides
### How to
- https://www.promptfoo.dev/docs/red-team/ 
- https://www.confident-ai.com/blog/red-teaming-llms-a-step-by-step-guide
- [Jailbreak Cookbook](https://github.com/General-Analysis/GA)
- https://github.com/nrimsky/LM-exp
- 
### Metrics
- DeepTeam redTeaming vulnerabilities :  https://docs.confident-ai.com/docs/red-teaming-introduction
- Promptfoo redTeaming plugins: https://www.promptfoo.dev/docs/red-team/plugins/
### Datasets
- **factual_errors**
    - Primary: TruthfulQA
        - Why: Designed to catch confidently false answers and common misconceptions.
        - Links: Paper [https://arxiv.org/abs/2109.07958](https://arxiv.org/abs/2109.07958) • 
        - HF [https://huggingface.co/datasets/truthfulqa/truthful_qa](https://huggingface.co/datasets/truthfulqa/truthful_qa) 
        - GitHub [https://github.com/sylinrl/TruthfulQA](https://github.com/sylinrl/TruthfulQA)
        - Fit to example: “Who was the first Black president…?” TruthfulQA includes many traps where models must correct false beliefs.
    - Alternatives (fact-checked, evidence-grounded):
        - FEVER (claim verification with Wikipedia evidence): [https://fever.ai](https://fever.ai/)
        - SciFact (scientific claims): [https://allenai.org/data/scifact](https://allenai.org/data/scifact)
        - VitaminC (contrastive evidence for verification): [https://github.com/TalSchuster/VitaminC](https://github.com/TalSchuster/VitaminC)

- **unsupported_claims**
    - Primary: FEVER
        - Why: Explicitly labels claims as Supported/Refuted/NotEnoughInfo with evidence sentences. Great to penalize assertions without support.
        - Links: [https://fever.ai](https://fever.ai/) 
        - HF mirror: [https://huggingface.co/datasets/fever](https://huggingface.co/datasets/fever)
        - Fit to example: “secretly Black president” → Refute; requires citing evidence or stating lack of evidence.
	-  Alternatives:
        - HoVer (multi-hop evidence): [https://hover-nlp.github.io](https://hover-nlp.github.io/) • HF: [https://huggingface.co/datasets/hover](https://huggingface.co/datasets/hover)
        - HotpotQA (requires supporting facts): [https://hotpotqa.github.io](https://hotpotqa.github.io/) • HF: [https://huggingface.co/datasets/hotpot_qa](https://huggingface.co/datasets/hotpot_qa)
        - SciFact (if focusing on scientific domains): [https://allenai.org/data/scifact](https://allenai.org/data/scifact)

- **input_overreliance**
    - Primary: CREPE (false presuppositions)
        - Why: Directly targets questions with false premises and includes annotations for presupposition and corrections.
        - Links: Paper [https://arxiv.org/abs/2211.17257](https://arxiv.org/abs/2211.17257) • Repo (data link in README) [https://github.com/velocityCavalry/CREPE](https://github.com/velocityCavalry/CREPE)
        - Fit to example: “If 2 + 2 = 6…” → Model should challenge/clarify the false premise rather than comply.
    - Strong complements:
        - SQuAD 2.0 (unanswerable questions; avoid forcing an answer): Paper [https://arxiv.org/abs/1806.03822](https://arxiv.org/abs/1806.03822) • HF [https://huggingface.co/datasets/squad_v2](https://huggingface.co/datasets/squad_v2)
        - MultiHoax (multi-hop false-premise questions): [https://arxiv.org/html/2506.00264](https://arxiv.org/html/2506.00264)
        - IfQA (counterfactual “if” questions): [https://arxiv.org/abs/2305.14010](https://arxiv.org/abs/2305.14010)
## Tools / libraries 
- DeepTeam
- promptfoo 
- Giskard

## Papers and research
- https://github.com/nrimsky/LM-exp

## News and updates
- [ r/ChatGPTJailbreak ](https://www.reddit.com/r/ChatGPTJailbreak/)
## Other resources 
- Check my github stars /lists to find some resources



