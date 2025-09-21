# Few Shot Prompting

Few-shot prompting is a technique used to guide large language models (LLMs) by providing a handful of examples in the prompt. This helps the model understand the desired format, style, or task.

## What is Few-Shot Prompting?

Few-shot prompting involves giving the model a small number of input-output pairs (examples) before asking it to generate a response for a new input. This is useful when you want the model to perform a specific task without fine-tuning.

## Structure

A typical few-shot prompt looks like:

```
Example 1:
Input: [input text]
Output: [desired output]

Example 2:
Input: [input text]
Output: [desired output]

...

Now, Input: [new input]
Output:
```

## Examples

### Example 1: Text Classification

```
Example 1:
Input: The movie was fantastic!
Output: Positive

Example 2:
Input: The food was terrible.
Output: Negative

Now, Input: The service was okay.
Output:
```

### Example 2: Translation

```
Example 1:
Input: Hello, how are you?
Output: Hola, ¿cómo estás?

Example 2:
Input: Good morning!
Output: ¡Buenos días!

Now, Input: Thank you very much.
Output:
```

### Example 3: Summarization

```
Example 1:
Input: The cat sat on the mat and looked out the window.
Output: Cat sat and watched outside.

Example 2:
Input: The weather was rainy, so we stayed inside.
Output: Stayed inside due to rain.

Now, Input: She read a book in the garden.
Output:
```

### Example 4: Math Problem Solving

```
Example 1:
Input: What is 2 + 2?
Output: 4

Example 2:
Input: What is 5 x 3?
Output: 15

Now, Input: What is 12 - 7?
Output:
```

## Tips for Effective Few-Shot Prompts

- Use clear and consistent formatting.
- Provide diverse examples covering edge cases.
- Keep examples relevant to the task.
- Limit the number of examples (typically 2-5).

## When to Use Few-Shot Prompting

- When zero-shot (no examples) performance is poor.
- When you want to specify a custom format or style.
- For tasks where labeled data is limited.

## Limitations

- May not work well for complex tasks.
- Model may not generalize beyond provided examples.
- Prompt length is limited by model context window.

## References

- [OpenAI Cookbook: Prompt Engineering](https://github.com/openai/openai-cookbook/blob/main/examples/Prompt_Engineering.md)
- [GPT-3 Paper](https://arxiv.org/abs/2005.14165)
