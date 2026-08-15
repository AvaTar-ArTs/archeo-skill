# Verification Protocol

Adapted from verification-before-completion.

## Evidence rule

Do not claim a repository, skill, build, test, fix, or migration is complete without fresh evidence.

## Gate

1. Identify the command, API response, diff, or file inspection that proves the claim.
2. Run the full check.
3. Read the output and exit status.
4. Compare the evidence to the claim.
5. Report success, partial completion, or failure precisely.

## Claim matrix

| Claim | Evidence |
|---|---|
| Repository contains a file | Fresh tree or contents listing |
| Skill is valid | Skill validator output |
| Parser is fixed | Regression fixtures covering the original malformed forms |
| Build passes | Full build command with exit 0 |
| Secret removed from source | Search over tracked source and diff inspection |
| Artifact is reproducible | Manifest plus provider/model/seed/reference metadata |
| PR is merged | Fresh PR state showing merged true |

## Negative evidence

Record what was not tested. Confidence should decrease when dependencies, credentials, models, or deployment targets are unavailable.
