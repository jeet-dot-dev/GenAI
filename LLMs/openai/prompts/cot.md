# Chain of Thought

Chain of Thought (CoT) reasoning is a technique used in prompting language models to improve their performance on complex tasks by encouraging step-by-step reasoning.

## What is Chain of Thought?

Chain of Thought involves breaking down a problem into intermediate steps, allowing the model to reason through each part before arriving at a final answer.

## Why Use Chain of Thought?

- **Improves accuracy**: Models are less likely to make mistakes when reasoning step by step.
- **Transparency**: You can see how the model arrived at its answer.
- **Handles complexity**: Useful for math, logic, and multi-step reasoning tasks.

## Examples

### Example 1: Math Problem

**Prompt:**
```
Q: If a train travels at 60 miles per hour for 3 hours, how far does it go?
Let's think step by step.
```

**Chain of Thought:**
- The train travels at 60 miles per hour.
- It travels for 3 hours.
- Distance = speed × time = 60 × 3 = 180 miles.
**Answer:** 180 miles.

---

### Example 2: Logical Reasoning

**Prompt:**
```
Q: All dogs are mammals. All mammals have hearts. Do dogs have hearts?
Let's think step by step.
```

**Chain of Thought:**
- All dogs are mammals.
- All mammals have hearts.
- Therefore, all dogs have hearts.
**Answer:** Yes, dogs have hearts.

---

### Example 3: Word Problem

**Prompt:**
```
Q: Sarah has 5 apples. She gives 2 to Tom and buys 4 more. How many apples does she have now?
Let's think step by step.
```

**Chain of Thought:**
- Sarah starts with 5 apples.
- She gives 2 apples to Tom: 5 - 2 = 3 apples left.
- She buys 4 more apples: 3 + 4 = 7 apples.
**Answer:** 7 apples.

---

## How to Write Chain of Thought Prompts

1. **Ask the model to reason step by step.**
    - Use phrases like "Let's think step by step" or "Let's break it down."
2. **Encourage intermediate steps.**
    - Guide the model to explain each part of the reasoning.
3. **Review the steps for correctness.**

## Tips

- Use CoT for tasks involving multiple steps or logical deductions.
- Combine with other prompting techniques for best results.

## References

- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)
- [OpenAI Cookbook: Chain of Thought](https://github.com/openai/openai-cookbook/blob/main/examples/Chain_of_Thought.ipynb)