import { countTokens } from '@anthropic-ai/tokenizer';

function main(): void {
  const text: string = 'hello world!';
  const tokens: number = countTokens(text);
  console.log(`'${text}' is ${tokens} tokens`);
}

main();
