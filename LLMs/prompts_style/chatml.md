# chatml prompt

## What is ChatML?

ChatML is a markup language designed to structure prompts for conversational AI models. It helps organize messages between users and assistants, making interactions clear and easy to parse.

## Basic Structure

A ChatML prompt consists of a sequence of messages, each marked with a role (e.g., `system`, `user`, `assistant`). Each message is wrapped in tags:

```
<role>
Message content here
</role>
```

## Example

```text
<system>
You are a helpful assistant.
</system>
<user>
What's the weather like today?
</user>
<assistant>
The weather is sunny and warm.
</assistant>
```

## Detailed Notes

- **Roles**: Common roles are `system`, `user`, and `assistant`.
- **System Message**: Sets context or instructions for the assistant.
- **User Message**: Represents input from the user.
- **Assistant Message**: The AI's response.

### Multi-turn Conversation Example

```text
<system>
You are a travel expert.
</system>
<user>
Can you suggest places to visit in Japan?
</user>
<assistant>
Sure! Tokyo, Kyoto, and Osaka are popular destinations.
</assistant>
<user>
What is special about Kyoto?
</user>
<assistant>
Kyoto is known for its historic temples and beautiful gardens.
</assistant>
```

## Tips

- Always start with a `system` message for context.
- Alternate between `user` and `assistant` for dialogue.
- Use clear and concise language in each message.
