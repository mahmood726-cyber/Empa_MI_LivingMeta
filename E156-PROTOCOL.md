# E156 Protocol — `Empa_MI_LivingMeta`

This repository is the source code and dashboard backing an E156 micro-paper on the [E156 Student Board](https://mahmood726-cyber.github.io/e156/students.html).

---

## `[445]` Empagliflozin Post-Myocardial Infarction: Living Meta-Analysis

**Type:** living-ma  |  ESTIMAND: HR for HF hospitalization or death  
**Data:** 1 RCT (EMPACT-MI), 6,522 patients; single-trial state (EMMY pending extraction)

### 156-word body

Does empagliflozin started early after acute myocardial infarction reduce heart failure hospitalisation or death in patients with preserved or reduced ejection fraction? One randomized placebo-controlled trial is currently deployed in this living meta-analysis: EMPACT-MI enrolled 6,522 patients with recent myocardial infarction within 14 days and compared empagliflozin 10 mg daily against placebo. Single-trial inverse-variance estimate used the original publication's Cox model hazard ratio and confidence interval. EMPACT-MI reported a hazard ratio of 0.90 (95% CI 0.76 to 1.06) for the primary composite of heart failure hospitalisation or death. The effect does not reach statistical significance and shows a smaller point estimate than that observed in chronic heart failure SGLT2 trials. Empagliflozin started post-myocardial infarction shows a directional but non-significant benefit in this single trial; the post-MI population differs from chronic HFrEF populations. EMMY and similar post-MI trials would update the pool; single-trial evidence remains preliminary.

### Submission metadata

```
Corresponding author: Mahmood Ahmad <mahmood.ahmad2@nhs.net>
ORCID: 0000-0001-9107-3704
Affiliation: Tahir Heart Institute, Rabwah, Pakistan

Links:
  Code:      https://github.com/mahmood726-cyber/Empa_MI_LivingMeta
  Protocol:  https://github.com/mahmood726-cyber/Empa_MI_LivingMeta/blob/main/E156-PROTOCOL.md
  Dashboard: https://mahmood726-cyber.github.io/empa_mi_livingmeta/

References (topic pack: restricted mean survival time / survival meta-analysis):
  1. Royston P, Parmar MK. 2013. Restricted mean survival time: an alternative to the hazard ratio for the design and analysis of randomized trials with a time-to-event outcome. BMC Med Res Methodol. 13:152. doi:10.1186/1471-2288-13-152
  2. Tierney JF, Stewart LA, Ghersi D, Burdett S, Sydes MR. 2007. Practical methods for incorporating summary time-to-event data into meta-analysis. Trials. 8:16. doi:10.1186/1745-6215-8-16

Data availability: No patient-level data used. Analysis derived exclusively
  from publicly available aggregate records. All source identifiers are in
  the protocol document linked above.

Ethics: Not required. Study uses only publicly available aggregate data; no
  human participants; no patient-identifiable information; no individual-
  participant data. No institutional review board approval sought or required
  under standard research-ethics guidelines for secondary methodological
  research on published literature.

Funding: None.

Competing interests: MA serves on the editorial board of Synthēsis (the
  target journal); MA had no role in editorial decisions on this
  manuscript, which was handled by an independent editor of the journal.

Author contributions (CRediT):
  [STUDENT REWRITER, first author] — Writing – original draft, Writing –
    review & editing, Validation.
  [SUPERVISING FACULTY, last/senior author] — Supervision, Validation,
    Writing – review & editing.
  Mahmood Ahmad (middle author, NOT first or last) — Conceptualization,
    Methodology, Software, Data curation, Formal analysis, Resources.

AI disclosure: Computational tooling (including AI-assisted coding via
  Claude Code [Anthropic]) was used to develop analysis scripts and assist
  with data extraction. The final manuscript was human-written, reviewed,
  and approved by the author; the submitted text is not AI-generated. All
  quantitative claims were verified against source data; cross-validation
  was performed where applicable. The author retains full responsibility for
  the final content.

Preprint: Not preprinted.

Reporting checklist: PRISMA 2020.

Target journal: ◆ Synthēsis (https://www.synthesis-medicine.org/index.php/journal)
  Section: Short Meta-Analysis — submit the 156-word E156 body verbatim as the main text.
  The journal caps main text at ≤400 words; E156's 156-word, 7-sentence
  contract sits well inside that ceiling. Do NOT pad to 400 — the
  micro-paper length is the point of the format.

Manuscript license: CC-BY-4.0.
Code license: MIT.

SUBMITTED: [ ]
```


---

_Auto-generated from the workbook by `C:/E156/scripts/create_missing_protocols.py`. If something is wrong, edit `rewrite-workbook.txt` and re-run the script — it will overwrite this file via the GitHub API._