You are a software engineer refactoring Python code.

## Inputs
1) Existing implementation file (content inserted below)
2) Pytest file(s) for this task (content inserted below)

## Goal
NEVER fix bugs note and continue. DO NOT FIX ANYTHING. DISREGARD CHANGE IF YOU ARE PREFACING IT AS A FIX. Refactor the implementation to improve readability while preserving code paths exactly as validated by the provided tests. 

## RULES MUST FOLLOW NEVER LIE 
- RULE 1 NEVER FIX BUGS
    - NEVER CHANGE OPERATORS even if incorrect note and continue
        - IMPORTANT ENSURE you don't say you didn't change an operator and change it anyway
    - NEVER correct arguments to a function even when they are wrong
    - NEVER change exact mathmatical formulas even if they are incorrect instead note the correct forumla and retain the incorrect formula


- Ensure when refactoring functions retain correct arguments


## Output Format (strict)
- Provide exactly one Python code block containing the full refactored implementation.
- After the code block, provide the checklist in 5 to 10 bullets.
- Do NOT include any additional text.
- Ensure all functions retain the exact name they had

---

## Implementation file content
<<<IMPLEMENTATION>>>
